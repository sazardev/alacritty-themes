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
  "gruvbox_hard_dark": "#fabd2f", "gruvbox_soft": "#fabd2f", "gruvbox_plum": "#cf86a8",
  "coffee": "#e0b050", "autumn": "#e8a23a", "desert_dusk": "#e0b46a", "terracotta": "#e2674e",
  "sunset_ember": "#ffb347", "nicotine": "#cfa94e", "sage": "#94b27e",
  "outrun": "#ff2975", "retrowave_sunset": "#ff5ac8", "miami_vice": "#3ff5c0",
  "vaporwave": "#d68cff", "laserwave": "#eb64b9", "retro_70s": "#e5ad2d",
  "space_age": "#ffc857", "atomic_age": "#5fcfc4", "blade_runner": "#ffb02e",
  "arcade_cabinet": "#ffe033", "candy": "#ff8cf0", "tropical": "#ffd23f", "aurora": "#6bffb0",
  "jewel": "#b05fe0", "festival": "#ffc933", "ocean_reef": "#38e0f0", "spring_bloom": "#e69ae8",
  "python": "#ffd43b", "rust": "#e5533d", "golang": "#00add8", "javascript": "#f7df1e",
  "typescript": "#5a9ae8", "ruby": "#ee4a4a", "php": "#7a86e0", "java": "#f2a33a",
  "kotlin": "#a97aff", "swift": "#f0503a", "csharp": "#c070d8", "elixir": "#b070f0",
  "haskell": "#a06ad8", "lua": "#5a78e8", "zig": "#f7a41d", "nodejs": "#68c657",
  "dart": "#13b9fd", "julia": "#b072d0",
  "espresso": "#e0a850", "cappuccino": "#e8b866", "americano": "#cba35a", "cortado": "#e0b070",
  "cafe_moka": "#c8789c", "caramel_macchiato": "#f0b840", "cold_brew": "#5cb8b0",
  "cafe_de_olla": "#e0a030", "flat_white": "#ddb86a", "irish_coffee": "#7fb06a",
  "turkish_coffee": "#e6a030", "affogato": "#ecc468", "cafe_bombon": "#f2c050",
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
