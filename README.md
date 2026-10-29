# Ballance for Wii

A source-level reimplementation of the **Ballance** runtime, ported to the
Nintendo Wii. The game logic, engine libraries, building blocks and plugins
come from the [Ballanced](https://github.com/doyaGu/Ballanced) project; the Wii
backend replaces SDL3 with libogc, GX rendering, Wii input and Wii audio.

This is an unofficial fan project. It is not affiliated with or endorsed by the
original Ballance developers or publishers.

## What you need

- A legally owned copy of **Ballance** — the original game files are not
  included.
- devkitPro with the `wii-dev` package group (devkitPPC, libogc, libfat, AESND,
  WiiUse/BTE).
- CMake 3.21+ and Ninja.
- The repository's submodules.

Clone with submodules:

```sh
git clone --recurse-submodules https://github.com/shervinemp/Ballanced-Wii.git
cd Ballanced-Wii
```

If you already cloned without them:

```sh
git submodule update --init --recursive
```

## Build

From a devkitPro shell (the devkitPro MSYS2 shell on Windows):

```sh
cmake -S . -B build/wii -G Ninja \
      -DCMAKE_TOOLCHAIN_FILE=cmake/wii.cmake \
      -DCMAKE_BUILD_TYPE=Release
cmake --build build/wii --target WiiPlayer
```

The game is `build/wii/Source/WiiPlayer/boot.dol`. To build the on-console test
DOL as well, add `WiiPlayerTests` to the `--target` list.

The full build matrix, toolchain notes, tests, profiling scripts and debugging
details are in [BUILD.md](BUILD.md).

## Install on the Wii

```sh
cmake --install build/wii --prefix <SD-card-root>
```

This creates `apps/ballance/` with `boot.dol`, `meta.xml`, `icon.png`, the
fallback font and the Wii tutorial overlay. Copy the game files from your own
Ballance installation into that folder:

```text
apps/ballance/
  boot.dol
  meta.xml
  icon.png
  base.cmo
  Database.tdb
  3D Entities/
  Sounds/
  Sounds_low/
  Textures/
  Text/
  Fonts/
  Wii/Text/       tutorial text for the Wii controls
  Wii/Cache/      collision surfaces written by the game
```

Start it from the Homebrew Channel. `Player.ini` and `Player.log` are written
next to `boot.dol`; the game's own settings are kept there too.

The public source snapshot reads FAT SD/USB storage. NTFS support is part of
the private development work and is not included in this snapshot.

## Controls

| Action | Wii Remote sideways | Wii Remote + Nunchuk | Classic / GameCube |
|---|---|---|---|
| Roll the ball | Tilt | Control Stick | Stick or D-Pad |
| Turn the view | D-Pad left/right | D-Pad left/right | Hold Y/L/ZL and press left/right |
| Overhead camera | D-Pad up or 2 | D-Pad up or C | X, R, ZR |
| Set the current hold as level | D-Pad down | — | — |
| Confirm | A | A | A |
| Back / pause | + | + or B | B or + / B or Start |
| Skip the tutorial | - | - | - |

Point the Wii Remote at the screen and press A where the game expects a mouse;
A also confirms menus. The on-screen keyboard appears when the game asks for a
name.

## Licensing and game data

The original port code is **MIT**. The upstream Ballanced root is MIT; its
engine submodules are MIT or **Apache-2.0** (see each submodule's `LICENSE`).
See [LICENSE](LICENSE), [CREDITS.md](CREDITS.md) and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

`Source/WiiPlayer/hbc/icon.png` and
`Source/WiiPlayer/data/Text/Tutorial*.txt` are Ballance-derived artwork and
text. They are **not** MIT-licensed and remain the property of their original
rights holders; see [NOTICE](NOTICE). The rest of the game's assets are not in
this repository.

This is a source-only repository: no game data, `build/`, DOL/ELF files,
packages or other binaries are included. See [RELEASE_POLICY.md](RELEASE_POLICY.md).

*Ballance* is a trademark of its respective owners. This is an unofficial,
non-commercial fan project.
