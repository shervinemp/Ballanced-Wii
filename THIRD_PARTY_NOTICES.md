# Third-party notices

The original port code in this repository is **MIT** (see `LICENSE`). The
upstream Ballanced project is a source-level reimplementation of the Ballance
runtime; its root project is MIT, and its engine components carry their own
licences, mostly MIT or Apache-2.0. Each Git submodule keeps its own `LICENSE`
file.

No full Ballance game data is included. The Homebrew Channel icon and tutorial
overlay are Ballance-derived; see `NOTICE`.

## Upstream Ballanced components

| Component | Location | Licence |
| --- | --- | --- |
| Ballanced (root project) | top-level | MIT — `LICENSE` |
| BallancePlayer | `Source/Player/` | MIT — `Source/Player/LICENSE` |
| CK2 | `Source/CK2/` | Apache-2.0 — `Source/CK2/LICENSE` |
| VxMath | `Source/VxMath/` | Apache-2.0 — `Source/VxMath/LICENSE` |
| CKRenderEngine | `Source/RenderEngine/` | Apache-2.0 — `Source/RenderEngine/LICENSE` |
| CKBuildingBlocks | `Source/BuildingBlocks/` | Apache-2.0 — `Source/BuildingBlocks/LICENSE` |
| CKPlugins | `Source/Plugins/` | Apache-2.0 — `Source/Plugins/LICENSE` |
| CKParameterOperations | `Source/Managers/ParameterOperations/` | Apache-2.0 — `Source/Managers/ParameterOperations/LICENSE` |
| SDL input/sound managers | `Source/Managers/SdlInputManager/`, `SdlSoundManager/` | Upstream SDL components; no separate licence file was found in the submodule at this snapshot. They are not used by the Wii build, which uses `WiiInputManager`/`WiiSoundManager`. |

## Third-party libraries

- **qhull** — <http://www.qhull.org> — Qhull licence; see
  `Source/BuildingBlocks/3DTrans/qhull/COPYING.txt`.
- **simde** — <https://github.com/simd-everywhere/simde> — MIT; see
  `Source/VxMath/deps/simde/COPYING`.
- **stb** — <https://github.com/nothings/stb> — public domain / MIT; see
  `Source/VxMath/deps/stb/LICENSE`.
- **miniz** — <https://github.com/richgel999/miniz> — MIT; see
  `Source/CK2/deps/miniz/LICENSE`.
- **Roboto** — Apache-2.0; see
  `Source/BuildingBlocks/Interface/tests/fonts/LICENSE`.
- **SDL3** — zlib licence; used by the upstream SDL runtime, not by the Wii
  build. See <https://github.com/libsdl-org/SDL>.
- **devkitPro / libogc / libfat / AESND / WiiUse / BTE** — the Wii toolchain
  and runtime; their licences are their own; see the devkitPro packages.
- **Dolphin** — <https://github.com/dolphin-emu/dolphin> — testing/emulation
  reference. GPL-2.0-or-later upstream; not linked into the Wii DOL.

## Private Wii work not in this snapshot

The private development tree adds the optional **libntfs-wii** submodule
(`rhyskoedijk/libntfs-wii`, GPL-2.0-or-later) and NTFS paths. It is not part of
this public snapshot. If you combine libntfs with the Apache-2.0 engine
components in a distributed binary, the compatible combined licence is
GPL-3.0-or-later, not GPL-2.0-only; keep all notices and provide the
corresponding source. This is a licensing summary, not legal advice.

## Game ownership

*Ballance* and its related artwork, text, audio, characters and trademarks
belong to their respective owners. The official icon and tutorial overlay are
included only as the port's UI files under `NOTICE`; they are not MIT-licensed.
Users must supply their own legally obtained copy of the game.

## Reporting a licensing problem

If you believe a file in this repository infringes your rights, please open an
issue or contact the maintainer. The file will be removed or the licence
corrected promptly.
