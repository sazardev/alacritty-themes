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
