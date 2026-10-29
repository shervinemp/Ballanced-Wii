# Contributing

Thanks for helping. The Wii port is still experimental, so small, measured
changes and test reports are useful.

## Licence of contributions

By submitting a change, you agree that it may be distributed under the
project's licence:

- The original port code and upstream Ballanced root are **MIT**.
- The engine submodules are MIT or **Apache-2.0**; keep their notices and
  licence files intact.
- Third-party components keep their own licences (see
  `THIRD_PARTY_NOTICES.md`).
- The Homebrew Channel icon and tutorial text are Ballance-derived and are not
  MIT-licensed; see `NOTICE`.

If you adapt third-party code, say so in the commit message and add the
attribution to `THIRD_PARTY_NOTICES.md` and `CREDITS.md`.

## Never commit game data

Do not add:

- `base.cmo`, `Database.tdb`, `3D Entities/`, `Sounds/`, `Sounds_low/`,
  `Textures/`, `Text/`, `Fonts/`, `Wii/`, or `Player.ini`/`Player.log`
- `build/`, `apps/`, `assets/`, or a staged SD-card layout
- `.dol`, `.elf`, `.map`, archives or other built binaries
- memory-card/save data or screenshots of game content

Run this before every commit or push:

```sh
python -I tools/check_repo.py
```

CI runs the same check.

## Building and testing

Follow `README.md`:

```sh
git clone --recurse-submodules https://github.com/shervinemp/Ballanced-Wii.git
cd Ballanced-Wii
cmake -S . -B build/wii -G Ninja \
      -DCMAKE_TOOLCHAIN_FILE=cmake/wii.cmake \
      -DCMAKE_BUILD_TYPE=Release
cmake --build build/wii --target WiiPlayer WiiPlayerTests
```

The on-console test DOL and the full build matrix are described in
`BUILD.md`. If your change affects a submodule, put the change in
`Source/WiiPatches/` rather than editing the submodule in place.

## Maintainer publishing

- Private development: **Ballanced-private**
- Public source snapshot: **Ballanced-Wii**
- The older public fork **Ballanced** remains the upstream-facing fork.
- The private tree may contain a larger, uncommitted WIP; only the committed
  snapshot is published.

The public repo is a single source snapshot, not the private development
history. Builds, game data and `build/` are never published.

Before publishing, run `python -I tools/check_repo.py` and inspect
`git status`. Do not publish a tree containing game files, `build/`, or a
built binary.
