import os, pty, sys, time, select, struct, fcntl, termios, re, tomllib, signal

theme = sys.argv[1]
path = f"/mnt/c/Users/Omar/AppData/Roaming/alacritty/themes/{theme}.toml"
c = tomllib.load(open(path, "rb"))["colors"]
names = "black red green yellow blue magenta cyan white".split()
pal = {i: c["normal"][n] for i, n in enumerate(names)} | {8 + i: c["bright"][n] for i, n in enumerate(names)}
fg, bg = c["primary"]["foreground"], c["primary"]["background"]

def rgb(h):
    h = h.lstrip("#"); return "rgb:" + "/".join(h[i:i+2] * 2 for i in (0, 2, 4))

if len(sys.argv) > 2: os.environ["XDG_CONFIG_HOME"] = sys.argv[2]
pid, fd = pty.fork()
if pid == 0:
    os.environ["TERM"] = "alacritty-direct" if False else "xterm-256color"
    os.environ["COLORTERM"] = "truecolor"
    for k in [k for k in os.environ if "HERDR" in k.upper()]: del os.environ[k]
    os.execvp("herdr", ["herdr", "--session", "probe"])
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 36, 130, 0, 0))
buf = b""; log = b""
def pump(t):
    global buf, log
    end = time.time() + t
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.1)
        if not r: continue
        try: d = os.read(fd, 65536)
        except OSError: return
        buf += d; log += d
        for m in re.finditer(rb"\x1b\](\d+)(?:;(\d+))?;\?(?:\x07|\x1b\\)", d):
            op, idx = int(m.group(1)), m.group(2)
            if op == 4: os.write(fd, f"\x1b]4;{idx.decode()};{rgb(pal[int(idx)])}\x1b\\".encode())
            elif op == 10: os.write(fd, f"\x1b]10;{rgb(fg)}\x1b\\".encode())
            elif op == 11: os.write(fd, f"\x1b]11;{rgb(bg)}\x1b\\".encode())
        if b"\x1b[c" in d or b"\x1b[0c" in d: os.write(fd, b"\x1b[?62;c")
        if b"\x1b[6n" in d: os.write(fd, b"\x1b[1;1R")
pump(3)
os.write(fd, b"\x02v"); pump(2)   # prefix + split_vertical
os.write(fd, b"\x02-"); pump(2)   # prefix + split_horizontal
open(f"/tmp/alac-gen/probe_{theme}.raw", "wb").write(log)
try: os.kill(pid, signal.SIGKILL)
except Exception: pass
os.system("herdr --session probe server stop >/dev/null 2>&1")

# which SGR color precedes box-drawing chars?
text = log.decode("utf8", "replace")
inv = {}
for i, h in pal.items(): inv.setdefault(h.lower(), []).append(i)
inv[fg.lower()] = inv.get(fg.lower(), []) + ["fg"]; inv[bg.lower()] = inv.get(bg.lower(), []) + ["bg"]
from collections import Counter
cnt = Counter()
cur = None
for m in re.finditer(r"\x1b\[([0-9;:]*)m|([│─┌┐└┘├┤┬┴┼╭╮╰╯┃━])", text):
    if m.group(1) is not None:
        p = m.group(1).replace(":", ";").split(";")
        if "38" in p:
            j = p.index("38")
            if p[j+1:j+2] == ["2"] and len(p) >= j + 5: cur = "#%02x%02x%02x" % tuple(int(x) for x in p[j+2:j+5])
            elif p[j+1:j+2] == ["5"]: cur = ("idx", int(p[j+2]))
        elif m.group(1) in ("0", ""): cur = None
        else:
            for x in p:
                if x.isdigit() and 30 <= int(x) <= 37: cur = ("idx", int(x) - 30)
                if x.isdigit() and 90 <= int(x) <= 97: cur = ("idx", int(x) - 90 + 8)
    else:
        cnt[cur] += 1
print("queries answered; border-glyph colors (count):")
for k, v in cnt.most_common(8):
    label = k
    if isinstance(k, str): label = f"{k} -> slots {inv.get(k.lower())}"
    print(" ", v, label)
