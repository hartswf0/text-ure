# TEXT-URE: The Medium as Operator

A research project exploring spatial-semantic grids, operative ekphrasis, and text-as-architecture through interactive raycaster environments.

## Quick Start

```bash
# Start local server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000/text-ure-nexus.html
```

## Project Structure

### Core Applications

| File | Description |
|------|-------------|
| `text-ure-nexus.html` | **Base camp launcher** — Matrix background, color themes, quick launch |
| `text-ure-03.html` | **Latest stable (v16.6)** — Full features, POML injection, custom text |
| `text-ure-cascade.html` | **Infinite stream** — Load books/chapters, animated cycling walls |
| `text-ure-02.html` | v16 Triad — Vision generation, depth maps |
| `text-ure-01.html` | v12 Polished — Minimap, TTS, haptics |
| `text-ure-00.html` | v11 Foundation — Core raycaster |

### Tools

| File | Description |
|------|-------------|
| `poml-scroll.html` | **Mobile-first POML IDE** — Horizontal columns, chain builder, notes |
| `poml-ide.html` | Original POML development environment |
| `poml.html` | Compact TUI-style POML tool |
| `index.html` | Research hub documentation |
| `ek-ide.html` | Paper outline comparison tool |

### Data

| File | Description |
|------|-------------|
| `data.json` | Source conversation with POML blocks |
| `Prompt Codex_ Medium as Operator.md` | Theoretical framework document |

## Controls

### Desktop
- **WASD** or **Arrow keys** — Move & rotate
- **A/D** — Turn left/right
- **Mouse click** — Enable mouse look (v16.6)
- **ESC** — Exit mouse look
- **H** — Toggle cinematic mode
- **Space** — Show scanner

### Mobile
- **Left pad** — Move forward/back
- **Right pad** — Turn left/right
- **≡ button** — Open config

## Theoretical Framework

Based on four media theorists:

1. **James Carey** (Ritual) — Communication as shared ceremony
2. **Friedrich Kittler** (Inscription) — Media as material discourse networks
3. **Guillaume Apollinaire** (Calligram) — Spatial typography, visual poetry
4. **Hannes Bajohr** (Operative Ekphrasis) — Text that causally produces images

## POML (Prompt-Oriented Meta-Language)

XML-like notation for AI prompt blocks:

```xml
<poml type="ritual" theorist="carey">
  <zone function="PRODUCE">
    <text>The grid is a world, not a page.</text>
  </zone>
</poml>
```

## Features

### text-ure-nexus
- Matrix code background
- Color themes: Green, Amber, Cyan, Rose
- Quick text launch
- File loading (auto-routes large files to Cascade)

### text-ure-cascade
- Load entire books/chapters
- Animated cycling wall text
- Speed controls: SLOW / MED / FAST
- Organic rain effect

### poml-scroll
- Horizontal scroll columns
- Context menu (right-click / long-press)
- Prompt chain builder
- Notes system
- JSON export
- Theme switching

## Color Themes

All tools support multiple color modes:
- **Green** (default) — Matrix terminal
- **Amber** — Retro warm
- **Cyan** — Cool digital
- **Rose** — Soft pink

Themes persist via localStorage.

## External Links

- [Gemini Session #1](https://g.co/gemini/share/13cd48bf4958)
- [Gemini Session #2](https://g.co/gemini/share/d27cfdc1d04b)

## License

Research project — open for academic use.
