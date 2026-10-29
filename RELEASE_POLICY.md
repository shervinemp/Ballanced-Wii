# Release policy

This repository is **source-only**. There are no binary releases, and there
should not be any.

Do **not** publish or attach any of these to a release, GitHub Actions
artifact, package, website, or mirror:

- the original game files: `base.cmo`, `Database.tdb`, `3D Entities/`,
  `Sounds/`, `Sounds_low/`, `Textures/`, `Text/`, `Fonts/`, `Wii/`
- `build/`, `apps/`, `assets/`, or any staged SD-card layout
- `*.dol`, `*.elf`, `*.map`, or other built binaries
- archives, disc images, or packaged releases
- memory-card/save data or screenshots of game content

## Why

The port is source code; the game data belongs to the original Ballance rights
holders. A built DOL is also a compiled artefact, and a release would need the
corresponding source and all third-party notices. Keep builds local.

## If you build it

Build and run it locally from your own legally owned copy. Share source changes
and instructions, not the binary or game data.

## Game-derived UI files

`Source/WiiPlayer/hbc/icon.png` and
`Source/WiiPlayer/data/Text/Tutorial*.txt` are Ballance-derived artwork/text,
included only as the port's UI overlay. They are not MIT-licensed; see
`NOTICE`. Do not present them as original project artwork.

## Takedown requests

If a copyright claim arrives, evaluate it with counsel before responding. A
counter-notice is an option for a mistaken claim, but it is not a substitute
for legal advice.

## Non-commercial

This is an unofficial, non-commercial fan project. Do not sell it, put it
behind a paywall, add monetised ads, or present it as an official Ballance
product.

This policy is not legal advice.
