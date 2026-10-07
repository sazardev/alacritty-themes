"""Agrega a cada tema las secciones de Alacritty que le falten (cursor, selection,
search, footer_bar, hints, vi_mode_cursor), derivadas de su propia paleta.
Idempotente: solo agrega tablas ausentes. Correr DESPUES de gen.py.
uso: python3 -I enrich.py <dir> [<dir>...]"""
import sys, os, tomllib

NAMES = "black red green yellow blue magenta cyan white".split()
# color "firma" (cursor / selección) para temas con identidad propia; el resto usa fg
ACCENT = {
  "cyberpunk_2077": "#fcee0a", "arasaka": "#e8202a", "edgerunners": "#ff4fd8",
  "viper": "#b6ff2e", "valorant": "#ff4655", "jett": "#6fe3ff", "jinx": "#ff4fa8",
  "zaun": "#7dff5a", "halo": "#e0b030", "cortana": "#5ad7ff", "pipboy": "#3dff55",
  "sheikah": "#ff9a1f", "n7": "#e4352b", "doom_slayer": "#ff3a1a", "creeper": "#5ac14a",
  "hollow_knight": "#a4bef0", "elden_ring": "#e6c065", "tron_legacy": "#00e5ff",
  "hextech": "#c8aa6e", "overwatch": "#f99e1a", "aperture": "#ff9a00",
  "lemon_lime": "#f2e03a", "forest_gold": "#d9a93a", "matcha": "#9ccc65",
  "radioactive": "#a8ff00", "jungle": "#3ecf6e", "swamp": "#c8a830", "amber_crt": "#ffb000",
}

def rgb(h): h = h.lstrip("#"); return [int(h[i:i+2], 16) for i in (0, 2, 4)]
def hexc(c): return "#%02x%02x%02x" % tuple(round(x) for x in c)
def mix(a, b, t): return hexc([x + (y - x) * t for x, y in zip(rgb(a), rgb(b))])
def lum(h):
    c = [x / 255 for x in rgb(h)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def cr(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def readable_on(bg, prefer):
    return prefer if cr(prefer, bg) >= 4.5 else max(("#000000", "#ffffff"), key=lambda c: cr(c, bg))

def enrich(path):
    name = os.path.basename(path)[:-5]
    c = tomllib.load(open(path, "rb"))["colors"]
    bg, fg = c["primary"]["background"], c["primary"]["foreground"]
    b = [c.get("bright", c["normal"])[n] for n in NAMES]
    acc = ACCENT.get(name, fg)
    if cr(acc, bg) < 3: acc = fg
    out = []
    if "cursor" not in c:
        out.append(f"[colors.cursor]\ntext = '{bg}'\ncursor = '{acc}'\n")
    if "vi_mode_cursor" not in c:
        vi = b[6] if b[6].lower() != acc.lower() else b[3]
        out.append(f"[colors.vi_mode_cursor]\ntext = '{bg}'\ncursor = '{vi}'\n")
    if "selection" not in c:
        hue = acc if acc.lower() != fg.lower() else b[4]
        t = 0.38
        sel = mix(bg, hue, t)
        while cr(fg, sel) < 4.5 and t > 0.05:
            t -= 0.03; sel = mix(bg, hue, t)
        out.append(f"[colors.selection]\ntext = '{fg}'\nbackground = '{sel}'\n")
    s = c.get("search", {})
    if "matches" not in s:
        out.append(f"[colors.search.matches]\nforeground = '{readable_on(b[3], bg)}'\nbackground = '{b[3]}'\n")
    if "focused_match" not in s:
        out.append(f"[colors.search.focused_match]\nforeground = '{readable_on(b[1], bg)}'\nbackground = '{b[1]}'\n")
    if "footer_bar" not in c:
        out.append(f"[colors.footer_bar]\nforeground = '{fg}'\nbackground = '{mix(bg, fg, 0.18)}'\n")
    h = c.get("hints", {})
    if "start" not in h:
        out.append(f"[colors.hints.start]\nforeground = '{readable_on(b[3], bg)}'\nbackground = '{b[3]}'\n")
    if "end" not in h:
        out.append(f"[colors.hints.end]\nforeground = '{readable_on(b[4], bg)}'\nbackground = '{b[4]}'\n")
    if out:
        txt = open(path).read().rstrip("\n")
        open(path, "w").write(txt + "\n\n# --- derivado de la paleta (enrich.py) ---\n" + "\n".join(out))
    return len(out)

if __name__ == "__main__":
    for d in sys.argv[1:]:
        added = 0
        for f in sorted(os.listdir(d)):
            if f.endswith(".toml"): added += enrich(os.path.join(d, f)) > 0
        print(f"{d}: {added} temas actualizados")
