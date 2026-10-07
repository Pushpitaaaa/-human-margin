# The Human Margin

A choice-based Moon outpost game for NASA Space Apps 2026 (challenge: *Build a Junior Astronaut Mission Trainer*).

You run a small lunar base for ten days. Each day you plan with a limited budget of crew hours and power across four systems (air, power, shielding, food), then live with the consequences. A story about the Commander's eight-year-old brother Mimi is the reason every decision matters. There are twelve endings.

## Play it

Open `index.html` in a modern browser (Chrome, Edge or Firefox). No install, no server, no internet needed. Sound on is best.

If this repository has GitHub Pages turned on, it plays at the repository's Pages link.

## What it teaches

Real mission planning is trade-offs: power, crew time, air, radiation shielding and food all draw on the same limited margin. Each day ends with a short "what a real planner weighs" note, and Mimi's questions (why not grow more food? why not live underground?) are answered by the player, with corrections for wrong answers.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The whole game, in one file |
| `art/` | Drop in finished images and they replace the drawn placeholders (see `art/README.txt`) |
| `audio/` | Drop in sound files and they replace the built-in sounds (see `audio/README.txt`) |
| `embed-art.py` | Packs `art/` and `audio/` into a single HTML file for sharing |
| `DISCLOSURE.md` | Data sources and AI tools used (draft, to be finished before submission) |

## Status

Playable from the prologue to all twelve endings. Not finished:

- **Real NASA data is not wired in yet.** The Day 8 solar flare, the sun angles and the life-support and radiation figures are placeholders. The game shows a "placeholder" label on the Day 8 card until a real record is added.
- Art and sound are drawn or synthesized in code.
- Mimi's single voice message (Day 9) is text until a recording is added as `audio/mimi-voice.mp3`.

## Privacy

Age, height and weight entered at the start stay in the browser's memory while you play. Nothing is sent anywhere. The only thing saved is which endings you have found (browser local storage).

## For developers

Adding `?debug` to the URL exposes the game state as `window.__hm` for testing.
