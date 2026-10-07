import sys, os

# name: (title, bg, fg, normal[8], bright[8])  order: black red green yellow blue magenta cyan white
T = {}
def t(name, title, bg, fg, normal, bright):
    T[name] = (title, bg, fg, normal.split(), bright.split())

t("monokai", "Monokai (base16)", "#272822", "#f8f8f2",
  "#272822 #f92672 #a6e22e #f4bf75 #66d9ef #ae81ff #a1efe4 #f8f8f2",
  "#75715e #f92672 #a6e22e #f4bf75 #66d9ef #ae81ff #a1efe4 #f9f8f5")
t("tomorrow_night", "Tomorrow Night", "#1d1f21", "#c5c8c6",
  "#1d1f21 #cc6666 #b5bd68 #f0c674 #81a2be #b294bb #8abeb7 #c5c8c6",
  "#969896 #cc6666 #b5bd68 #f0c674 #81a2be #b294bb #8abeb7 #ffffff")
t("tomorrow_night_eighties", "Tomorrow Night Eighties", "#2d2d2d", "#cccccc",
  "#2d2d2d #f2777a #99cc99 #ffcc66 #6699cc #cc99cc #66cccc #cccccc",
  "#999999 #f2777a #99cc99 #ffcc66 #6699cc #cc99cc #66cccc #ffffff")
t("nightfox", "Nightfox", "#192330", "#cdcecf",
  "#393b44 #d65b79 #81b29a #dbc074 #719cd6 #9d79d6 #63cdcf #dfdfe0",
  "#5f6b94 #d16983 #8ebaa4 #e0c989 #86abdc #baa1e2 #7ad5d6 #e4e4e5")
t("carbonfox", "Carbonfox", "#161616", "#f2f4f8",
  "#282828 #ee5396 #25be6a #08bdba #78a9ff #be95ff #33b1ff #dfdfe0",
  "#6e6e6e #f16da6 #46c880 #2dc7c4 #8cb6ff #c8a5ff #52bdff #e4e4e5")
t("gruvbox_material_dark", "Gruvbox Material Dark", "#282828", "#d4be98",
  "#3c3836 #ea6962 #a9b665 #d8a657 #7daea3 #d3869b #89b482 #d4be98",
  "#7c6f64 #ea6962 #a9b665 #d8a657 #7daea3 #d3869b #89b482 #ddc7a1")
t("palenight", "Material Palenight", "#292d3e", "#a6accd",
  "#292d3e #f07178 #c3e88d #ffcb6b #82aaff #c792ea #89ddff #d0d0d0",
  "#7580ad #ff8b92 #ddffa7 #ffe585 #9cc4ff #e1acff #a3f7ff #ffffff")
t("horizon_dark", "Horizon Dark", "#1c1e26", "#d5d8da",
  "#16161c #e95678 #29d398 #fab795 #26bbd9 #ee64ac #59e1e3 #d5d8da",
  "#6c6f93 #ec6a88 #3fdaa4 #fbc3a7 #3fc4de #f075b5 #6be4e6 #d5d8da")
t("tokyo_night_moon", "Tokyo Night Moon", "#222436", "#c8d3f5",
  "#1b1d2b #ff757f #c3e88d #ffc777 #82aaff #c099ff #86e1fc #828bb8",
  "#636da6 #ff8d94 #c7fb6d #ffd8ab #9ab8ff #caabff #b2ebff #c8d3f5")
t("oxocarbon", "Oxocarbon Dark (IBM Carbon)", "#161616", "#f2f4f8",
  "#262626 #ee5396 #42be65 #ffe97b #33b1ff #be95ff #3ddbd9 #dde1e6",
  "#6f6f6f #ff7eb6 #42be65 #ffe97b #78a9ff #be95ff #08bdba #ffffff")
t("cyberdream", "Cyberdream", "#16181a", "#ffffff",
  "#16181a #ff6e5e #5eff6c #f1ff5e #5ea1ff #bd5eff #5ef1ff #ffffff",
  "#6b7076 #ff6e5e #5eff6c #f1ff5e #5ea1ff #bd5eff #5ef1ff #ffffff")
t("iceberg", "Iceberg", "#161821", "#c6c8d1",
  "#1e2132 #e27878 #b4be82 #e2a478 #84a0c6 #a093c7 #89b8c2 #c6c8d1",
  "#6b7089 #e98989 #c0ca8e #e9b189 #91acd1 #ada0d3 #95c4ce #d2d4de")
t("github_dark_dimmed", "GitHub Dark Dimmed", "#22272e", "#adbac7",
  "#545d68 #f47067 #57ab5a #c69026 #539bf5 #b083f0 #39c5cf #909dab",
  "#768390 #ff938a #6bc46d #daaa3f #6cb6ff #dcbdfb #56d4dd #cdd9e5")
t("github_dark_high_contrast", "GitHub Dark High Contrast", "#0a0c10", "#f0f3f6",
  "#7a828e #ff9492 #26cd4d #f0b72f #71b7ff #cb9eff #39c5cf #d9dee3",
  "#9ea7b3 #ffb1af #4ae168 #f7c843 #91cbff #dbb7ff #56d4dd #ffffff")
t("flexoki_dark", "Flexoki Dark", "#100f0f", "#cecdc3",
  "#1c1b1a #d14d41 #879a39 #d0a215 #4385be #ce5d97 #3aa99f #cecdc3",
  "#6f6e69 #e8705f #a0af54 #dfb431 #66a0c8 #e47da8 #5abdac #fffcf0")
t("nightfly", "Nightfly", "#011627", "#c3ccdc",
  "#1d3b53 #fc514e #a1cd5e #e3d18a #82aaff #c792ea #7fdbca #a1aab8",
  "#7c8f8f #ff5874 #21c7a8 #ecc48d #82aaff #ae81ff #7fdbca #d6deeb")
t("mellow", "Mellow", "#161617", "#c9c7cd",
  "#27272a #f5a191 #90b99f #e6b99d #aca1cf #e29eca #ea83a5 #c1c0d4",
  "#6b6b75 #ffae9f #9dc6ac #f0c5a9 #b9aeda #ecaad6 #f591b2 #cac9dd")
t("poimandres", "Poimandres", "#1b1e28", "#a6accd",
  "#1b1e28 #d0679d #5de4c7 #fffac2 #89ddff #fcc5e9 #add7ff #ffffff",
  "#5f7290 #d0679d #5de4c7 #fffac2 #add7ff #fae4fc #89ddff #ffffff")
t("sonokai", "Sonokai", "#2c2e34", "#e2e2e3",
  "#181819 #fc5d7c #9ed072 #e7c664 #76cce0 #b39df3 #f39660 #e2e2e3",
  "#7f8490 #fc5d7c #9ed072 #e7c664 #76cce0 #b39df3 #f39660 #e2e2e3")
t("snazzy", "Snazzy", "#282a36", "#eff0eb",
  "#282a36 #ff5c57 #5af78e #f3f99d #57c7ff #ff6ac1 #9aedfe #f1f1f0",
  "#7a7a7a #ff5c57 #5af78e #f3f99d #57c7ff #ff6ac1 #9aedfe #f1f1f0")
t("vscode_dark_plus", "VS Code Dark+", "#1e1e1e", "#cccccc",
  "#000000 #e5484d #0dbc79 #e5e510 #3b8eea #c75fc7 #11a8cd #e5e5e5",
  "#666666 #f14c4c #23d18b #f5f543 #3b8eea #d670d6 #29b8db #e5e5e5")
t("ubuntu", "Ubuntu", "#300a24", "#eeeeec",
  "#2e3436 #e0443e #4e9a06 #c4a000 #4a7fc4 #ad7fa8 #06989a #d3d7cf",
  "#75757a #ef2929 #8ae234 #fce94f #729fcf #ad7fa8 #34e2e2 #eeeeec")
t("moonfly", "Moonfly", "#080808", "#bdbdbd",
  "#323437 #ff5454 #8cc85f #e3c78a #80a0ff #cf87e8 #79dac8 #c6c6c6",
  "#949494 #ff5189 #36c692 #c2c292 #74b2ff #ae81ff #85dc85 #e4e4e4")
t("oceanic_next", "Oceanic Next", "#1b2b34", "#c0c5ce",
  "#1b2b34 #ec5f67 #99c794 #fac863 #6699cc #c594c5 #5fb3b3 #c0c5ce",
  "#65737e #ec5f67 #99c794 #fac863 #6699cc #c594c5 #5fb3b3 #d8dee9")
t("challenger_deep", "Challenger Deep", "#1e1c31", "#cbe3e7",
  "#141228 #ff5458 #62d196 #ffe9aa #65b2ff #906cff #63f2f1 #a6b3cc",
  "#6c6a94 #ff8080 #95ffa4 #ffe9aa #91ddff #c991e1 #aaffe4 #cbe3e7")
t("everblush", "Everblush", "#141b1e", "#dadada",
  "#232a2d #e57474 #8ccf7e #e5c76b #67b0e8 #c47fd5 #6cbfbf #b3b9b8",
  "#66737a #ef7e7e #96d988 #f4d67a #71baf2 #ce89df #67cbe7 #bdc3c2")

# ---- videojuegos (inspirados, paletas originales) ----
t("cyberpunk_2077", "Cyberpunk 2077 (inspired)", "#0b0c10", "#e9e7c8",
  "#1b1d26 #ff2a4d #8ee05a #fcee0a #3b9cff #ff4fc3 #00f0ff #d9d7bd",
  "#5c6070 #ff6b81 #aaf27a #fff35c #6fb8ff #ff7fd6 #6ff7ff #fffde8")
t("arasaka", "Arasaka (inspired)", "#0a0a0a", "#e8e8e8",
  "#1c1c1c #e8202a #7fae7f #d9b44a #6f8fb5 #c0607a #6fb5b5 #cfcfcf",
  "#666666 #ff4d55 #9fcf9f #f0cc66 #8fb0d6 #de7f98 #8fd5d5 #ffffff")
t("edgerunners", "Cyberpunk Edgerunners (inspired)", "#0e0b1a", "#ebe6ff",
  "#1d1830 #ff4f7b #b6ff3b #ffe14d #5a8cff #ff4fd8 #2ee6d6 #d6d0ef",
  "#665e8c #ff7f9f #cdff72 #fff080 #8aaeff #ff7fe4 #6ff2e6 #ffffff")
t("viper", "Valorant Viper (inspired)", "#050c08", "#d4f2de",
  "#0e1a13 #ff4d5e #39e46a #c6f432 #2ba6b8 #a85cff #1fe0b0 #b7d1c0",
  "#4f7260 #ff7482 #7dff9f #e4ff6a #5ccbdc #c48cff #66f5d2 #f0fff5")
t("valorant", "Valorant (inspired)", "#0f1923", "#ece8e1",
  "#1f2c3a #ff4655 #5fd0a0 #e6c45a #4a90d9 #c46bd6 #0ac8b9 #ece8e1",
  "#5b6b7c #ff6f7b #7fe6bb #f3d77c #74aef0 #dc8ce8 #3fe0d2 #ffffff")
t("jett", "Valorant Jett (inspired)", "#0f1a26", "#eaf6ff",
  "#1d2c3d #ff7a8a #6fe0b0 #ffe08a #5aa9ff #b49cff #6fe3ff #d4e4f2",
  "#5f7790 #ff9aa6 #96efc7 #fff0b0 #86c2ff #cdbcff #9aefff #ffffff")
t("jinx", "Arcane Jinx (inspired)", "#12101c", "#e8e3f2",
  "#1f1b30 #ff5c8a #7be0a8 #ffd35c #4cc9f0 #ff4fa8 #3de0e0 #cfc8e0",
  "#615b80 #ff85a8 #a2f0c4 #ffe28a #7cd9f6 #ff7fc2 #75ecec #ffffff")
t("zaun", "Arcane Zaun (inspired)", "#0e1411", "#d8e8d0",
  "#19241d #ff6a5a #7dff5a #e6f03c #4fa8e0 #b45fe0 #3fe0b8 #bcd0b4",
  "#556b5c #ff9082 #a2ff88 #f4ff7a #7cc2f0 #cc88f0 #78f0cf #f4fff0")
t("halo", "Halo Master Chief (inspired)", "#11140e", "#d5dcc5",
  "#1d2218 #d9503e #8bab4e #e0b030 #5b92e0 #b07acc #46c8e0 #bcc5aa",
  "#5d6650 #f07a68 #aed06e #f5cc55 #85b0f0 #cb9ae0 #78dcf0 #eef4de")
t("cortana", "Halo Cortana (inspired)", "#060b1c", "#cfe6ff",
  "#101a3a #ff6b8a #5fe0b0 #ffd36b #4d8dff #b57bff #5ad7ff #b4c9e6",
  "#5a6ea6 #ff94ab #8aefca #ffe39a #7fadff #cfa6ff #8ae6ff #ffffff")
t("pipboy", "Fallout Pip-Boy (inspired)", "#031304", "#3dff55",
  "#0a2410 #e8644a #3dff55 #d6e84a #37c97a #7fe0a0 #2ee6b0 #8fe89a",
  "#2c7a38 #ff8a70 #7dff8f #f0ff7a #5de89a #a8f0c0 #6ff5cc #d0ffd6")
t("sheikah", "Zelda Sheikah Slate (inspired)", "#0a1419", "#cfeff7",
  "#14262e #ff6b5a #7fe0a0 #ff9a1f #38a8ff #a58cf0 #38c8ff #b4d4dc",
  "#4c6a75 #ff907f #a2efbc #ffb855 #6cc0ff #c0acf6 #72dcff #ffffff")
t("n7", "Mass Effect N7 (inspired)", "#0c0d10", "#e8e8e8",
  "#1e2128 #e4352b #6bbf6b #e8a33a #4a8fd9 #b070d0 #4ac8d8 #cfd2d8",
  "#606674 #ff6a5e #8fdc8f #f5bf63 #78aef0 #cc92e6 #7ae0ee #ffffff")
t("doom_slayer", "Doom Slayer (inspired)", "#120a08", "#e8d8c8",
  "#241612 #ff3a1a #6bd13a #ffb01a #4a8fd0 #c060b0 #3ac8b0 #cdbdad",
  "#7a5d52 #ff6a4a #92e667 #ffc94a #78acea #d88ac8 #6adcc8 #fff4e8")
t("creeper", "Minecraft Creeper (inspired)", "#0f1a0d", "#c9e8b8",
  "#1b2b18 #e0614a #5ac14a #e0d24a #4a9ad0 #a870c8 #3ac8a0 #b0cc9c",
  "#567050 #f48a74 #86dd76 #f2e67a #78b8e8 #c498dc #6ae0be #ecfce0")
t("hollow_knight", "Hollow Knight (inspired)", "#0b0d14", "#dfe6f2",
  "#171b28 #e0707c #7ec8a8 #e0c070 #7a9cd8 #a890d8 #7ad0e0 #c4cedc",
  "#5a6480 #f09aa4 #a4dcc4 #f0d898 #a4bef0 #c4b4ee #a4e4f0 #ffffff")
t("elden_ring", "Elden Ring (inspired)", "#0f0d0a", "#e8dcc0",
  "#1f1b14 #d9593f #8aa860 #e6c065 #6a8ec0 #a878b8 #62b0a8 #c8bca0",
  "#6a604a #ee826a #aac882 #f5d88a #92b0dc #c49ad0 #8ccdc4 #fff4d8")
t("tron_legacy", "Tron Legacy (inspired)", "#05080f", "#aee6ff",
  "#0f1a2a #ff5a4a #4af0a0 #ffd23a #3a9cff #b06cff #00e5ff #9cc8dc",
  "#4d7aa0 #ff857a #7af7bf #ffe37a #70b8ff #cc9aff #7af0ff #ffffff")
t("hextech", "League Hextech (inspired)", "#091428", "#f0e6d2",
  "#172540 #e8606a #5fc8a0 #c8aa6e #4a8ad8 #a880d8 #0ac8b9 #c8bca0",
  "#5a6a85 #f58a92 #86dcb8 #e6cd8c #78a8f0 #c4a4ec #3fe0d2 #f0e6d2")
t("overwatch", "Overwatch (inspired)", "#1b1e2b", "#edf0f5",
  "#2a2f42 #fa4454 #4cd68c #f99e1a #218ffe #a07cf0 #34d4e8 #c8cede",
  "#6a7290 #ff7380 #7ae6ac #ffbd54 #5aaeff #bda2f8 #70e4f2 #ffffff")
t("aperture", "Portal Aperture (inspired)", "#0f1114", "#e8e8e8",
  "#1d2026 #ff5a4a #6fd08a #ff9a00 #00a8ff #b080e0 #30d0d8 #c8c8c8",
  "#626872 #ff8070 #96e4a8 #ffb84a #55c4ff #c8a4ee #66e2e8 #ffffff")
# ---- verdes y amarillos ----
t("lemon_lime", "Lemon Lime", "#0f1a0a", "#e8f2c8",
  "#1c2b14 #f0634a #7cd62f #f2e03a #4aa3d0 #b080d0 #3ad0a0 #cdd8ae",
  "#5e7548 #ff8d78 #a4ee5c #fff46a #7ac0e4 #cca0e4 #6ae6bc #fbffe6")
t("forest_gold", "Forest Gold", "#101810", "#dcd6b0",
  "#1c281c #d96a50 #6fae5a #d9a93a #5a8fb0 #a07ab0 #4aa89a #c4bf9c",
  "#5f7258 #ee9078 #94cc80 #f0c866 #86b0cc #c09ccc #78c4b6 #f6f0d0")
t("matcha", "Matcha (dark)", "#1a2118", "#d8e4cc",
  "#28321f #e07a6a #9ccc65 #e6d56a #6aa8c8 #b896c8 #6ac4a8 #c0ccb0",
  "#6a7a5c #f0a090 #bcdf8a #f2e68c #92c4dc #d0b4dc #92dcc4 #f4fbe8")
t("radioactive", "Radioactive", "#080a06", "#e0f0b8",
  "#151a0e #ff5030 #a8ff00 #ffe600 #3aa0ff #d060ff #00e0a0 #c0cca0",
  "#5a6a3c #ff7a5c #c4ff4a #fff266 #70bcff #e08cff #4af0bc #f8ffe0")
t("jungle", "Jungle", "#0b1810", "#d0e8d0",
  "#162a1c #f0705a #3ecf6e #f0c83a #3a9ad0 #c070c0 #2ed0b8 #b4ccb4",
  "#4f7258 #ff9a86 #6ee898 #ffe066 #6ab8e8 #d898d8 #62e8d2 #f0fff0")
t("swamp", "Swamp", "#14180e", "#cfd2a8",
  "#232a16 #d4684a #8ea63a #c8a830 #5a8aa0 #9a7aa8 #4a9a80 #b4b890",
  "#666c48 #e8907a #b0c85a #e0c860 #86aac0 #b69cc4 #78baa0 #eceec4")
t("amber_crt", "Amber CRT", "#120c02", "#ffb000",
  "#241804 #ff5a3a #b8c030 #ffb000 #d08a30 #e8806a #d0c870 #ffd070",
  "#7a5a1a #ff8060 #d4dc50 #ffc83a #e8a850 #f4a090 #e8e090 #fff0c0")

# ---- familias nuevas: gruvbox/cálidos, retrowave/retrofuturista, colorful ----
# t2 solo recibe el matiz base; deriva negro, bright y bright black con reglas fijas
# y aclara cualquier color que no llegue a 4.3:1 contra el fondo.
def _rgb(h): h = h.lstrip("#"); return [int(h[i:i+2], 16) for i in (0, 2, 4)]
def _hex(c): return "#%02x%02x%02x" % tuple(max(0, min(255, round(x))) for x in c)
def _mix(a, b, k): return _hex([x + (y - x) * k for x, y in zip(_rgb(a), _rgb(b))])
def _lum(h):
    c = [x / 255 for x in _rgb(h)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def _cr(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def _lift(c, bg, need):
    k = 0.0
    while _cr(c, bg) < need and k < 1:
        k += 0.03; c = _mix(c, "#ffffff", 0.03 / (1 - k + 0.03) if k < 0.97 else 1)
    return c
def t2(name, title, bg, fg, base):
    cols = [_lift(c, bg, 4.3) for c in base.split()]           # red..white
    black = _mix(bg, fg, 0.12)
    bb = bg
    for k in range(20, 80, 2):                                  # bright black >= 3.3:1
        bb = _mix(bg, fg, k / 100)
        if _cr(bb, bg) >= 3.3: break
    bright = [_mix(c, "#ffffff", 0.22) for c in cols[:6]] + [_mix(cols[6], "#ffffff", 0.6)]
    T[name] = (title, bg, fg, [black] + cols, [bb] + bright)

# Gruvbox y cálidos apagados
t2("gruvbox_hard_dark", "Gruvbox Hard Dark", "#1d2021", "#ebdbb2", "#e5513f #a8a52a #e0a526 #6fa0a8 #c97b95 #8ec07c #d5c4a1")
t2("gruvbox_soft", "Gruvbox Soft", "#32302f", "#ebdbb2", "#e5604a #aaa83a #e3aa3a #78a5ad #cf88a0 #93c482 #d5c4a1")
t2("gruvbox_plum", "Gruvbox Plum", "#2a2229", "#e8d7c6", "#e0605a #a6b05c #e3b04b #78a0b5 #cf86a8 #85bfa5 #cdbfb0")
t2("coffee", "Coffee", "#1f1a16", "#e6d5b8", "#d9644a #a3a860 #e0b050 #7fa5a8 #c08a9c #86b89a #cdbfa3")
t2("autumn", "Autumn", "#1c1512", "#e8d3b5", "#d9553b #9aa84a #e8a23a #6a94a8 #b8708a #6fae94 #cbb99a")
t2("desert_dusk", "Desert Dusk", "#201a1a", "#e3d2c3", "#d66a5c #9db17c #e0b46a #7f9fb8 #c487a0 #7fbfae #cdbaa8")
t2("terracotta", "Terracotta", "#231815", "#f0dccb", "#e2674e #8fae6a #eab255 #6f9bbd #d17f9c #66b7a5 #d4bfae")
t2("sunset_ember", "Sunset Ember", "#1a1114", "#f2d8c8", "#ff5a4d #b9c25a #ffb347 #7aa2d6 #e56b9f #5fc9b5 #d8c0b4")
t2("nicotine", "Nicotine", "#221e18", "#d9ccb0", "#c9654f #8f9d5a #cfa94e #6f8fa0 #a77a8c #6fa08c #bfb398")
t2("sage", "Sage", "#1c211e", "#d6dccb", "#cf7a6a #94b27e #d5b86c #7fa0b4 #b58aa5 #78b5a5 #c2cab5")
# Retrowave / retrofuturista
t2("outrun", "Outrun", "#0d0221", "#f1e6ff", "#ff2975 #0be881 #f9f871 #4d7cff #ff2fd1 #00e5ff #d9c8f5")
t2("retrowave_sunset", "Retrowave Sunset", "#1a0b2e", "#ffe9f3", "#ff4f6d #7bf0a0 #ffb347 #6f8cff #ff5ac8 #4dd8ff #e8cfe8")
t2("miami_vice", "Miami Vice", "#0c1b2a", "#f4f1ff", "#ff5a7a #3ff5c0 #ffe36e #4aa8ff #ff6ad5 #2fe6e6 #d6e4f0")
t2("vaporwave", "Vaporwave", "#1b1230", "#f0e0ff", "#ff7aa8 #8cffc4 #fff29a #8fb4ff #d68cff #8ff5f5 #e4d4f4")
t2("laserwave", "Laserwave", "#27212e", "#e0e0e0", "#eb64b9 #74dfc4 #ffe261 #40b4c4 #b381c5 #6bd5e8 #e0d8e8")
t2("retro_70s", "Retro 70s", "#1f1812", "#f0dfc0", "#d9482b #8fa03a #e5ad2d #3d8fa8 #c4608a #4fb3a0 #d9c8a8")
t2("space_age", "Space Age", "#0b1520", "#d8ecf0", "#ff6a4a #7fd8a0 #ffc857 #4aa3d6 #d77fb0 #4fd8d0 #cfe0e4")
t2("atomic_age", "Atomic Age", "#1b2226", "#efe6d2", "#f26b5b #7cc4a0 #f2c14e #5aa5c9 #d98aa8 #5fcfc4 #d8ceb8")
t2("blade_runner", "Blade Runner", "#0a0f18", "#d0d8e0", "#ff4a3d #66d9a8 #ffb02e #3a9ad9 #e0509a #2fd4d0 #b8c4cc")
t2("arcade_cabinet", "Arcade Cabinet", "#0a0a1a", "#f0f0ff", "#ff3355 #33ff77 #ffe033 #3377ff #ff33cc #33eeff #e0e0ee")
# Colorful
t2("candy", "Candy", "#1c1426", "#fdf0ff", "#ff6b8b #7dffb2 #ffe66d #6bb5ff #ff8cf0 #6bf5ff #f0dcf5")
t2("prism", "Prism", "#101018", "#eeeef6", "#ff5555 #55e07a #f5d442 #5588ff #cc66ff #44ddee #d8d8e4")
t2("tropical", "Tropical", "#0d1f1f", "#f0f5e0", "#ff6a5e #6be37a #ffd23f #3fa7ff #ff6fb5 #2fe0c8 #d8e8d0")
t2("aurora", "Aurora", "#0a1620", "#d8f0f0", "#ff7088 #6bffb0 #e8f08a #6aa0ff #b88cff #5ff0e0 #c8dce4")
t2("jewel", "Jewel", "#120f1a", "#ece6f4", "#e0455f #2fcf8a #f0b43a #4a78e8 #b05fe0 #2fc4cf #cfc8dc")
t2("festival", "Festival", "#1a0f0a", "#fff0e0", "#ff4d3d #8be04a #ffc933 #4aa8ff #ff52a8 #3fe0c0 #e8d8c8")
t2("ocean_reef", "Ocean Reef", "#07182a", "#e0f4ff", "#ff6f7a #5ef0b0 #ffd86a #4aa8ff #ff7ac8 #38e0f0 #cce4f0")
t2("spring_bloom", "Spring Bloom", "#1d1822", "#f3e8f0", "#ff8a9a #a8e68a #ffe08a #8ab8ff #e69ae8 #8ae6e0 #e0d4e0")

# ---- lenguajes de programación (inspirados en el color de marca de cada uno) ----
t2("python", "Python", "#11161d", "#e6edf3", "#e5646a #6fcf8a #ffd43b #5b9bd5 #b08ee0 #4fc3d9 #cfd8e3")
t2("rust", "Rust", "#1a1512", "#ecdcc8", "#e5533d #9db563 #e6a756 #6e9cb8 #c4789a #6fb5a8 #d1c0aa")
t2("golang", "Go", "#0f1a22", "#e0f0f5", "#f0675a #5fd0a0 #f0cc60 #3fa8e0 #b387d9 #00c8e8 #cbdde6")
t2("javascript", "JavaScript", "#121212", "#f0eee0", "#ff6159 #7ed957 #f7df1e #5aa6f5 #d57ae0 #4fd6d0 #d8d4c0")
t2("typescript", "TypeScript", "#0f1824", "#e0e8f4", "#f0646e #6fd49a #f0d070 #5a9ae8 #b88ae8 #4ac8e0 #ccd6e6")
t2("ruby", "Ruby", "#1c0f12", "#f0dcdc", "#ee4a4a #8fc46f #e8b45a #6a95d0 #e0609a #5cbfb0 #d9c4c4")
t2("php", "PHP", "#15152b", "#e4e4f4", "#f06a80 #78d29a #eac870 #7a86e0 #b88ae0 #5cc8dc #cdcde4")
t2("java", "Java", "#14181f", "#e8ecf0", "#f0553a #6fc48a #f2a33a #5a8fc0 #c07aa8 #4fbfc4 #d0d8e0")
t2("kotlin", "Kotlin", "#14101c", "#ece4f4", "#ee4a6a #6fd09a #f5b04a #6a8cf5 #a97aff #4fd0d8 #d4cce4")
t2("swift", "Swift", "#170f0d", "#f4e6e0", "#f0503a #78c88a #f5b84a #5a9ee0 #e06aa0 #4ec4c4 #dccac4")
t2("csharp", "C#", "#17121f", "#e8e0f4", "#ee5a7a #6ccb8a #eac060 #6a8ee8 #c070d8 #4ac4dc #d0c8e0")
t2("elixir", "Elixir", "#150f1f", "#eadff5", "#f0607a #7ad4a0 #f0c878 #7a8cf0 #b070f0 #5acce0 #d4c8e8")
t2("haskell", "Haskell", "#12101e", "#e4def0", "#ee6078 #78cc9a #e8c470 #7090e8 #a06ad8 #58c0d8 #cdc6e0")
t2("lua", "Lua", "#0b1030", "#dfe6f5", "#f06070 #70d890 #e8cc70 #5a78e8 #b080e8 #50c8e8 #ccd4e8")
t2("zig", "Zig", "#1a1408", "#f0e6d0", "#ee5a3a #98c860 #f7a41d #5a9ad0 #d0709a #58c0a8 #d8ccb4")
t2("nodejs", "Node.js", "#0e150f", "#e0efe0", "#f0645a #68c657 #e8cd5a #5aa0e0 #c07ad8 #4cc8b8 #cadcca")
t2("dart", "Dart / Flutter", "#0b1620", "#e0f0fa", "#f06070 #5ee0a0 #f5d060 #3aa0f0 #b080f0 #13b9fd #cce0ee")
t2("julia", "Julia", "#12121a", "#ece8f0", "#e5534b #5ec050 #e8c050 #5a8fe0 #b072d0 #4cc0c8 #d4d0dc")
# ---- cafés ----
t2("espresso", "Espresso", "#140d0a", "#e8d5c0", "#d9634a #8fa05a #e0a850 #6e90a0 #b0728a #6fa890 #c9b8a2")
t2("cappuccino", "Cappuccino", "#2a1f19", "#eddcc8", "#de6f58 #9cae6a #e8b866 #7ea0b0 #bc8095 #7cb89f #d3c1ac")
t2("americano", "Americano", "#1a1411", "#d9cdbc", "#c8604c #8a9a62 #cba35a #6c8898 #a47890 #6a9c8a #bfb2a0")
t2("cortado", "Cortado", "#231a15", "#e6d4bc", "#d86a52 #96a860 #dcae5a #7498a8 #b47c8e #70ac94 #c8b8a0")
t2("cafe_moka", "Café Moka", "#1f1215", "#f0d8d0", "#e05a64 #8aa868 #e0a85a #7a94b0 #c8789c #6cb0a0 #d4bcb8")
t2("caramel_macchiato", "Caramel Macchiato", "#2b1c12", "#f5e1c4", "#e8704a #a0b45a #f0b840 #7a9eb0 #c8809a #78bca0 #dcc8a8")
t2("cold_brew", "Cold Brew", "#0e1314", "#d8e4e0", "#d86a58 #86b080 #d2b068 #6a9cb8 #a880a0 #5cb8b0 #bccac4")
t2("cafe_de_olla", "Café de Olla", "#1e130e", "#ecd5b4", "#d25a3a #8ca350 #e0a030 #6a94a0 #c07080 #62a89a #cdb898")
t2("flat_white", "Flat White", "#24201c", "#efe6d8", "#d9705f #9bb078 #ddb86a #7c9fb8 #b98aa4 #7ab8a8 #d6ccbc")
t2("irish_coffee", "Irish Coffee", "#18140f", "#e4dcc4", "#d4604a #7fb06a #e0a840 #6f94a8 #b07a90 #62b0a0 #cabfa4")
t2("turkish_coffee", "Turkish Coffee", "#1b1210", "#e8d0b8", "#d4553e #98a850 #e6a030 #5e8aa8 #b8607c #58a898 #c9b09a")
t2("affogato", "Affogato", "#1c1814", "#f6eede", "#e0705c #a4b878 #ecc468 #86a8c0 #c490a8 #84c0aa #e4d8c4")
t2("cafe_bombon", "Café Bombón", "#241810", "#f2e0c0", "#e0644a #98ac5c #f2c050 #7098b0 #c07c94 #6ab4a0 #dccaa8")

NAMES = "black red green yellow blue magenta cyan white".split()

def lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def cr(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def render(title, bg, fg, n, b):
    out = [f"# {title}", "", "[colors.primary]", f"background = '{bg}'", f"foreground = '{fg}'", ""]
    for sect, vals in (("normal", n), ("bright", b)):
        out.append(f"[colors.{sect}]")
        for k, v in zip(NAMES, vals):
            out.append(f"{k:<7} = '{v}'")
        out.append("")
    return "\n".join(out)

dirs = sys.argv[1:]
print(f"{'tema':27} {'fg':>5} {'min.color':>9} {'peor':>8} {'br.black':>8}")
for name, (title, bg, fg, n, b) in T.items():
    for d in dirs:
        with open(os.path.join(d, name + ".toml"), "w") as f:
            f.write(render(title, bg, fg, n, b))
    # text-ish colors: red..white normal + bright (exclude black slots, which are bg-ish)
    cols = [(f"n.{NAMES[i]}", n[i]) for i in range(1, 7)] + [(f"b.{NAMES[i]}", b[i]) for i in range(1, 7)]
    worst = min(cols, key=lambda c: cr(c[1], bg))
    print(f"{name:27} {cr(fg,bg):5.1f} {cr(worst[1],bg):9.1f} {worst[0]:>8} {cr(b[0],bg):8.1f}")
