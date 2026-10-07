# alacritty-themes

Colección privada de 138 temas **oscuros / coloridos** para [Alacritty](https://alacritty.org), pensados para leerse bien en terminal. Sin temas claros.

Cada tema es un `.toml` con la paleta completa y todas las tablas opcionales declaradas (`primary`, `normal`, `bright`, `cursor`, `vi_mode_cursor`, `selection`, `search.*`, `footer_bar`, `hints.*`), en lugar de depender de los valores por defecto de Alacritty.

## Uso

Copia `themes/` a `%APPDATA%\alacritty\themes\` (o `~/.config/alacritty/themes/`) e impórtalo desde `alacritty.toml`:

```toml
[general]
import = ["themes/viper.toml"]
```

Con `live_config_reload = true` el cambio se aplica al instante. Para cambiarlos con un selector (fzf, vista previa en vivo) usa `alac-theme` de [`my-alacritty-setup`](https://github.com/sazardev/my-alacritty-setup).

## Temas

**Videojuegos** (paletas originales *inspiradas en*, no son assets oficiales): `cyberpunk_2077`, `arasaka`, `edgerunners`, `viper`, `valorant`, `jett`, `jinx`, `zaun`, `halo`, `cortana`, `pipboy`, `sheikah`, `n7`, `doom_slayer`, `creeper`, `hollow_knight`, `elden_ring`, `tron_legacy`, `hextech`, `overwatch`, `aperture`, `hades_2`

**Verdes y amarillos / mono-ish:** `lemon_lime`, `forest_gold`, `matcha`, `radioactive`, `jungle`, `swamp`, `amber_crt`

**Tipo Gruvbox** (cálidos, apagados, coherentes): `gruvbox_hard_dark`, `gruvbox_soft`, `gruvbox_plum`

**Cálidos apagados:** `coffee`, `autumn`, `desert_dusk`, `terracotta`, `sunset_ember`, `nicotine`, `sage`

**Retrowave / retrofuturistas:** `outrun`, `retrowave_sunset`, `miami_vice`, `vaporwave`, `laserwave`, `retro_70s`, `space_age`, `atomic_age`, `blade_runner`, `arcade_cabinet`

**Colorful:** `candy`, `prism`, `tropical`, `aurora`, `jewel`, `festival`, `ocean_reef`, `spring_bloom`

Estos 28 (y los de lenguajes y cafés) se definen solo con el matiz base de cada color (`t2()` en `tools/gen-themes.py`): el negro, los brillantes y el bright black se derivan con reglas fijas y cualquier color que no llegue a 4.3:1 contra el fondo se aclara automáticamente. Todos quedan con texto ≥ 4.3:1 y bright black ≥ 3.3:1.

**Lenguajes de programación** (basados en el color de marca de cada uno): `python`, `rust`, `golang`, `javascript`, `typescript`, `ruby`, `php`, `java`, `kotlin`, `swift`, `csharp`, `elixir`, `haskell`, `lua`, `zig`, `nodejs`, `dart`, `julia`

**Cafés:** `espresso`, `cappuccino`, `americano`, `cortado`, `cafe_moka`, `caramel_macchiato`, `cold_brew`, `cafe_de_olla`, `flat_white`, `irish_coffee`, `turkish_coffee`, `affogato`, `cafe_bombon`

**Escritos a mano** desde la paleta publicada de cada proyecto (fieles pero no oficiales): `monokai`, `tomorrow_night`, `tomorrow_night_eighties`, `nightfox`, `carbonfox`, `gruvbox_material_dark`, `palenight`, `horizon_dark`, `tokyo_night_moon`, `oxocarbon`, `cyberdream`, `iceberg`, `github_dark_dimmed`, `github_dark_high_contrast`, `flexoki_dark`, `nightfly`, `mellow`, `poimandres`, `sonokai`, `snazzy`, `vscode_dark_plus`, `ubuntu`, `moonfly`, `oceanic_next`, `challenger_deep`, `everblush`

**Tomados de [alacritty/alacritty-theme](https://github.com/alacritty/alacritty-theme)** (más `osaka_jade`, derivado de Omarchy): `ayu_dark`, `ayu_mirage`, `catppuccin_frappe`, `catppuccin_macchiato`, `catppuccin_mocha`, `doom_one`, `dracula`, `everforest_dark`, `github_dark_default`, `gruvbox_dark`, `kanagawa_dragon`, `kanagawa_wave`, `miasma`, `monokai_pro`, `night_owl`, `nord`, `one_dark`, `osaka_jade`, `rose_pine`, `rose_pine_moon`, `solarized_dark`, `synthwave_84`, `tokyo_night`, `tokyo_night_storm`

## Accesibilidad

En los temas escritos a mano y los de juegos, el foreground y cada color ANSI de texto (rojo–cian, normal y bright) se revisaron contra el fondo con contraste WCAG (casi todos ≥ 4.5:1, el mínimo ≥ 3.6:1), y el `bright black` (comentarios, sugerencias) queda en ≈ 3:1 o más. Algunos slots se ajustaron respecto al valor original para lograrlo (`ubuntu`, `vscode_dark_plus`, `nightfox` y el bright black de varios). `pipboy` y `amber_crt` son casi monocromáticos a propósito. El texto de la selección y de la búsqueda cumple ≥ 4.5:1.

## herdr

Con `theme.name = "terminal"`, [herdr](https://herdr.dev) toma la paleta ANSI de Alacritty. El borde de los panes inactivos usa el token `overlay0`, que por defecto cae en ANSI *white* (claro en casi todos los temas). Se corrige en `~/.config/herdr/config.toml`:

```toml
[theme.custom]
overlay0 = "darkgray"   # = ANSI bright black: atenuado y sigue el tema activo
```

El pane activo usa `accent` (= ANSI blue). `tools/herdr-border-probe.py <tema> [XDG_CONFIG_HOME]` abre una sesión aislada de herdr en un pty, le responde las consultas de paleta con ese tema y muestra qué colores usan los bordes.

## Herramientas (`tools/`)

| Script | Qué hace |
|---|---|
| `gen-themes.py <dir>...` | Regenera los temas escritos a mano (los de juegos, verdes y los 26 extra y las familias nuevas) y reporta contraste. |
| `enrich-themes.py <dir>...` | Agrega a cualquier tema las tablas que le falten, derivadas de su paleta. Idempotente. **Correr después de `gen-themes.py`.** |
| `herdr-border-probe.py` | Diagnóstico de colores de borde en herdr (ver arriba). |

```sh
python3 -I tools/gen-themes.py themes && python3 -I tools/enrich-themes.py themes
```

`herdr-border-probe.py` asume la ruta de temas de Windows (`/mnt/c/Users/Omar/AppData/Roaming/alacritty/themes`); ajústala si lo usas en otra máquina.
