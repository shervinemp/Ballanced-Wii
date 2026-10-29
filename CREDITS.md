# Credits and thanks

This port builds on the work of the Ballance community and the upstream
Ballanced project. The full licence record is in `THIRD_PARTY_NOTICES.md`.

## The original game

- **Ballance** — the original game and its assets, characters, audio and
  trademarks belong to their respective rights holders. This project does not
  include the game data; you need your own copy.

## Upstream reimplementation

- **Ballanced** by **doyaGu** and contributors —
  <https://github.com/doyaGu/Ballanced>
  - The source-level Ballance runtime reimplementation: player, engine
    libraries, building blocks, plugins and managers. The root project is
    MIT; the engine submodules are MIT or Apache-2.0 (see each submodule).
- Upstream component projects, all linked as Git submodules:
  - [BallancePlayer](https://github.com/doyaGu/BallancePlayer)
  - [CK2](https://github.com/doyaGu/CK2)
  - [VxMath](https://github.com/doyaGu/VxMath)
  - [CKRenderEngine](https://github.com/doyaGu/CKRenderEngine)
  - [CKBuildingBlocks](https://github.com/doyaGu/CKBuildingBlocks)
  - [CKPlugins](https://github.com/doyaGu/CKPlugins)
  - [CKParameterOperations](https://github.com/doyaGu/CKParameterOperations)
  - [SdlInputManager](https://github.com/doyaGu/SdlInputManager)
  - [SdlSoundManager](https://github.com/doyaGu/SdlSoundManager)

## Third-party libraries

- **qhull** — <http://www.qhull.org> — Qhull licence; see
  `Source/BuildingBlocks/3DTrans/qhull/COPYING.txt`.
- **simde** — <https://github.com/simd-everywhere/simde> — MIT; see
  `Source/VxMath/deps/simde/COPYING`.
- **stb** — <https://github.com/nothings/stb> — public domain / MIT; see
  `Source/VxMath/deps/stb/LICENSE`.
- **miniz** — <https://github.com/richgel999/miniz> — MIT; see
  `Source/CK2/deps/miniz/LICENSE`.
- **Roboto** — Apache License 2.0; see
  `Source/BuildingBlocks/Interface/tests/fonts/LICENSE`.
- **SDL3** — zlib licence; used by the upstream SDL runtime, not by this Wii
  build. See <https://github.com/libsdl-org/SDL>.
- **devkitPro / libogc / libfat / AESND / WiiUse / BTE** — the Wii toolchain
  and runtime. Their licences are their own; see the devkitPro packages.

## Testing and references

- **Dolphin** — <https://github.com/dolphin-emu/dolphin> — used for testing
  and for the on-console test workflow. GPL-2.0-or-later upstream; not linked
  into the Wii DOL.

## This port

- **Shervin Naseri (`sherv`)** and contributors — the Wii platform layer, GX
  rasterizer, Wii input and audio managers, build integration, tests and
  documentation.

If a source or contributor is missing, please open an issue. The goal is to
credit the work accurately and correct any licensing mistake promptly.
