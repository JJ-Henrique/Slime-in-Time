
```
game
├─ assets
│  ├─ images
│  │  ├─ background
│  │  │  └─ background.png
│  │  ├─ enemy
│  │  │  ├─ enemy_1.png
│  │  │  ├─ enemy_2.png
│  │  │  └─ enemy_3.png
│  │  └─ player
│  │     ├─ player_1.png
│  │     ├─ player_2.png
│  │     └─ player_3.png
│  └─ sounds
│     └─ music.mp3
├─ enemy.py
├─ game.py
├─ main.py
├─ player.py
├─ settings.py
├─ venv
│  ├─ Include
│  │  └─ site
│  │     └─ python3.11
│  │        └─ pygame
│  │           ├─ camera.h
│  │           ├─ font.h
│  │           ├─ freetype.h
│  │           ├─ include
│  │           │  ├─ bitmask.h
│  │           │  ├─ pgcompat.h
│  │           │  ├─ pgimport.h
│  │           │  ├─ pgplatform.h
│  │           │  ├─ pygame.h
│  │           │  ├─ pygame_bufferproxy.h
│  │           │  ├─ pygame_font.h
│  │           │  ├─ pygame_freetype.h
│  │           │  ├─ pygame_mask.h
│  │           │  ├─ pygame_mixer.h
│  │           │  ├─ sse2neon.h
│  │           │  └─ _pygame.h
│  │           ├─ mask.h
│  │           ├─ mixer.h
│  │           ├─ palette.h
│  │           ├─ pgarrinter.h
│  │           ├─ pgbufferproxy.h
│  │           ├─ pgcompat.h
│  │           ├─ pgopengl.h
│  │           ├─ pgplatform.h
│  │           ├─ pygame.h
│  │           ├─ scrap.h
│  │           ├─ simd_blitters.h
│  │           ├─ surface.h
│  │           ├─ _blit_info.h
│  │           ├─ _camera.h
│  │           ├─ _pygame.h
│  │           └─ _surface.h
│  ├─ Lib
│  │  └─ site-packages
│  │     ├─ 30fcd23745efe32ce681__mypyc.cp311-win_amd64.pyd
│  │     ├─ black
│  │     │  ├─ brackets.cp311-win_amd64.pyd
│  │     │  ├─ brackets.py
│  │     │  ├─ cache.cp311-win_amd64.pyd
│  │     │  ├─ cache.py
│  │     │  ├─ comments.cp311-win_amd64.pyd
│  │     │  ├─ comments.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ const.cp311-win_amd64.pyd
│  │     │  ├─ const.py
│  │     │  ├─ debug.py
│  │     │  ├─ files.py
│  │     │  ├─ handle_ipynb_magics.cp311-win_amd64.pyd
│  │     │  ├─ handle_ipynb_magics.py
│  │     │  ├─ linegen.cp311-win_amd64.pyd
│  │     │  ├─ linegen.py
│  │     │  ├─ lines.cp311-win_amd64.pyd
│  │     │  ├─ lines.py
│  │     │  ├─ mode.cp311-win_amd64.pyd
│  │     │  ├─ mode.py
│  │     │  ├─ nodes.cp311-win_amd64.pyd
│  │     │  ├─ nodes.py
│  │     │  ├─ numerics.cp311-win_amd64.pyd
│  │     │  ├─ numerics.py
│  │     │  ├─ output.py
│  │     │  ├─ parsing.cp311-win_amd64.pyd
│  │     │  ├─ parsing.py
│  │     │  ├─ py.typed
│  │     │  ├─ ranges.cp311-win_amd64.pyd
│  │     │  ├─ ranges.py
│  │     │  ├─ report.py
│  │     │  ├─ resources
│  │     │  │  ├─ black.schema.json
│  │     │  │  ├─ __init__.cp311-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ rusty.cp311-win_amd64.pyd
│  │     │  ├─ rusty.py
│  │     │  ├─ schema.cp311-win_amd64.pyd
│  │     │  ├─ schema.py
│  │     │  ├─ strings.cp311-win_amd64.pyd
│  │     │  ├─ strings.py
│  │     │  ├─ trans.cp311-win_amd64.pyd
│  │     │  ├─ trans.py
│  │     │  ├─ _width_table.cp311-win_amd64.pyd
│  │     │  ├─ _width_table.py
│  │     │  ├─ __init__.cp311-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ brackets.cpython-311.pyc
│  │     │     ├─ cache.cpython-311.pyc
│  │     │     ├─ comments.cpython-311.pyc
│  │     │     ├─ concurrency.cpython-311.pyc
│  │     │     ├─ const.cpython-311.pyc
│  │     │     ├─ debug.cpython-311.pyc
│  │     │     ├─ files.cpython-311.pyc
│  │     │     ├─ handle_ipynb_magics.cpython-311.pyc
│  │     │     ├─ linegen.cpython-311.pyc
│  │     │     ├─ lines.cpython-311.pyc
│  │     │     ├─ mode.cpython-311.pyc
│  │     │     ├─ nodes.cpython-311.pyc
│  │     │     ├─ numerics.cpython-311.pyc
│  │     │     ├─ output.cpython-311.pyc
│  │     │     ├─ parsing.cpython-311.pyc
│  │     │     ├─ ranges.cpython-311.pyc
│  │     │     ├─ report.cpython-311.pyc
│  │     │     ├─ rusty.cpython-311.pyc
│  │     │     ├─ schema.cpython-311.pyc
│  │     │     ├─ strings.cpython-311.pyc
│  │     │     ├─ trans.cpython-311.pyc
│  │     │     ├─ _width_table.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ black-26.5.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ blackd
│  │     │  ├─ client.py
│  │     │  ├─ middlewares.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ client.cpython-311.pyc
│  │     │     ├─ middlewares.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ blib2to3
│  │     │  ├─ Grammar.txt
│  │     │  ├─ LICENSE
│  │     │  ├─ PatternGrammar.txt
│  │     │  ├─ pgen2
│  │     │  │  ├─ conv.cp311-win_amd64.pyd
│  │     │  │  ├─ conv.py
│  │     │  │  ├─ driver.cp311-win_amd64.pyd
│  │     │  │  ├─ driver.py
│  │     │  │  ├─ grammar.cp311-win_amd64.pyd
│  │     │  │  ├─ grammar.py
│  │     │  │  ├─ literals.cp311-win_amd64.pyd
│  │     │  │  ├─ literals.py
│  │     │  │  ├─ parse.cp311-win_amd64.pyd
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ pgen.cp311-win_amd64.pyd
│  │     │  │  ├─ pgen.py
│  │     │  │  ├─ token.cp311-win_amd64.pyd
│  │     │  │  ├─ token.py
│  │     │  │  ├─ tokenize.cp311-win_amd64.pyd
│  │     │  │  ├─ tokenize.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conv.cpython-311.pyc
│  │     │  │     ├─ driver.cpython-311.pyc
│  │     │  │     ├─ grammar.cpython-311.pyc
│  │     │  │     ├─ literals.cpython-311.pyc
│  │     │  │     ├─ parse.cpython-311.pyc
│  │     │  │     ├─ pgen.cpython-311.pyc
│  │     │  │     ├─ token.cpython-311.pyc
│  │     │  │     ├─ tokenize.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ pygram.cp311-win_amd64.pyd
│  │     │  ├─ pygram.py
│  │     │  ├─ pytree.cp311-win_amd64.pyd
│  │     │  ├─ pytree.py
│  │     │  ├─ README
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ pygram.cpython-311.pyc
│  │     │     ├─ pytree.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ click
│  │     │  ├─ core.py
│  │     │  ├─ decorators.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formatting.py
│  │     │  ├─ globals.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ shell_completion.py
│  │     │  ├─ termui.py
│  │     │  ├─ testing.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _termui_impl.py
│  │     │  ├─ _textwrap.py
│  │     │  ├─ _utils.py
│  │     │  ├─ _winconsole.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-311.pyc
│  │     │     ├─ decorators.cpython-311.pyc
│  │     │     ├─ exceptions.cpython-311.pyc
│  │     │     ├─ formatting.cpython-311.pyc
│  │     │     ├─ globals.cpython-311.pyc
│  │     │     ├─ parser.cpython-311.pyc
│  │     │     ├─ shell_completion.cpython-311.pyc
│  │     │     ├─ termui.cpython-311.pyc
│  │     │     ├─ testing.cpython-311.pyc
│  │     │     ├─ types.cpython-311.pyc
│  │     │     ├─ utils.cpython-311.pyc
│  │     │     ├─ _compat.cpython-311.pyc
│  │     │     ├─ _termui_impl.cpython-311.pyc
│  │     │     ├─ _textwrap.cpython-311.pyc
│  │     │     ├─ _utils.cpython-311.pyc
│  │     │     ├─ _winconsole.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ click-8.4.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ colorama
│  │     │  ├─ ansi.py
│  │     │  ├─ ansitowin32.py
│  │     │  ├─ initialise.py
│  │     │  ├─ tests
│  │     │  │  ├─ ansitowin32_test.py
│  │     │  │  ├─ ansi_test.py
│  │     │  │  ├─ initialise_test.py
│  │     │  │  ├─ isatty_test.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ winterm_test.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ansitowin32_test.cpython-311.pyc
│  │     │  │     ├─ ansi_test.cpython-311.pyc
│  │     │  │     ├─ initialise_test.cpython-311.pyc
│  │     │  │     ├─ isatty_test.cpython-311.pyc
│  │     │  │     ├─ utils.cpython-311.pyc
│  │     │  │     ├─ winterm_test.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ win32.py
│  │     │  ├─ winterm.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ ansi.cpython-311.pyc
│  │     │     ├─ ansitowin32.cpython-311.pyc
│  │     │     ├─ initialise.cpython-311.pyc
│  │     │     ├─ win32.cpython-311.pyc
│  │     │     ├─ winterm.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ colorama-0.4.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ distutils-precedence.pth
│  │     ├─ fd7dcdb10166ebd4db98__mypyc.cp311-win_amd64.pyd
│  │     ├─ mypy_extensions-1.1.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ mypy_extensions.py
│  │     ├─ packaging
│  │     │  ├─ dependency_groups.py
│  │     │  ├─ direct_url.py
│  │     │  ├─ errors.py
│  │     │  ├─ licenses
│  │     │  │  ├─ _spdx.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _spdx.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ markers.py
│  │     │  ├─ metadata.py
│  │     │  ├─ py.typed
│  │     │  ├─ pylock.py
│  │     │  ├─ requirements.py
│  │     │  ├─ specifiers.py
│  │     │  ├─ tags.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ _elffile.py
│  │     │  ├─ _manylinux.py
│  │     │  ├─ _musllinux.py
│  │     │  ├─ _parser.py
│  │     │  ├─ _structures.py
│  │     │  ├─ _tokenizer.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ dependency_groups.cpython-311.pyc
│  │     │     ├─ direct_url.cpython-311.pyc
│  │     │     ├─ errors.cpython-311.pyc
│  │     │     ├─ markers.cpython-311.pyc
│  │     │     ├─ metadata.cpython-311.pyc
│  │     │     ├─ pylock.cpython-311.pyc
│  │     │     ├─ requirements.cpython-311.pyc
│  │     │     ├─ specifiers.cpython-311.pyc
│  │     │     ├─ tags.cpython-311.pyc
│  │     │     ├─ utils.cpython-311.pyc
│  │     │     ├─ version.cpython-311.pyc
│  │     │     ├─ _elffile.cpython-311.pyc
│  │     │     ├─ _manylinux.cpython-311.pyc
│  │     │     ├─ _musllinux.cpython-311.pyc
│  │     │     ├─ _parser.cpython-311.pyc
│  │     │     ├─ _structures.cpython-311.pyc
│  │     │     ├─ _tokenizer.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ packaging-26.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ LICENSE.APACHE
│  │     │  │  └─ LICENSE.BSD
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pathspec
│  │     │  ├─ backend.py
│  │     │  ├─ gitignore.py
│  │     │  ├─ pathspec.py
│  │     │  ├─ pattern.py
│  │     │  ├─ patterns
│  │     │  │  ├─ gitignore
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ basic.py
│  │     │  │  │  ├─ spec.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ basic.cpython-311.pyc
│  │     │  │  │     ├─ spec.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ gitwildmatch.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ gitwildmatch.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ util.py
│  │     │  ├─ _backends
│  │     │  │  ├─ agg.py
│  │     │  │  ├─ hyperscan
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ gitignore.py
│  │     │  │  │  ├─ pathspec.py
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ gitignore.cpython-311.pyc
│  │     │  │  │     ├─ pathspec.cpython-311.pyc
│  │     │  │  │     ├─ _base.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ re2
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ gitignore.py
│  │     │  │  │  ├─ pathspec.py
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ gitignore.cpython-311.pyc
│  │     │  │  │     ├─ pathspec.cpython-311.pyc
│  │     │  │  │     ├─ _base.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ simple
│  │     │  │  │  ├─ gitignore.py
│  │     │  │  │  ├─ pathspec.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ gitignore.cpython-311.pyc
│  │     │  │  │     ├─ pathspec.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ agg.cpython-311.pyc
│  │     │  │     ├─ _utils.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _meta.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ backend.cpython-311.pyc
│  │     │     ├─ gitignore.cpython-311.pyc
│  │     │     ├─ pathspec.cpython-311.pyc
│  │     │     ├─ pattern.cpython-311.pyc
│  │     │     ├─ util.cpython-311.pyc
│  │     │     ├─ _meta.cpython-311.pyc
│  │     │     ├─ _typing.cpython-311.pyc
│  │     │     ├─ _version.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ pathspec-1.1.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pip
│  │     │  ├─ py.typed
│  │     │  ├─ _internal
│  │     │  │  ├─ build_env.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ cli
│  │     │  │  │  ├─ autocompletion.py
│  │     │  │  │  ├─ base_command.py
│  │     │  │  │  ├─ cmdoptions.py
│  │     │  │  │  ├─ command_context.py
│  │     │  │  │  ├─ main.py
│  │     │  │  │  ├─ main_parser.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ progress_bars.py
│  │     │  │  │  ├─ req_command.py
│  │     │  │  │  ├─ spinners.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ autocompletion.cpython-311.pyc
│  │     │  │  │     ├─ base_command.cpython-311.pyc
│  │     │  │  │     ├─ cmdoptions.cpython-311.pyc
│  │     │  │  │     ├─ command_context.cpython-311.pyc
│  │     │  │  │     ├─ main.cpython-311.pyc
│  │     │  │  │     ├─ main_parser.cpython-311.pyc
│  │     │  │  │     ├─ parser.cpython-311.pyc
│  │     │  │  │     ├─ progress_bars.cpython-311.pyc
│  │     │  │  │     ├─ req_command.cpython-311.pyc
│  │     │  │  │     ├─ spinners.cpython-311.pyc
│  │     │  │  │     ├─ status_codes.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ commands
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ configuration.py
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ hash.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ inspect.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ show.py
│  │     │  │  │  ├─ uninstall.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cache.cpython-311.pyc
│  │     │  │  │     ├─ check.cpython-311.pyc
│  │     │  │  │     ├─ completion.cpython-311.pyc
│  │     │  │  │     ├─ configuration.cpython-311.pyc
│  │     │  │  │     ├─ debug.cpython-311.pyc
│  │     │  │  │     ├─ download.cpython-311.pyc
│  │     │  │  │     ├─ freeze.cpython-311.pyc
│  │     │  │  │     ├─ hash.cpython-311.pyc
│  │     │  │  │     ├─ help.cpython-311.pyc
│  │     │  │  │     ├─ index.cpython-311.pyc
│  │     │  │  │     ├─ inspect.cpython-311.pyc
│  │     │  │  │     ├─ install.cpython-311.pyc
│  │     │  │  │     ├─ list.cpython-311.pyc
│  │     │  │  │     ├─ search.cpython-311.pyc
│  │     │  │  │     ├─ show.cpython-311.pyc
│  │     │  │  │     ├─ uninstall.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ configuration.py
│  │     │  │  ├─ distributions
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ installed.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ installed.cpython-311.pyc
│  │     │  │  │     ├─ sdist.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ index
│  │     │  │  │  ├─ collector.py
│  │     │  │  │  ├─ package_finder.py
│  │     │  │  │  ├─ sources.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ collector.cpython-311.pyc
│  │     │  │  │     ├─ package_finder.cpython-311.pyc
│  │     │  │  │     ├─ sources.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ locations
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _sysconfig.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ _distutils.cpython-311.pyc
│  │     │  │  │     ├─ _sysconfig.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ main.py
│  │     │  │  ├─ metadata
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ importlib
│  │     │  │  │  │  ├─ _compat.py
│  │     │  │  │  │  ├─ _dists.py
│  │     │  │  │  │  ├─ _envs.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │  │     ├─ _dists.cpython-311.pyc
│  │     │  │  │  │     ├─ _envs.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ pkg_resources.py
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ pkg_resources.cpython-311.pyc
│  │     │  │  │     ├─ _json.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ models
│  │     │  │  │  ├─ candidate.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ format_control.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ installation_report.py
│  │     │  │  │  ├─ link.py
│  │     │  │  │  ├─ scheme.py
│  │     │  │  │  ├─ search_scope.py
│  │     │  │  │  ├─ selection_prefs.py
│  │     │  │  │  ├─ target_python.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ candidate.cpython-311.pyc
│  │     │  │  │     ├─ direct_url.cpython-311.pyc
│  │     │  │  │     ├─ format_control.cpython-311.pyc
│  │     │  │  │     ├─ index.cpython-311.pyc
│  │     │  │  │     ├─ installation_report.cpython-311.pyc
│  │     │  │  │     ├─ link.cpython-311.pyc
│  │     │  │  │     ├─ scheme.cpython-311.pyc
│  │     │  │  │     ├─ search_scope.cpython-311.pyc
│  │     │  │  │     ├─ selection_prefs.cpython-311.pyc
│  │     │  │  │     ├─ target_python.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ network
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ lazy_wheel.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ xmlrpc.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auth.cpython-311.pyc
│  │     │  │  │     ├─ cache.cpython-311.pyc
│  │     │  │  │     ├─ download.cpython-311.pyc
│  │     │  │  │     ├─ lazy_wheel.cpython-311.pyc
│  │     │  │  │     ├─ session.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ xmlrpc.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ operations
│  │     │  │  │  ├─ build
│  │     │  │  │  │  ├─ build_tracker.py
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ metadata_editable.py
│  │     │  │  │  │  ├─ metadata_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ wheel_editable.py
│  │     │  │  │  │  ├─ wheel_legacy.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ build_tracker.cpython-311.pyc
│  │     │  │  │  │     ├─ metadata.cpython-311.pyc
│  │     │  │  │  │     ├─ metadata_editable.cpython-311.pyc
│  │     │  │  │  │     ├─ metadata_legacy.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel_editable.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel_legacy.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ install
│  │     │  │  │  │  ├─ editable_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ editable_legacy.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ prepare.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ check.cpython-311.pyc
│  │     │  │  │     ├─ freeze.cpython-311.pyc
│  │     │  │  │     ├─ prepare.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyproject.py
│  │     │  │  ├─ req
│  │     │  │  │  ├─ constructors.py
│  │     │  │  │  ├─ req_file.py
│  │     │  │  │  ├─ req_install.py
│  │     │  │  │  ├─ req_set.py
│  │     │  │  │  ├─ req_uninstall.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ constructors.cpython-311.pyc
│  │     │  │  │     ├─ req_file.cpython-311.pyc
│  │     │  │  │     ├─ req_install.cpython-311.pyc
│  │     │  │  │     ├─ req_set.cpython-311.pyc
│  │     │  │  │     ├─ req_uninstall.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ resolution
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ legacy
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ resolver.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ resolvelib
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ candidates.py
│  │     │  │  │  │  ├─ factory.py
│  │     │  │  │  │  ├─ found_candidates.py
│  │     │  │  │  │  ├─ provider.py
│  │     │  │  │  │  ├─ reporter.py
│  │     │  │  │  │  ├─ requirements.py
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │  │     ├─ candidates.cpython-311.pyc
│  │     │  │  │  │     ├─ factory.cpython-311.pyc
│  │     │  │  │  │     ├─ found_candidates.cpython-311.pyc
│  │     │  │  │  │     ├─ provider.cpython-311.pyc
│  │     │  │  │  │     ├─ reporter.cpython-311.pyc
│  │     │  │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │  │     ├─ resolver.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ self_outdated_check.py
│  │     │  │  ├─ utils
│  │     │  │  │  ├─ appdirs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ compatibility_tags.py
│  │     │  │  │  ├─ datetime.py
│  │     │  │  │  ├─ deprecation.py
│  │     │  │  │  ├─ direct_url_helpers.py
│  │     │  │  │  ├─ egg_link.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ entrypoints.py
│  │     │  │  │  ├─ filesystem.py
│  │     │  │  │  ├─ filetypes.py
│  │     │  │  │  ├─ glibc.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ setuptools_build.py
│  │     │  │  │  ├─ subprocess.py
│  │     │  │  │  ├─ temp_dir.py
│  │     │  │  │  ├─ unpacking.py
│  │     │  │  │  ├─ urls.py
│  │     │  │  │  ├─ virtualenv.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ _jaraco_text.py
│  │     │  │  │  ├─ _log.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ appdirs.cpython-311.pyc
│  │     │  │  │     ├─ compat.cpython-311.pyc
│  │     │  │  │     ├─ compatibility_tags.cpython-311.pyc
│  │     │  │  │     ├─ datetime.cpython-311.pyc
│  │     │  │  │     ├─ deprecation.cpython-311.pyc
│  │     │  │  │     ├─ direct_url_helpers.cpython-311.pyc
│  │     │  │  │     ├─ egg_link.cpython-311.pyc
│  │     │  │  │     ├─ encoding.cpython-311.pyc
│  │     │  │  │     ├─ entrypoints.cpython-311.pyc
│  │     │  │  │     ├─ filesystem.cpython-311.pyc
│  │     │  │  │     ├─ filetypes.cpython-311.pyc
│  │     │  │  │     ├─ glibc.cpython-311.pyc
│  │     │  │  │     ├─ hashes.cpython-311.pyc
│  │     │  │  │     ├─ logging.cpython-311.pyc
│  │     │  │  │     ├─ misc.cpython-311.pyc
│  │     │  │  │     ├─ models.cpython-311.pyc
│  │     │  │  │     ├─ packaging.cpython-311.pyc
│  │     │  │  │     ├─ setuptools_build.cpython-311.pyc
│  │     │  │  │     ├─ subprocess.cpython-311.pyc
│  │     │  │  │     ├─ temp_dir.cpython-311.pyc
│  │     │  │  │     ├─ unpacking.cpython-311.pyc
│  │     │  │  │     ├─ urls.cpython-311.pyc
│  │     │  │  │     ├─ virtualenv.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     ├─ _jaraco_text.cpython-311.pyc
│  │     │  │  │     ├─ _log.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ vcs
│  │     │  │  │  ├─ bazaar.py
│  │     │  │  │  ├─ git.py
│  │     │  │  │  ├─ mercurial.py
│  │     │  │  │  ├─ subversion.py
│  │     │  │  │  ├─ versioncontrol.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bazaar.cpython-311.pyc
│  │     │  │  │     ├─ git.cpython-311.pyc
│  │     │  │  │     ├─ mercurial.cpython-311.pyc
│  │     │  │  │     ├─ subversion.cpython-311.pyc
│  │     │  │  │     ├─ versioncontrol.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ wheel_builder.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ build_env.cpython-311.pyc
│  │     │  │     ├─ cache.cpython-311.pyc
│  │     │  │     ├─ configuration.cpython-311.pyc
│  │     │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │     ├─ main.cpython-311.pyc
│  │     │  │     ├─ pyproject.cpython-311.pyc
│  │     │  │     ├─ self_outdated_check.cpython-311.pyc
│  │     │  │     ├─ wheel_builder.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ cachecontrol
│  │     │  │  │  ├─ adapter.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ caches
│  │     │  │  │  │  ├─ file_cache.py
│  │     │  │  │  │  ├─ redis_cache.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ file_cache.cpython-311.pyc
│  │     │  │  │  │     ├─ redis_cache.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ controller.py
│  │     │  │  │  ├─ filewrapper.py
│  │     │  │  │  ├─ heuristics.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ serialize.py
│  │     │  │  │  ├─ wrapper.py
│  │     │  │  │  ├─ _cmd.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ adapter.cpython-311.pyc
│  │     │  │  │     ├─ cache.cpython-311.pyc
│  │     │  │  │     ├─ controller.cpython-311.pyc
│  │     │  │  │     ├─ filewrapper.cpython-311.pyc
│  │     │  │  │     ├─ heuristics.cpython-311.pyc
│  │     │  │  │     ├─ serialize.cpython-311.pyc
│  │     │  │  │     ├─ wrapper.cpython-311.pyc
│  │     │  │  │     ├─ _cmd.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ certifi
│  │     │  │  │  ├─ cacert.pem
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ chardet
│  │     │  │  │  ├─ big5freq.py
│  │     │  │  │  ├─ big5prober.py
│  │     │  │  │  ├─ chardistribution.py
│  │     │  │  │  ├─ charsetgroupprober.py
│  │     │  │  │  ├─ charsetprober.py
│  │     │  │  │  ├─ cli
│  │     │  │  │  │  ├─ chardetect.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ chardetect.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ codingstatemachine.py
│  │     │  │  │  ├─ codingstatemachinedict.py
│  │     │  │  │  ├─ cp949prober.py
│  │     │  │  │  ├─ enums.py
│  │     │  │  │  ├─ escprober.py
│  │     │  │  │  ├─ escsm.py
│  │     │  │  │  ├─ eucjpprober.py
│  │     │  │  │  ├─ euckrfreq.py
│  │     │  │  │  ├─ euckrprober.py
│  │     │  │  │  ├─ euctwfreq.py
│  │     │  │  │  ├─ euctwprober.py
│  │     │  │  │  ├─ gb2312freq.py
│  │     │  │  │  ├─ gb2312prober.py
│  │     │  │  │  ├─ hebrewprober.py
│  │     │  │  │  ├─ jisfreq.py
│  │     │  │  │  ├─ johabfreq.py
│  │     │  │  │  ├─ johabprober.py
│  │     │  │  │  ├─ jpcntx.py
│  │     │  │  │  ├─ langbulgarianmodel.py
│  │     │  │  │  ├─ langgreekmodel.py
│  │     │  │  │  ├─ langhebrewmodel.py
│  │     │  │  │  ├─ langhungarianmodel.py
│  │     │  │  │  ├─ langrussianmodel.py
│  │     │  │  │  ├─ langthaimodel.py
│  │     │  │  │  ├─ langturkishmodel.py
│  │     │  │  │  ├─ latin1prober.py
│  │     │  │  │  ├─ macromanprober.py
│  │     │  │  │  ├─ mbcharsetprober.py
│  │     │  │  │  ├─ mbcsgroupprober.py
│  │     │  │  │  ├─ mbcssm.py
│  │     │  │  │  ├─ metadata
│  │     │  │  │  │  ├─ languages.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ languages.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ resultdict.py
│  │     │  │  │  ├─ sbcharsetprober.py
│  │     │  │  │  ├─ sbcsgroupprober.py
│  │     │  │  │  ├─ sjisprober.py
│  │     │  │  │  ├─ universaldetector.py
│  │     │  │  │  ├─ utf1632prober.py
│  │     │  │  │  ├─ utf8prober.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ big5freq.cpython-311.pyc
│  │     │  │  │     ├─ big5prober.cpython-311.pyc
│  │     │  │  │     ├─ chardistribution.cpython-311.pyc
│  │     │  │  │     ├─ charsetgroupprober.cpython-311.pyc
│  │     │  │  │     ├─ charsetprober.cpython-311.pyc
│  │     │  │  │     ├─ codingstatemachine.cpython-311.pyc
│  │     │  │  │     ├─ codingstatemachinedict.cpython-311.pyc
│  │     │  │  │     ├─ cp949prober.cpython-311.pyc
│  │     │  │  │     ├─ enums.cpython-311.pyc
│  │     │  │  │     ├─ escprober.cpython-311.pyc
│  │     │  │  │     ├─ escsm.cpython-311.pyc
│  │     │  │  │     ├─ eucjpprober.cpython-311.pyc
│  │     │  │  │     ├─ euckrfreq.cpython-311.pyc
│  │     │  │  │     ├─ euckrprober.cpython-311.pyc
│  │     │  │  │     ├─ euctwfreq.cpython-311.pyc
│  │     │  │  │     ├─ euctwprober.cpython-311.pyc
│  │     │  │  │     ├─ gb2312freq.cpython-311.pyc
│  │     │  │  │     ├─ gb2312prober.cpython-311.pyc
│  │     │  │  │     ├─ hebrewprober.cpython-311.pyc
│  │     │  │  │     ├─ jisfreq.cpython-311.pyc
│  │     │  │  │     ├─ johabfreq.cpython-311.pyc
│  │     │  │  │     ├─ johabprober.cpython-311.pyc
│  │     │  │  │     ├─ jpcntx.cpython-311.pyc
│  │     │  │  │     ├─ langbulgarianmodel.cpython-311.pyc
│  │     │  │  │     ├─ langgreekmodel.cpython-311.pyc
│  │     │  │  │     ├─ langhebrewmodel.cpython-311.pyc
│  │     │  │  │     ├─ langhungarianmodel.cpython-311.pyc
│  │     │  │  │     ├─ langrussianmodel.cpython-311.pyc
│  │     │  │  │     ├─ langthaimodel.cpython-311.pyc
│  │     │  │  │     ├─ langturkishmodel.cpython-311.pyc
│  │     │  │  │     ├─ latin1prober.cpython-311.pyc
│  │     │  │  │     ├─ macromanprober.cpython-311.pyc
│  │     │  │  │     ├─ mbcharsetprober.cpython-311.pyc
│  │     │  │  │     ├─ mbcsgroupprober.cpython-311.pyc
│  │     │  │  │     ├─ mbcssm.cpython-311.pyc
│  │     │  │  │     ├─ resultdict.cpython-311.pyc
│  │     │  │  │     ├─ sbcharsetprober.cpython-311.pyc
│  │     │  │  │     ├─ sbcsgroupprober.cpython-311.pyc
│  │     │  │  │     ├─ sjisprober.cpython-311.pyc
│  │     │  │  │     ├─ universaldetector.cpython-311.pyc
│  │     │  │  │     ├─ utf1632prober.cpython-311.pyc
│  │     │  │  │     ├─ utf8prober.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ colorama
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ ansitowin32.py
│  │     │  │  │  ├─ initialise.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ ansitowin32_test.py
│  │     │  │  │  │  ├─ ansi_test.py
│  │     │  │  │  │  ├─ initialise_test.py
│  │     │  │  │  │  ├─ isatty_test.py
│  │     │  │  │  │  ├─ utils.py
│  │     │  │  │  │  ├─ winterm_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ ansitowin32_test.cpython-311.pyc
│  │     │  │  │  │     ├─ ansi_test.cpython-311.pyc
│  │     │  │  │  │     ├─ initialise_test.cpython-311.pyc
│  │     │  │  │  │     ├─ isatty_test.cpython-311.pyc
│  │     │  │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │  │     ├─ winterm_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ win32.py
│  │     │  │  │  ├─ winterm.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ansi.cpython-311.pyc
│  │     │  │  │     ├─ ansitowin32.cpython-311.pyc
│  │     │  │  │     ├─ initialise.cpython-311.pyc
│  │     │  │  │     ├─ win32.cpython-311.pyc
│  │     │  │  │     ├─ winterm.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ distlib
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ database.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ locators.py
│  │     │  │  │  ├─ manifest.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ resources.py
│  │     │  │  │  ├─ scripts.py
│  │     │  │  │  ├─ t32.exe
│  │     │  │  │  ├─ t64-arm.exe
│  │     │  │  │  ├─ t64.exe
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ w32.exe
│  │     │  │  │  ├─ w64-arm.exe
│  │     │  │  │  ├─ w64.exe
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ compat.cpython-311.pyc
│  │     │  │  │     ├─ database.cpython-311.pyc
│  │     │  │  │     ├─ index.cpython-311.pyc
│  │     │  │  │     ├─ locators.cpython-311.pyc
│  │     │  │  │     ├─ manifest.cpython-311.pyc
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ metadata.cpython-311.pyc
│  │     │  │  │     ├─ resources.cpython-311.pyc
│  │     │  │  │     ├─ scripts.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ distro
│  │     │  │  │  ├─ distro.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ distro.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ idna
│  │     │  │  │  ├─ codec.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ idnadata.py
│  │     │  │  │  ├─ intranges.py
│  │     │  │  │  ├─ package_data.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ uts46data.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ codec.cpython-311.pyc
│  │     │  │  │     ├─ compat.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ idnadata.cpython-311.pyc
│  │     │  │  │     ├─ intranges.cpython-311.pyc
│  │     │  │  │     ├─ package_data.cpython-311.pyc
│  │     │  │  │     ├─ uts46data.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ msgpack
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  ├─ fallback.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ ext.cpython-311.pyc
│  │     │  │  │     ├─ fallback.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │     ├─ specifiers.cpython-311.pyc
│  │     │  │  │     ├─ tags.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ _manylinux.cpython-311.pyc
│  │     │  │  │     ├─ _musllinux.cpython-311.pyc
│  │     │  │  │     ├─ _structures.cpython-311.pyc
│  │     │  │  │     ├─ __about__.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pkg_resources
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ platformdirs
│  │     │  │  │  ├─ android.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ macos.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ unix.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ android.cpython-311.pyc
│  │     │  │  │     ├─ api.cpython-311.pyc
│  │     │  │  │     ├─ macos.cpython-311.pyc
│  │     │  │  │     ├─ unix.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ windows.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ pygments
│  │     │  │  │  ├─ cmdline.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ filter.py
│  │     │  │  │  ├─ filters
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ formatter.py
│  │     │  │  │  ├─ formatters
│  │     │  │  │  │  ├─ bbcode.py
│  │     │  │  │  │  ├─ groff.py
│  │     │  │  │  │  ├─ html.py
│  │     │  │  │  │  ├─ img.py
│  │     │  │  │  │  ├─ irc.py
│  │     │  │  │  │  ├─ latex.py
│  │     │  │  │  │  ├─ other.py
│  │     │  │  │  │  ├─ pangomarkup.py
│  │     │  │  │  │  ├─ rtf.py
│  │     │  │  │  │  ├─ svg.py
│  │     │  │  │  │  ├─ terminal.py
│  │     │  │  │  │  ├─ terminal256.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ bbcode.cpython-311.pyc
│  │     │  │  │  │     ├─ groff.cpython-311.pyc
│  │     │  │  │  │     ├─ html.cpython-311.pyc
│  │     │  │  │  │     ├─ img.cpython-311.pyc
│  │     │  │  │  │     ├─ irc.cpython-311.pyc
│  │     │  │  │  │     ├─ latex.cpython-311.pyc
│  │     │  │  │  │     ├─ other.cpython-311.pyc
│  │     │  │  │  │     ├─ pangomarkup.cpython-311.pyc
│  │     │  │  │  │     ├─ rtf.cpython-311.pyc
│  │     │  │  │  │     ├─ svg.cpython-311.pyc
│  │     │  │  │  │     ├─ terminal.cpython-311.pyc
│  │     │  │  │  │     ├─ terminal256.cpython-311.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ lexer.py
│  │     │  │  │  ├─ lexers
│  │     │  │  │  │  ├─ python.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ python.cpython-311.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ modeline.py
│  │     │  │  │  ├─ plugin.py
│  │     │  │  │  ├─ regexopt.py
│  │     │  │  │  ├─ scanner.py
│  │     │  │  │  ├─ sphinxext.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styles
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ token.py
│  │     │  │  │  ├─ unistring.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cmdline.cpython-311.pyc
│  │     │  │  │     ├─ console.cpython-311.pyc
│  │     │  │  │     ├─ filter.cpython-311.pyc
│  │     │  │  │     ├─ formatter.cpython-311.pyc
│  │     │  │  │     ├─ lexer.cpython-311.pyc
│  │     │  │  │     ├─ modeline.cpython-311.pyc
│  │     │  │  │     ├─ plugin.cpython-311.pyc
│  │     │  │  │     ├─ regexopt.cpython-311.pyc
│  │     │  │  │     ├─ scanner.cpython-311.pyc
│  │     │  │  │     ├─ sphinxext.cpython-311.pyc
│  │     │  │  │     ├─ style.cpython-311.pyc
│  │     │  │  │     ├─ token.cpython-311.pyc
│  │     │  │  │     ├─ unistring.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ pyparsing
│  │     │  │  │  ├─ actions.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ diagram
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ helpers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ results.py
│  │     │  │  │  ├─ testing.py
│  │     │  │  │  ├─ unicode.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ actions.cpython-311.pyc
│  │     │  │  │     ├─ common.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ helpers.cpython-311.pyc
│  │     │  │  │     ├─ results.cpython-311.pyc
│  │     │  │  │     ├─ testing.cpython-311.pyc
│  │     │  │  │     ├─ unicode.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyproject_hooks
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _impl.py
│  │     │  │  │  ├─ _in_process
│  │     │  │  │  │  ├─ _in_process.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _in_process.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _impl.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ requests
│  │     │  │  │  ├─ adapters.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ certs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ hooks.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packages.py
│  │     │  │  │  ├─ sessions.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ structures.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _internal_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __pycache__
│  │     │  │  │  │  ├─ adapters.cpython-311.pyc
│  │     │  │  │  │  ├─ api.cpython-311.pyc
│  │     │  │  │  │  ├─ auth.cpython-311.pyc
│  │     │  │  │  │  ├─ certs.cpython-311.pyc
│  │     │  │  │  │  ├─ compat.cpython-311.pyc
│  │     │  │  │  │  ├─ cookies.cpython-311.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-311.pyc
│  │     │  │  │  │  ├─ help.cpython-311.pyc
│  │     │  │  │  │  ├─ hooks.cpython-311.pyc
│  │     │  │  │  │  ├─ models.cpython-311.pyc
│  │     │  │  │  │  ├─ packages.cpython-311.pyc
│  │     │  │  │  │  ├─ sessions.cpython-311.pyc
│  │     │  │  │  │  ├─ status_codes.cpython-311.pyc
│  │     │  │  │  │  ├─ structures.cpython-311.pyc
│  │     │  │  │  │  ├─ utils.cpython-311.pyc
│  │     │  │  │  │  ├─ _internal_utils.cpython-311.pyc
│  │     │  │  │  │  ├─ __init__.cpython-311.pyc
│  │     │  │  │  │  └─ __version__.cpython-311.pyc
│  │     │  │  │  └─ __version__.py
│  │     │  │  ├─ resolvelib
│  │     │  │  │  ├─ compat
│  │     │  │  │  │  ├─ collections_abc.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ collections_abc.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ providers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ reporters.py
│  │     │  │  │  ├─ resolvers.py
│  │     │  │  │  ├─ structs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ providers.cpython-311.pyc
│  │     │  │  │     ├─ reporters.cpython-311.pyc
│  │     │  │  │     ├─ resolvers.cpython-311.pyc
│  │     │  │  │     ├─ structs.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ rich
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ box.py
│  │     │  │  │  ├─ cells.py
│  │     │  │  │  ├─ color.py
│  │     │  │  │  ├─ color_triplet.py
│  │     │  │  │  ├─ columns.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ constrain.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ control.py
│  │     │  │  │  ├─ default_styles.py
│  │     │  │  │  ├─ diagnose.py
│  │     │  │  │  ├─ emoji.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ filesize.py
│  │     │  │  │  ├─ file_proxy.py
│  │     │  │  │  ├─ highlighter.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ jupyter.py
│  │     │  │  │  ├─ layout.py
│  │     │  │  │  ├─ live.py
│  │     │  │  │  ├─ live_render.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ markup.py
│  │     │  │  │  ├─ measure.py
│  │     │  │  │  ├─ padding.py
│  │     │  │  │  ├─ pager.py
│  │     │  │  │  ├─ palette.py
│  │     │  │  │  ├─ panel.py
│  │     │  │  │  ├─ pretty.py
│  │     │  │  │  ├─ progress.py
│  │     │  │  │  ├─ progress_bar.py
│  │     │  │  │  ├─ prompt.py
│  │     │  │  │  ├─ protocol.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ region.py
│  │     │  │  │  ├─ repr.py
│  │     │  │  │  ├─ rule.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  ├─ screen.py
│  │     │  │  │  ├─ segment.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ status.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styled.py
│  │     │  │  │  ├─ syntax.py
│  │     │  │  │  ├─ table.py
│  │     │  │  │  ├─ terminal_theme.py
│  │     │  │  │  ├─ text.py
│  │     │  │  │  ├─ theme.py
│  │     │  │  │  ├─ themes.py
│  │     │  │  │  ├─ traceback.py
│  │     │  │  │  ├─ tree.py
│  │     │  │  │  ├─ _cell_widths.py
│  │     │  │  │  ├─ _emoji_codes.py
│  │     │  │  │  ├─ _emoji_replace.py
│  │     │  │  │  ├─ _export_format.py
│  │     │  │  │  ├─ _extension.py
│  │     │  │  │  ├─ _fileno.py
│  │     │  │  │  ├─ _inspect.py
│  │     │  │  │  ├─ _log_render.py
│  │     │  │  │  ├─ _loop.py
│  │     │  │  │  ├─ _null_file.py
│  │     │  │  │  ├─ _palettes.py
│  │     │  │  │  ├─ _pick.py
│  │     │  │  │  ├─ _ratio.py
│  │     │  │  │  ├─ _spinners.py
│  │     │  │  │  ├─ _stack.py
│  │     │  │  │  ├─ _timer.py
│  │     │  │  │  ├─ _win32_console.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ _windows_renderer.py
│  │     │  │  │  ├─ _wrap.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-311.pyc
│  │     │  │  │     ├─ align.cpython-311.pyc
│  │     │  │  │     ├─ ansi.cpython-311.pyc
│  │     │  │  │     ├─ bar.cpython-311.pyc
│  │     │  │  │     ├─ box.cpython-311.pyc
│  │     │  │  │     ├─ cells.cpython-311.pyc
│  │     │  │  │     ├─ color.cpython-311.pyc
│  │     │  │  │     ├─ color_triplet.cpython-311.pyc
│  │     │  │  │     ├─ columns.cpython-311.pyc
│  │     │  │  │     ├─ console.cpython-311.pyc
│  │     │  │  │     ├─ constrain.cpython-311.pyc
│  │     │  │  │     ├─ containers.cpython-311.pyc
│  │     │  │  │     ├─ control.cpython-311.pyc
│  │     │  │  │     ├─ default_styles.cpython-311.pyc
│  │     │  │  │     ├─ diagnose.cpython-311.pyc
│  │     │  │  │     ├─ emoji.cpython-311.pyc
│  │     │  │  │     ├─ errors.cpython-311.pyc
│  │     │  │  │     ├─ filesize.cpython-311.pyc
│  │     │  │  │     ├─ file_proxy.cpython-311.pyc
│  │     │  │  │     ├─ highlighter.cpython-311.pyc
│  │     │  │  │     ├─ json.cpython-311.pyc
│  │     │  │  │     ├─ jupyter.cpython-311.pyc
│  │     │  │  │     ├─ layout.cpython-311.pyc
│  │     │  │  │     ├─ live.cpython-311.pyc
│  │     │  │  │     ├─ live_render.cpython-311.pyc
│  │     │  │  │     ├─ logging.cpython-311.pyc
│  │     │  │  │     ├─ markup.cpython-311.pyc
│  │     │  │  │     ├─ measure.cpython-311.pyc
│  │     │  │  │     ├─ padding.cpython-311.pyc
│  │     │  │  │     ├─ pager.cpython-311.pyc
│  │     │  │  │     ├─ palette.cpython-311.pyc
│  │     │  │  │     ├─ panel.cpython-311.pyc
│  │     │  │  │     ├─ pretty.cpython-311.pyc
│  │     │  │  │     ├─ progress.cpython-311.pyc
│  │     │  │  │     ├─ progress_bar.cpython-311.pyc
│  │     │  │  │     ├─ prompt.cpython-311.pyc
│  │     │  │  │     ├─ protocol.cpython-311.pyc
│  │     │  │  │     ├─ region.cpython-311.pyc
│  │     │  │  │     ├─ repr.cpython-311.pyc
│  │     │  │  │     ├─ rule.cpython-311.pyc
│  │     │  │  │     ├─ scope.cpython-311.pyc
│  │     │  │  │     ├─ screen.cpython-311.pyc
│  │     │  │  │     ├─ segment.cpython-311.pyc
│  │     │  │  │     ├─ spinner.cpython-311.pyc
│  │     │  │  │     ├─ status.cpython-311.pyc
│  │     │  │  │     ├─ style.cpython-311.pyc
│  │     │  │  │     ├─ styled.cpython-311.pyc
│  │     │  │  │     ├─ syntax.cpython-311.pyc
│  │     │  │  │     ├─ table.cpython-311.pyc
│  │     │  │  │     ├─ terminal_theme.cpython-311.pyc
│  │     │  │  │     ├─ text.cpython-311.pyc
│  │     │  │  │     ├─ theme.cpython-311.pyc
│  │     │  │  │     ├─ themes.cpython-311.pyc
│  │     │  │  │     ├─ traceback.cpython-311.pyc
│  │     │  │  │     ├─ tree.cpython-311.pyc
│  │     │  │  │     ├─ _cell_widths.cpython-311.pyc
│  │     │  │  │     ├─ _emoji_codes.cpython-311.pyc
│  │     │  │  │     ├─ _emoji_replace.cpython-311.pyc
│  │     │  │  │     ├─ _export_format.cpython-311.pyc
│  │     │  │  │     ├─ _extension.cpython-311.pyc
│  │     │  │  │     ├─ _fileno.cpython-311.pyc
│  │     │  │  │     ├─ _inspect.cpython-311.pyc
│  │     │  │  │     ├─ _log_render.cpython-311.pyc
│  │     │  │  │     ├─ _loop.cpython-311.pyc
│  │     │  │  │     ├─ _null_file.cpython-311.pyc
│  │     │  │  │     ├─ _palettes.cpython-311.pyc
│  │     │  │  │     ├─ _pick.cpython-311.pyc
│  │     │  │  │     ├─ _ratio.cpython-311.pyc
│  │     │  │  │     ├─ _spinners.cpython-311.pyc
│  │     │  │  │     ├─ _stack.cpython-311.pyc
│  │     │  │  │     ├─ _timer.cpython-311.pyc
│  │     │  │  │     ├─ _win32_console.cpython-311.pyc
│  │     │  │  │     ├─ _windows.cpython-311.pyc
│  │     │  │  │     ├─ _windows_renderer.cpython-311.pyc
│  │     │  │  │     ├─ _wrap.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ six.py
│  │     │  │  ├─ tenacity
│  │     │  │  │  ├─ after.py
│  │     │  │  │  ├─ before.py
│  │     │  │  │  ├─ before_sleep.py
│  │     │  │  │  ├─ nap.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ stop.py
│  │     │  │  │  ├─ tornadoweb.py
│  │     │  │  │  ├─ wait.py
│  │     │  │  │  ├─ _asyncio.py
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ after.cpython-311.pyc
│  │     │  │  │     ├─ before.cpython-311.pyc
│  │     │  │  │     ├─ before_sleep.cpython-311.pyc
│  │     │  │  │     ├─ nap.cpython-311.pyc
│  │     │  │  │     ├─ retry.cpython-311.pyc
│  │     │  │  │     ├─ stop.cpython-311.pyc
│  │     │  │  │     ├─ tornadoweb.cpython-311.pyc
│  │     │  │  │     ├─ wait.cpython-311.pyc
│  │     │  │  │     ├─ _asyncio.cpython-311.pyc
│  │     │  │  │     ├─ _utils.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ tomli
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ _types.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _parser.cpython-311.pyc
│  │     │  │  │     ├─ _re.cpython-311.pyc
│  │     │  │  │     ├─ _types.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ truststore
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _api.py
│  │     │  │  │  ├─ _macos.py
│  │     │  │  │  ├─ _openssl.py
│  │     │  │  │  ├─ _ssl_constants.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _api.cpython-311.pyc
│  │     │  │  │     ├─ _macos.cpython-311.pyc
│  │     │  │  │     ├─ _openssl.cpython-311.pyc
│  │     │  │  │     ├─ _ssl_constants.cpython-311.pyc
│  │     │  │  │     ├─ _windows.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ typing_extensions.py
│  │     │  │  ├─ urllib3
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ connectionpool.py
│  │     │  │  │  ├─ contrib
│  │     │  │  │  │  ├─ appengine.py
│  │     │  │  │  │  ├─ ntlmpool.py
│  │     │  │  │  │  ├─ pyopenssl.py
│  │     │  │  │  │  ├─ securetransport.py
│  │     │  │  │  │  ├─ socks.py
│  │     │  │  │  │  ├─ _appengine_environ.py
│  │     │  │  │  │  ├─ _securetransport
│  │     │  │  │  │  │  ├─ bindings.py
│  │     │  │  │  │  │  ├─ low_level.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ bindings.cpython-311.pyc
│  │     │  │  │  │  │     ├─ low_level.cpython-311.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ appengine.cpython-311.pyc
│  │     │  │  │  │     ├─ ntlmpool.cpython-311.pyc
│  │     │  │  │  │     ├─ pyopenssl.cpython-311.pyc
│  │     │  │  │  │     ├─ securetransport.cpython-311.pyc
│  │     │  │  │  │     ├─ socks.cpython-311.pyc
│  │     │  │  │  │     ├─ _appengine_environ.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fields.py
│  │     │  │  │  ├─ filepost.py
│  │     │  │  │  ├─ packages
│  │     │  │  │  │  ├─ backports
│  │     │  │  │  │  │  ├─ makefile.py
│  │     │  │  │  │  │  ├─ weakref_finalize.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ makefile.cpython-311.pyc
│  │     │  │  │  │  │     ├─ weakref_finalize.cpython-311.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  │  ├─ six.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ six.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ poolmanager.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ util
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ proxy.py
│  │     │  │  │  │  ├─ queue.py
│  │     │  │  │  │  ├─ request.py
│  │     │  │  │  │  ├─ response.py
│  │     │  │  │  │  ├─ retry.py
│  │     │  │  │  │  ├─ ssltransport.py
│  │     │  │  │  │  ├─ ssl_.py
│  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │     │  │  │  │  ├─ timeout.py
│  │     │  │  │  │  ├─ url.py
│  │     │  │  │  │  ├─ wait.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ connection.cpython-311.pyc
│  │     │  │  │  │     ├─ proxy.cpython-311.pyc
│  │     │  │  │  │     ├─ queue.cpython-311.pyc
│  │     │  │  │  │     ├─ request.cpython-311.pyc
│  │     │  │  │  │     ├─ response.cpython-311.pyc
│  │     │  │  │  │     ├─ retry.cpython-311.pyc
│  │     │  │  │  │     ├─ ssltransport.cpython-311.pyc
│  │     │  │  │  │     ├─ ssl_.cpython-311.pyc
│  │     │  │  │  │     ├─ ssl_match_hostname.cpython-311.pyc
│  │     │  │  │  │     ├─ timeout.cpython-311.pyc
│  │     │  │  │  │     ├─ url.cpython-311.pyc
│  │     │  │  │  │     ├─ wait.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ connection.cpython-311.pyc
│  │     │  │  │     ├─ connectionpool.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ fields.cpython-311.pyc
│  │     │  │  │     ├─ filepost.cpython-311.pyc
│  │     │  │  │     ├─ poolmanager.cpython-311.pyc
│  │     │  │  │     ├─ request.cpython-311.pyc
│  │     │  │  │     ├─ response.cpython-311.pyc
│  │     │  │  │     ├─ _collections.cpython-311.pyc
│  │     │  │  │     ├─ _version.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ vendor.txt
│  │     │  │  ├─ webencodings
│  │     │  │  │  ├─ labels.py
│  │     │  │  │  ├─ mklabels.py
│  │     │  │  │  ├─ tests.py
│  │     │  │  │  ├─ x_user_defined.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ labels.cpython-311.pyc
│  │     │  │  │     ├─ mklabels.cpython-311.pyc
│  │     │  │  │     ├─ tests.cpython-311.pyc
│  │     │  │  │     ├─ x_user_defined.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ six.cpython-311.pyc
│  │     │  │     ├─ typing_extensions.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ __pip-runner__.py
│  │     │  └─ __pycache__
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     ├─ __main__.cpython-311.pyc
│  │     │     └─ __pip-runner__.cpython-311.pyc
│  │     ├─ pip-24.0.dist-info
│  │     │  ├─ AUTHORS.txt
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pkg_resources
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ appdirs.py
│  │     │  │  ├─ importlib_resources
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ readers.py
│  │     │  │  │  ├─ simple.py
│  │     │  │  │  ├─ _adapters.py
│  │     │  │  │  ├─ _common.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _itertools.py
│  │     │  │  │  ├─ _legacy.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-311.pyc
│  │     │  │  │     ├─ readers.cpython-311.pyc
│  │     │  │  │     ├─ simple.cpython-311.pyc
│  │     │  │  │     ├─ _adapters.cpython-311.pyc
│  │     │  │  │     ├─ _common.cpython-311.pyc
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _itertools.cpython-311.pyc
│  │     │  │  │     ├─ _legacy.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ jaraco
│  │     │  │  │  ├─ context.py
│  │     │  │  │  ├─ functools.py
│  │     │  │  │  ├─ text
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ context.cpython-311.pyc
│  │     │  │  │     ├─ functools.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ more_itertools
│  │     │  │  │  ├─ more.py
│  │     │  │  │  ├─ recipes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ more.cpython-311.pyc
│  │     │  │  │     ├─ recipes.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │     ├─ specifiers.cpython-311.pyc
│  │     │  │  │     ├─ tags.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ _manylinux.cpython-311.pyc
│  │     │  │  │     ├─ _musllinux.cpython-311.pyc
│  │     │  │  │     ├─ _structures.cpython-311.pyc
│  │     │  │  │     ├─ __about__.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyparsing
│  │     │  │  │  ├─ actions.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ diagram
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ helpers.py
│  │     │  │  │  ├─ results.py
│  │     │  │  │  ├─ testing.py
│  │     │  │  │  ├─ unicode.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ actions.cpython-311.pyc
│  │     │  │  │     ├─ common.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ helpers.cpython-311.pyc
│  │     │  │  │     ├─ results.cpython-311.pyc
│  │     │  │  │     ├─ testing.cpython-311.pyc
│  │     │  │  │     ├─ unicode.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ zipp.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ appdirs.cpython-311.pyc
│  │     │  │     ├─ zipp.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ platformdirs
│  │     │  ├─ android.py
│  │     │  ├─ api.py
│  │     │  ├─ macos.py
│  │     │  ├─ py.typed
│  │     │  ├─ unix.py
│  │     │  ├─ version.py
│  │     │  ├─ windows.py
│  │     │  ├─ _xdg.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ android.cpython-311.pyc
│  │     │     ├─ api.cpython-311.pyc
│  │     │     ├─ macos.cpython-311.pyc
│  │     │     ├─ unix.cpython-311.pyc
│  │     │     ├─ version.cpython-311.pyc
│  │     │     ├─ windows.cpython-311.pyc
│  │     │     ├─ _xdg.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ platformdirs-4.10.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pygame
│  │     │  ├─ base.cp311-win_amd64.pyd
│  │     │  ├─ base.pyi
│  │     │  ├─ bufferproxy.cp311-win_amd64.pyd
│  │     │  ├─ bufferproxy.pyi
│  │     │  ├─ camera.py
│  │     │  ├─ camera.pyi
│  │     │  ├─ color.cp311-win_amd64.pyd
│  │     │  ├─ color.pyi
│  │     │  ├─ colordict.py
│  │     │  ├─ constants.cp311-win_amd64.pyd
│  │     │  ├─ constants.pyi
│  │     │  ├─ cursors.py
│  │     │  ├─ cursors.pyi
│  │     │  ├─ display.cp311-win_amd64.pyd
│  │     │  ├─ display.pyi
│  │     │  ├─ docs
│  │     │  │  ├─ generated
│  │     │  │  │  ├─ c_api
│  │     │  │  │  │  ├─ base.html
│  │     │  │  │  │  ├─ bufferproxy.html
│  │     │  │  │  │  ├─ color.html
│  │     │  │  │  │  ├─ display.html
│  │     │  │  │  │  ├─ event.html
│  │     │  │  │  │  ├─ freetype.html
│  │     │  │  │  │  ├─ mixer.html
│  │     │  │  │  │  ├─ rect.html
│  │     │  │  │  │  ├─ rwobject.html
│  │     │  │  │  │  ├─ slots.html
│  │     │  │  │  │  ├─ surface.html
│  │     │  │  │  │  ├─ surflock.html
│  │     │  │  │  │  └─ version.html
│  │     │  │  │  ├─ c_api.html
│  │     │  │  │  ├─ filepaths.html
│  │     │  │  │  ├─ genindex.html
│  │     │  │  │  ├─ index.html
│  │     │  │  │  ├─ LGPL.txt
│  │     │  │  │  ├─ logos.html
│  │     │  │  │  ├─ py-modindex.html
│  │     │  │  │  ├─ ref
│  │     │  │  │  │  ├─ bufferproxy.html
│  │     │  │  │  │  ├─ camera.html
│  │     │  │  │  │  ├─ cdrom.html
│  │     │  │  │  │  ├─ color.html
│  │     │  │  │  │  ├─ color_list.html
│  │     │  │  │  │  ├─ cursors.html
│  │     │  │  │  │  ├─ display.html
│  │     │  │  │  │  ├─ draw.html
│  │     │  │  │  │  ├─ event.html
│  │     │  │  │  │  ├─ examples.html
│  │     │  │  │  │  ├─ fastevent.html
│  │     │  │  │  │  ├─ font.html
│  │     │  │  │  │  ├─ freetype.html
│  │     │  │  │  │  ├─ gfxdraw.html
│  │     │  │  │  │  ├─ image.html
│  │     │  │  │  │  ├─ joystick.html
│  │     │  │  │  │  ├─ key.html
│  │     │  │  │  │  ├─ locals.html
│  │     │  │  │  │  ├─ mask.html
│  │     │  │  │  │  ├─ math.html
│  │     │  │  │  │  ├─ midi.html
│  │     │  │  │  │  ├─ mixer.html
│  │     │  │  │  │  ├─ mouse.html
│  │     │  │  │  │  ├─ music.html
│  │     │  │  │  │  ├─ overlay.html
│  │     │  │  │  │  ├─ pixelarray.html
│  │     │  │  │  │  ├─ pixelcopy.html
│  │     │  │  │  │  ├─ pygame.html
│  │     │  │  │  │  ├─ rect.html
│  │     │  │  │  │  ├─ scrap.html
│  │     │  │  │  │  ├─ sdl2_controller.html
│  │     │  │  │  │  ├─ sdl2_video.html
│  │     │  │  │  │  ├─ sndarray.html
│  │     │  │  │  │  ├─ sprite.html
│  │     │  │  │  │  ├─ surface.html
│  │     │  │  │  │  ├─ surfarray.html
│  │     │  │  │  │  ├─ tests.html
│  │     │  │  │  │  ├─ time.html
│  │     │  │  │  │  ├─ touch.html
│  │     │  │  │  │  └─ transform.html
│  │     │  │  │  ├─ search.html
│  │     │  │  │  ├─ searchindex.js
│  │     │  │  │  ├─ tut
│  │     │  │  │  │  ├─ CameraIntro.html
│  │     │  │  │  │  ├─ chimp.py.html
│  │     │  │  │  │  ├─ ChimpLineByLine.html
│  │     │  │  │  │  ├─ DisplayModes.html
│  │     │  │  │  │  ├─ ImportInit.html
│  │     │  │  │  │  ├─ MakeGames.html
│  │     │  │  │  │  ├─ MoveIt.html
│  │     │  │  │  │  ├─ newbieguide.html
│  │     │  │  │  │  ├─ PygameIntro.html
│  │     │  │  │  │  ├─ SpriteIntro.html
│  │     │  │  │  │  ├─ SurfarrayIntro.html
│  │     │  │  │  │  ├─ tom_games2.html
│  │     │  │  │  │  ├─ tom_games3.html
│  │     │  │  │  │  ├─ tom_games4.html
│  │     │  │  │  │  ├─ tom_games5.html
│  │     │  │  │  │  └─ tom_games6.html
│  │     │  │  │  ├─ _images
│  │     │  │  │  │  ├─ AdvancedInputOutput1.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput11.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput2.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput21.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput3.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput31.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput4.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput41.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput5.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput51.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha1.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha11.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha2.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha21.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha3.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha31.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess1.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess11.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess2.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess21.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess3.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess31.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess4.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess41.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess5.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess51.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess6.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess61.gif
│  │     │  │  │  │  ├─ angle_to.png
│  │     │  │  │  │  ├─ Bagic-INPUT-resultscreen.png
│  │     │  │  │  │  ├─ Bagic-INPUT-resultscreen1.png
│  │     │  │  │  │  ├─ Bagic-INPUT-sourcecode.png
│  │     │  │  │  │  ├─ Bagic-INPUT-sourcecode1.png
│  │     │  │  │  │  ├─ Bagic-ouput-result-screen.png
│  │     │  │  │  │  ├─ Bagic-ouput-result-screen1.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-resultscreen.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-resultscreen1.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-sourcecode.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-sourcecode1.png
│  │     │  │  │  │  ├─ Basic-ouput-sourcecode.png
│  │     │  │  │  │  ├─ Basic-ouput-sourcecode1.png
│  │     │  │  │  │  ├─ camera_average.jpg
│  │     │  │  │  │  ├─ camera_background.jpg
│  │     │  │  │  │  ├─ camera_green.jpg
│  │     │  │  │  │  ├─ camera_hsv.jpg
│  │     │  │  │  │  ├─ camera_mask.jpg
│  │     │  │  │  │  ├─ camera_rgb.jpg
│  │     │  │  │  │  ├─ camera_thresh.jpg
│  │     │  │  │  │  ├─ camera_thresholded.jpg
│  │     │  │  │  │  ├─ camera_yuv.jpg
│  │     │  │  │  │  ├─ chimpshot.gif
│  │     │  │  │  │  ├─ draw_module_example.png
│  │     │  │  │  │  ├─ introduction-Battleship.png
│  │     │  │  │  │  ├─ introduction-Battleship1.png
│  │     │  │  │  │  ├─ introduction-PuyoPuyo.png
│  │     │  │  │  │  ├─ introduction-PuyoPuyo1.png
│  │     │  │  │  │  ├─ introduction-TPS.png
│  │     │  │  │  │  ├─ introduction-TPS1.png
│  │     │  │  │  │  ├─ intro_ball.gif
│  │     │  │  │  │  ├─ intro_blade.jpg
│  │     │  │  │  │  ├─ intro_freedom.jpg
│  │     │  │  │  │  ├─ joystick_calls.png
│  │     │  │  │  │  ├─ pygame_lofi.png
│  │     │  │  │  │  ├─ pygame_logo.png
│  │     │  │  │  │  ├─ pygame_powered.png
│  │     │  │  │  │  ├─ pygame_powered_lowres.png
│  │     │  │  │  │  ├─ pygame_tiny.png
│  │     │  │  │  │  ├─ surfarray_allblack.png
│  │     │  │  │  │  ├─ surfarray_flipped.png
│  │     │  │  │  │  ├─ surfarray_redimg.png
│  │     │  │  │  │  ├─ surfarray_rgbarray.png
│  │     │  │  │  │  ├─ surfarray_scaledown.png
│  │     │  │  │  │  ├─ surfarray_scaleup.png
│  │     │  │  │  │  ├─ surfarray_soften.png
│  │     │  │  │  │  ├─ surfarray_striped.png
│  │     │  │  │  │  ├─ surfarray_xfade.png
│  │     │  │  │  │  ├─ tom_basic.png
│  │     │  │  │  │  ├─ tom_event-flowchart.png
│  │     │  │  │  │  ├─ tom_formulae.png
│  │     │  │  │  │  └─ tom_radians.png
│  │     │  │  │  ├─ _sources
│  │     │  │  │  │  ├─ c_api.rst.txt
│  │     │  │  │  │  ├─ filepaths.rst.txt
│  │     │  │  │  │  ├─ index.rst.txt
│  │     │  │  │  │  ├─ logos.rst.txt
│  │     │  │  │  │  └─ ref
│  │     │  │  │  │     ├─ bufferproxy.rst.txt
│  │     │  │  │  │     ├─ camera.rst.txt
│  │     │  │  │  │     ├─ cdrom.rst.txt
│  │     │  │  │  │     ├─ color.rst.txt
│  │     │  │  │  │     ├─ color_list.rst.txt
│  │     │  │  │  │     ├─ cursors.rst.txt
│  │     │  │  │  │     ├─ display.rst.txt
│  │     │  │  │  │     ├─ draw.rst.txt
│  │     │  │  │  │     ├─ event.rst.txt
│  │     │  │  │  │     ├─ examples.rst.txt
│  │     │  │  │  │     ├─ fastevent.rst.txt
│  │     │  │  │  │     ├─ font.rst.txt
│  │     │  │  │  │     ├─ freetype.rst.txt
│  │     │  │  │  │     ├─ gfxdraw.rst.txt
│  │     │  │  │  │     ├─ image.rst.txt
│  │     │  │  │  │     ├─ joystick.rst.txt
│  │     │  │  │  │     ├─ key.rst.txt
│  │     │  │  │  │     ├─ locals.rst.txt
│  │     │  │  │  │     ├─ mask.rst.txt
│  │     │  │  │  │     ├─ math.rst.txt
│  │     │  │  │  │     ├─ midi.rst.txt
│  │     │  │  │  │     ├─ mixer.rst.txt
│  │     │  │  │  │     ├─ mouse.rst.txt
│  │     │  │  │  │     ├─ music.rst.txt
│  │     │  │  │  │     ├─ overlay.rst.txt
│  │     │  │  │  │     ├─ pixelarray.rst.txt
│  │     │  │  │  │     ├─ pixelcopy.rst.txt
│  │     │  │  │  │     ├─ pygame.rst.txt
│  │     │  │  │  │     ├─ rect.rst.txt
│  │     │  │  │  │     ├─ scrap.rst.txt
│  │     │  │  │  │     ├─ sdl2_controller.rst.txt
│  │     │  │  │  │     ├─ sdl2_video.rst.txt
│  │     │  │  │  │     ├─ sndarray.rst.txt
│  │     │  │  │  │     ├─ sprite.rst.txt
│  │     │  │  │  │     ├─ surface.rst.txt
│  │     │  │  │  │     ├─ surfarray.rst.txt
│  │     │  │  │  │     ├─ tests.rst.txt
│  │     │  │  │  │     ├─ time.rst.txt
│  │     │  │  │  │     ├─ touch.rst.txt
│  │     │  │  │  │     └─ transform.rst.txt
│  │     │  │  │  └─ _static
│  │     │  │  │     ├─ basic.css
│  │     │  │  │     ├─ doctools.js
│  │     │  │  │     ├─ documentation_options.js
│  │     │  │  │     ├─ file.png
│  │     │  │  │     ├─ language_data.js
│  │     │  │  │     ├─ legacy_logos.zip
│  │     │  │  │     ├─ minus.png
│  │     │  │  │     ├─ plus.png
│  │     │  │  │     ├─ pygame.css
│  │     │  │  │     ├─ pygame.ico
│  │     │  │  │     ├─ pygame_lofi.png
│  │     │  │  │     ├─ pygame_lofi.svg
│  │     │  │  │     ├─ pygame_logo.png
│  │     │  │  │     ├─ pygame_logo.svg
│  │     │  │  │     ├─ pygame_powered.png
│  │     │  │  │     ├─ pygame_powered.svg
│  │     │  │  │     ├─ pygame_powered_lowres.png
│  │     │  │  │     ├─ pygame_tiny.png
│  │     │  │  │     ├─ pygments.css
│  │     │  │  │     ├─ reset.css
│  │     │  │  │     ├─ searchtools.js
│  │     │  │  │     ├─ sphinx_highlight.js
│  │     │  │  │     └─ tooltip.css
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __main__.cpython-311.pyc
│  │     │  ├─ draw.cp311-win_amd64.pyd
│  │     │  ├─ draw.pyi
│  │     │  ├─ draw_py.py
│  │     │  ├─ event.cp311-win_amd64.pyd
│  │     │  ├─ event.pyi
│  │     │  ├─ examples
│  │     │  │  ├─ aacircle.py
│  │     │  │  ├─ aliens.py
│  │     │  │  ├─ arraydemo.py
│  │     │  │  ├─ audiocapture.py
│  │     │  │  ├─ blend_fill.py
│  │     │  │  ├─ blit_blends.py
│  │     │  │  ├─ camera.py
│  │     │  │  ├─ chimp.py
│  │     │  │  ├─ cursors.py
│  │     │  │  ├─ data
│  │     │  │  │  ├─ alien1.gif
│  │     │  │  │  ├─ alien1.jpg
│  │     │  │  │  ├─ alien1.png
│  │     │  │  │  ├─ alien2.gif
│  │     │  │  │  ├─ alien2.png
│  │     │  │  │  ├─ alien3.gif
│  │     │  │  │  ├─ alien3.png
│  │     │  │  │  ├─ arraydemo.bmp
│  │     │  │  │  ├─ asprite.bmp
│  │     │  │  │  ├─ background.gif
│  │     │  │  │  ├─ BGR.png
│  │     │  │  │  ├─ black.ppm
│  │     │  │  │  ├─ blue.gif
│  │     │  │  │  ├─ blue.mpg
│  │     │  │  │  ├─ bomb.gif
│  │     │  │  │  ├─ boom.wav
│  │     │  │  │  ├─ brick.png
│  │     │  │  │  ├─ car_door.wav
│  │     │  │  │  ├─ chimp.png
│  │     │  │  │  ├─ city.png
│  │     │  │  │  ├─ crimson.pnm
│  │     │  │  │  ├─ cursor.png
│  │     │  │  │  ├─ danger.gif
│  │     │  │  │  ├─ explosion1.gif
│  │     │  │  │  ├─ fist.png
│  │     │  │  │  ├─ green.pcx
│  │     │  │  │  ├─ grey.pgm
│  │     │  │  │  ├─ house_lo.mp3
│  │     │  │  │  ├─ house_lo.ogg
│  │     │  │  │  ├─ house_lo.wav
│  │     │  │  │  ├─ laplacian.png
│  │     │  │  │  ├─ liquid.bmp
│  │     │  │  │  ├─ midikeys.png
│  │     │  │  │  ├─ player1.gif
│  │     │  │  │  ├─ punch.wav
│  │     │  │  │  ├─ purple.xpm
│  │     │  │  │  ├─ red.jpg
│  │     │  │  │  ├─ sans.ttf
│  │     │  │  │  ├─ scarlet.webp
│  │     │  │  │  ├─ secosmic_lo.wav
│  │     │  │  │  ├─ shot.gif
│  │     │  │  │  ├─ static.png
│  │     │  │  │  ├─ teal.svg
│  │     │  │  │  ├─ turquoise.tif
│  │     │  │  │  ├─ whiff.wav
│  │     │  │  │  └─ yellow.tga
│  │     │  │  ├─ dropevent.py
│  │     │  │  ├─ eventlist.py
│  │     │  │  ├─ fonty.py
│  │     │  │  ├─ font_viewer.py
│  │     │  │  ├─ freetype_misc.py
│  │     │  │  ├─ glcube.py
│  │     │  │  ├─ go_over_there.py
│  │     │  │  ├─ grid.py
│  │     │  │  ├─ headless_no_windows_needed.py
│  │     │  │  ├─ joystick.py
│  │     │  │  ├─ liquid.py
│  │     │  │  ├─ mask.py
│  │     │  │  ├─ midi.py
│  │     │  │  ├─ moveit.py
│  │     │  │  ├─ music_drop_fade.py
│  │     │  │  ├─ pixelarray.py
│  │     │  │  ├─ playmus.py
│  │     │  │  ├─ README.rst
│  │     │  │  ├─ resizing_new.py
│  │     │  │  ├─ scaletest.py
│  │     │  │  ├─ scrap_clipboard.py
│  │     │  │  ├─ scroll.py
│  │     │  │  ├─ setmodescale.py
│  │     │  │  ├─ sound.py
│  │     │  │  ├─ sound_array_demos.py
│  │     │  │  ├─ sprite_texture.py
│  │     │  │  ├─ stars.py
│  │     │  │  ├─ testsprite.py
│  │     │  │  ├─ textinput.py
│  │     │  │  ├─ vgrade.py
│  │     │  │  ├─ video.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ aacircle.cpython-311.pyc
│  │     │  │     ├─ aliens.cpython-311.pyc
│  │     │  │     ├─ arraydemo.cpython-311.pyc
│  │     │  │     ├─ audiocapture.cpython-311.pyc
│  │     │  │     ├─ blend_fill.cpython-311.pyc
│  │     │  │     ├─ blit_blends.cpython-311.pyc
│  │     │  │     ├─ camera.cpython-311.pyc
│  │     │  │     ├─ chimp.cpython-311.pyc
│  │     │  │     ├─ cursors.cpython-311.pyc
│  │     │  │     ├─ dropevent.cpython-311.pyc
│  │     │  │     ├─ eventlist.cpython-311.pyc
│  │     │  │     ├─ fonty.cpython-311.pyc
│  │     │  │     ├─ font_viewer.cpython-311.pyc
│  │     │  │     ├─ freetype_misc.cpython-311.pyc
│  │     │  │     ├─ glcube.cpython-311.pyc
│  │     │  │     ├─ go_over_there.cpython-311.pyc
│  │     │  │     ├─ grid.cpython-311.pyc
│  │     │  │     ├─ headless_no_windows_needed.cpython-311.pyc
│  │     │  │     ├─ joystick.cpython-311.pyc
│  │     │  │     ├─ liquid.cpython-311.pyc
│  │     │  │     ├─ mask.cpython-311.pyc
│  │     │  │     ├─ midi.cpython-311.pyc
│  │     │  │     ├─ moveit.cpython-311.pyc
│  │     │  │     ├─ music_drop_fade.cpython-311.pyc
│  │     │  │     ├─ pixelarray.cpython-311.pyc
│  │     │  │     ├─ playmus.cpython-311.pyc
│  │     │  │     ├─ resizing_new.cpython-311.pyc
│  │     │  │     ├─ scaletest.cpython-311.pyc
│  │     │  │     ├─ scrap_clipboard.cpython-311.pyc
│  │     │  │     ├─ scroll.cpython-311.pyc
│  │     │  │     ├─ setmodescale.cpython-311.pyc
│  │     │  │     ├─ sound.cpython-311.pyc
│  │     │  │     ├─ sound_array_demos.cpython-311.pyc
│  │     │  │     ├─ sprite_texture.cpython-311.pyc
│  │     │  │     ├─ stars.cpython-311.pyc
│  │     │  │     ├─ testsprite.cpython-311.pyc
│  │     │  │     ├─ textinput.cpython-311.pyc
│  │     │  │     ├─ vgrade.cpython-311.pyc
│  │     │  │     ├─ video.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ fastevent.py
│  │     │  ├─ fastevent.pyi
│  │     │  ├─ font.cp311-win_amd64.pyd
│  │     │  ├─ font.pyi
│  │     │  ├─ freesansbold.ttf
│  │     │  ├─ freetype.dll
│  │     │  ├─ freetype.py
│  │     │  ├─ freetype.pyi
│  │     │  ├─ ftfont.py
│  │     │  ├─ gfxdraw.cp311-win_amd64.pyd
│  │     │  ├─ gfxdraw.pyi
│  │     │  ├─ image.cp311-win_amd64.pyd
│  │     │  ├─ image.pyi
│  │     │  ├─ imageext.cp311-win_amd64.pyd
│  │     │  ├─ joystick.cp311-win_amd64.pyd
│  │     │  ├─ joystick.pyi
│  │     │  ├─ key.cp311-win_amd64.pyd
│  │     │  ├─ key.pyi
│  │     │  ├─ libjpeg-9.dll
│  │     │  ├─ libmodplug-1.dll
│  │     │  ├─ libogg-0.dll
│  │     │  ├─ libopus-0.dll
│  │     │  ├─ libopusfile-0.dll
│  │     │  ├─ libpng16-16.dll
│  │     │  ├─ libtiff-5.dll
│  │     │  ├─ libwebp-7.dll
│  │     │  ├─ locals.py
│  │     │  ├─ locals.pyi
│  │     │  ├─ macosx.py
│  │     │  ├─ mask.cp311-win_amd64.pyd
│  │     │  ├─ mask.pyi
│  │     │  ├─ math.cp311-win_amd64.pyd
│  │     │  ├─ math.pyi
│  │     │  ├─ midi.py
│  │     │  ├─ midi.pyi
│  │     │  ├─ mixer.cp311-win_amd64.pyd
│  │     │  ├─ mixer.pyi
│  │     │  ├─ mixer_music.cp311-win_amd64.pyd
│  │     │  ├─ mixer_music.pyi
│  │     │  ├─ mouse.cp311-win_amd64.pyd
│  │     │  ├─ mouse.pyi
│  │     │  ├─ newbuffer.cp311-win_amd64.pyd
│  │     │  ├─ pixelarray.cp311-win_amd64.pyd
│  │     │  ├─ pixelarray.pyi
│  │     │  ├─ pixelcopy.cp311-win_amd64.pyd
│  │     │  ├─ pixelcopy.pyi
│  │     │  ├─ pkgdata.py
│  │     │  ├─ portmidi.dll
│  │     │  ├─ py.typed
│  │     │  ├─ pygame.ico
│  │     │  ├─ pygame_icon.bmp
│  │     │  ├─ pygame_icon.icns
│  │     │  ├─ pygame_icon_mac.bmp
│  │     │  ├─ pypm.cp311-win_amd64.pyd
│  │     │  ├─ rect.cp311-win_amd64.pyd
│  │     │  ├─ rect.pyi
│  │     │  ├─ rwobject.cp311-win_amd64.pyd
│  │     │  ├─ rwobject.pyi
│  │     │  ├─ scrap.cp311-win_amd64.pyd
│  │     │  ├─ scrap.pyi
│  │     │  ├─ SDL2.dll
│  │     │  ├─ SDL2_image.dll
│  │     │  ├─ SDL2_mixer.dll
│  │     │  ├─ SDL2_ttf.dll
│  │     │  ├─ sndarray.py
│  │     │  ├─ sndarray.pyi
│  │     │  ├─ sprite.py
│  │     │  ├─ sprite.pyi
│  │     │  ├─ surface.cp311-win_amd64.pyd
│  │     │  ├─ surface.pyi
│  │     │  ├─ surfarray.py
│  │     │  ├─ surfarray.pyi
│  │     │  ├─ surflock.cp311-win_amd64.pyd
│  │     │  ├─ surflock.pyi
│  │     │  ├─ sysfont.py
│  │     │  ├─ tests
│  │     │  │  ├─ base_test.py
│  │     │  │  ├─ blit_test.py
│  │     │  │  ├─ bufferproxy_test.py
│  │     │  │  ├─ camera_test.py
│  │     │  │  ├─ color_test.py
│  │     │  │  ├─ constants_test.py
│  │     │  │  ├─ controller_test.py
│  │     │  │  ├─ cursors_test.py
│  │     │  │  ├─ display_test.py
│  │     │  │  ├─ docs_test.py
│  │     │  │  ├─ draw_test.py
│  │     │  │  ├─ event_test.py
│  │     │  │  ├─ fixtures
│  │     │  │  │  ├─ fonts
│  │     │  │  │  │  ├─ A_PyGameMono-8.png
│  │     │  │  │  │  ├─ PlayfairDisplaySemibold.ttf
│  │     │  │  │  │  ├─ PyGameMono-18-100dpi.bdf
│  │     │  │  │  │  ├─ PyGameMono-18-75dpi.bdf
│  │     │  │  │  │  ├─ PyGameMono-8.bdf
│  │     │  │  │  │  ├─ PyGameMono.otf
│  │     │  │  │  │  ├─ test_fixed.otf
│  │     │  │  │  │  ├─ test_sans.ttf
│  │     │  │  │  │  └─ u13079_PyGameMono-8.png
│  │     │  │  │  └─ xbm_cursors
│  │     │  │  │     ├─ white_sizing.xbm
│  │     │  │  │     └─ white_sizing_mask.xbm
│  │     │  │  ├─ font_test.py
│  │     │  │  ├─ freetype_tags.py
│  │     │  │  ├─ freetype_test.py
│  │     │  │  ├─ ftfont_tags.py
│  │     │  │  ├─ ftfont_test.py
│  │     │  │  ├─ gfxdraw_test.py
│  │     │  │  ├─ imageext_tags.py
│  │     │  │  ├─ imageext_test.py
│  │     │  │  ├─ image_tags.py
│  │     │  │  ├─ image_test.py
│  │     │  │  ├─ image__save_gl_surface_test.py
│  │     │  │  ├─ joystick_test.py
│  │     │  │  ├─ key_test.py
│  │     │  │  ├─ locals_test.py
│  │     │  │  ├─ mask_test.py
│  │     │  │  ├─ math_test.py
│  │     │  │  ├─ midi_test.py
│  │     │  │  ├─ mixer_music_tags.py
│  │     │  │  ├─ mixer_music_test.py
│  │     │  │  ├─ mixer_tags.py
│  │     │  │  ├─ mixer_test.py
│  │     │  │  ├─ mouse_test.py
│  │     │  │  ├─ pixelarray_test.py
│  │     │  │  ├─ pixelcopy_test.py
│  │     │  │  ├─ rect_test.py
│  │     │  │  ├─ run_tests__tests
│  │     │  │  │  ├─ all_ok
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ fake_5_test.py
│  │     │  │  │  │  ├─ fake_6_test.py
│  │     │  │  │  │  ├─ no_assertions__ret_code_of_1__test.py
│  │     │  │  │  │  ├─ zero_tests_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_5_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_6_test.cpython-311.pyc
│  │     │  │  │  │     ├─ no_assertions__ret_code_of_1__test.cpython-311.pyc
│  │     │  │  │  │     ├─ zero_tests_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ everything
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ incomplete_todo_test.py
│  │     │  │  │  │  ├─ magic_tag_test.py
│  │     │  │  │  │  ├─ sleep_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ incomplete_todo_test.cpython-311.pyc
│  │     │  │  │  │     ├─ magic_tag_test.cpython-311.pyc
│  │     │  │  │  │     ├─ sleep_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exclude
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ invisible_tag_test.py
│  │     │  │  │  │  ├─ magic_tag_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ invisible_tag_test.cpython-311.pyc
│  │     │  │  │  │     ├─ magic_tag_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ failures1
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ incomplete
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ incomplete_todo
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ infinite_loop
│  │     │  │  │  │  ├─ fake_1_test.py
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_1_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ print_stderr
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ print_stdout
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ run_tests__test.py
│  │     │  │  │  ├─ timeout
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ sleep_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ sleep_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ run_tests__test.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ rwobject_test.py
│  │     │  │  ├─ scrap_tags.py
│  │     │  │  ├─ scrap_test.py
│  │     │  │  ├─ sndarray_tags.py
│  │     │  │  ├─ sndarray_test.py
│  │     │  │  ├─ sprite_test.py
│  │     │  │  ├─ surface_test.py
│  │     │  │  ├─ surfarray_tags.py
│  │     │  │  ├─ surfarray_test.py
│  │     │  │  ├─ surflock_test.py
│  │     │  │  ├─ sysfont_test.py
│  │     │  │  ├─ test_utils
│  │     │  │  │  ├─ arrinter.py
│  │     │  │  │  ├─ async_sub.py
│  │     │  │  │  ├─ buftools.py
│  │     │  │  │  ├─ endian.py
│  │     │  │  │  ├─ png.py
│  │     │  │  │  ├─ run_tests.py
│  │     │  │  │  ├─ test_machinery.py
│  │     │  │  │  ├─ test_runner.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ arrinter.cpython-311.pyc
│  │     │  │  │     ├─ async_sub.cpython-311.pyc
│  │     │  │  │     ├─ buftools.cpython-311.pyc
│  │     │  │  │     ├─ endian.cpython-311.pyc
│  │     │  │  │     ├─ png.cpython-311.pyc
│  │     │  │  │     ├─ run_tests.cpython-311.pyc
│  │     │  │  │     ├─ test_machinery.cpython-311.pyc
│  │     │  │  │     ├─ test_runner.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ threads_test.py
│  │     │  │  ├─ time_test.py
│  │     │  │  ├─ touch_test.py
│  │     │  │  ├─ transform_test.py
│  │     │  │  ├─ version_test.py
│  │     │  │  ├─ video_test.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base_test.cpython-311.pyc
│  │     │  │     ├─ blit_test.cpython-311.pyc
│  │     │  │     ├─ bufferproxy_test.cpython-311.pyc
│  │     │  │     ├─ camera_test.cpython-311.pyc
│  │     │  │     ├─ color_test.cpython-311.pyc
│  │     │  │     ├─ constants_test.cpython-311.pyc
│  │     │  │     ├─ controller_test.cpython-311.pyc
│  │     │  │     ├─ cursors_test.cpython-311.pyc
│  │     │  │     ├─ display_test.cpython-311.pyc
│  │     │  │     ├─ docs_test.cpython-311.pyc
│  │     │  │     ├─ draw_test.cpython-311.pyc
│  │     │  │     ├─ event_test.cpython-311.pyc
│  │     │  │     ├─ font_test.cpython-311.pyc
│  │     │  │     ├─ freetype_tags.cpython-311.pyc
│  │     │  │     ├─ freetype_test.cpython-311.pyc
│  │     │  │     ├─ ftfont_tags.cpython-311.pyc
│  │     │  │     ├─ ftfont_test.cpython-311.pyc
│  │     │  │     ├─ gfxdraw_test.cpython-311.pyc
│  │     │  │     ├─ imageext_tags.cpython-311.pyc
│  │     │  │     ├─ imageext_test.cpython-311.pyc
│  │     │  │     ├─ image_tags.cpython-311.pyc
│  │     │  │     ├─ image_test.cpython-311.pyc
│  │     │  │     ├─ image__save_gl_surface_test.cpython-311.pyc
│  │     │  │     ├─ joystick_test.cpython-311.pyc
│  │     │  │     ├─ key_test.cpython-311.pyc
│  │     │  │     ├─ locals_test.cpython-311.pyc
│  │     │  │     ├─ mask_test.cpython-311.pyc
│  │     │  │     ├─ math_test.cpython-311.pyc
│  │     │  │     ├─ midi_test.cpython-311.pyc
│  │     │  │     ├─ mixer_music_tags.cpython-311.pyc
│  │     │  │     ├─ mixer_music_test.cpython-311.pyc
│  │     │  │     ├─ mixer_tags.cpython-311.pyc
│  │     │  │     ├─ mixer_test.cpython-311.pyc
│  │     │  │     ├─ mouse_test.cpython-311.pyc
│  │     │  │     ├─ pixelarray_test.cpython-311.pyc
│  │     │  │     ├─ pixelcopy_test.cpython-311.pyc
│  │     │  │     ├─ rect_test.cpython-311.pyc
│  │     │  │     ├─ rwobject_test.cpython-311.pyc
│  │     │  │     ├─ scrap_tags.cpython-311.pyc
│  │     │  │     ├─ scrap_test.cpython-311.pyc
│  │     │  │     ├─ sndarray_tags.cpython-311.pyc
│  │     │  │     ├─ sndarray_test.cpython-311.pyc
│  │     │  │     ├─ sprite_test.cpython-311.pyc
│  │     │  │     ├─ surface_test.cpython-311.pyc
│  │     │  │     ├─ surfarray_tags.cpython-311.pyc
│  │     │  │     ├─ surfarray_test.cpython-311.pyc
│  │     │  │     ├─ surflock_test.cpython-311.pyc
│  │     │  │     ├─ sysfont_test.cpython-311.pyc
│  │     │  │     ├─ threads_test.cpython-311.pyc
│  │     │  │     ├─ time_test.cpython-311.pyc
│  │     │  │     ├─ touch_test.cpython-311.pyc
│  │     │  │     ├─ transform_test.cpython-311.pyc
│  │     │  │     ├─ version_test.cpython-311.pyc
│  │     │  │     ├─ video_test.cpython-311.pyc
│  │     │  │     ├─ __init__.cpython-311.pyc
│  │     │  │     └─ __main__.cpython-311.pyc
│  │     │  ├─ threads
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ time.cp311-win_amd64.pyd
│  │     │  ├─ time.pyi
│  │     │  ├─ transform.cp311-win_amd64.pyd
│  │     │  ├─ transform.pyi
│  │     │  ├─ version.py
│  │     │  ├─ version.pyi
│  │     │  ├─ zlib1.dll
│  │     │  ├─ _camera.cp311-win_amd64.pyd
│  │     │  ├─ _camera_opencv.py
│  │     │  ├─ _camera_vidcapture.py
│  │     │  ├─ _common.pyi
│  │     │  ├─ _freetype.cp311-win_amd64.pyd
│  │     │  ├─ _sdl2
│  │     │  │  ├─ audio.cp311-win_amd64.pyd
│  │     │  │  ├─ audio.pyi
│  │     │  │  ├─ controller.cp311-win_amd64.pyd
│  │     │  │  ├─ controller.pyi
│  │     │  │  ├─ mixer.cp311-win_amd64.pyd
│  │     │  │  ├─ sdl2.cp311-win_amd64.pyd
│  │     │  │  ├─ sdl2.pyi
│  │     │  │  ├─ touch.cp311-win_amd64.pyd
│  │     │  │  ├─ touch.pyi
│  │     │  │  ├─ video.cp311-win_amd64.pyd
│  │     │  │  ├─ video.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _sprite.cp311-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  ├─ __pycache__
│  │     │  │  ├─ camera.cpython-311.pyc
│  │     │  │  ├─ colordict.cpython-311.pyc
│  │     │  │  ├─ cursors.cpython-311.pyc
│  │     │  │  ├─ draw_py.cpython-311.pyc
│  │     │  │  ├─ fastevent.cpython-311.pyc
│  │     │  │  ├─ freetype.cpython-311.pyc
│  │     │  │  ├─ ftfont.cpython-311.pyc
│  │     │  │  ├─ locals.cpython-311.pyc
│  │     │  │  ├─ macosx.cpython-311.pyc
│  │     │  │  ├─ midi.cpython-311.pyc
│  │     │  │  ├─ pkgdata.cpython-311.pyc
│  │     │  │  ├─ sndarray.cpython-311.pyc
│  │     │  │  ├─ sprite.cpython-311.pyc
│  │     │  │  ├─ surfarray.cpython-311.pyc
│  │     │  │  ├─ sysfont.cpython-311.pyc
│  │     │  │  ├─ version.cpython-311.pyc
│  │     │  │  ├─ _camera_opencv.cpython-311.pyc
│  │     │  │  ├─ _camera_vidcapture.cpython-311.pyc
│  │     │  │  └─ __init__.cpython-311.pyc
│  │     │  └─ __pyinstaller
│  │     │     ├─ hook-pygame.py
│  │     │     ├─ __init__.py
│  │     │     └─ __pycache__
│  │     │        ├─ hook-pygame.cpython-311.pyc
│  │     │        └─ __init__.cpython-311.pyc
│  │     ├─ pygame-2.6.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pytokens
│  │     │  ├─ cli.py
│  │     │  ├─ py.typed
│  │     │  ├─ _mypyc_dummy.cp311-win_amd64.pyd
│  │     │  ├─ _mypyc_dummy.py
│  │     │  ├─ __init__.cp311-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cli.cpython-311.pyc
│  │     │     ├─ _mypyc_dummy.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ pytokens-0.4.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ setuptools
│  │     │  ├─ archive_util.py
│  │     │  ├─ build_meta.py
│  │     │  ├─ cli-32.exe
│  │     │  ├─ cli-64.exe
│  │     │  ├─ cli-arm64.exe
│  │     │  ├─ cli.exe
│  │     │  ├─ command
│  │     │  │  ├─ alias.py
│  │     │  │  ├─ bdist_egg.py
│  │     │  │  ├─ bdist_rpm.py
│  │     │  │  ├─ build.py
│  │     │  │  ├─ build_clib.py
│  │     │  │  ├─ build_ext.py
│  │     │  │  ├─ build_py.py
│  │     │  │  ├─ develop.py
│  │     │  │  ├─ dist_info.py
│  │     │  │  ├─ easy_install.py
│  │     │  │  ├─ editable_wheel.py
│  │     │  │  ├─ egg_info.py
│  │     │  │  ├─ install.py
│  │     │  │  ├─ install_egg_info.py
│  │     │  │  ├─ install_lib.py
│  │     │  │  ├─ install_scripts.py
│  │     │  │  ├─ launcher manifest.xml
│  │     │  │  ├─ py36compat.py
│  │     │  │  ├─ register.py
│  │     │  │  ├─ rotate.py
│  │     │  │  ├─ saveopts.py
│  │     │  │  ├─ sdist.py
│  │     │  │  ├─ setopt.py
│  │     │  │  ├─ test.py
│  │     │  │  ├─ upload.py
│  │     │  │  ├─ upload_docs.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ alias.cpython-311.pyc
│  │     │  │     ├─ bdist_egg.cpython-311.pyc
│  │     │  │     ├─ bdist_rpm.cpython-311.pyc
│  │     │  │     ├─ build.cpython-311.pyc
│  │     │  │     ├─ build_clib.cpython-311.pyc
│  │     │  │     ├─ build_ext.cpython-311.pyc
│  │     │  │     ├─ build_py.cpython-311.pyc
│  │     │  │     ├─ develop.cpython-311.pyc
│  │     │  │     ├─ dist_info.cpython-311.pyc
│  │     │  │     ├─ easy_install.cpython-311.pyc
│  │     │  │     ├─ editable_wheel.cpython-311.pyc
│  │     │  │     ├─ egg_info.cpython-311.pyc
│  │     │  │     ├─ install.cpython-311.pyc
│  │     │  │     ├─ install_egg_info.cpython-311.pyc
│  │     │  │     ├─ install_lib.cpython-311.pyc
│  │     │  │     ├─ install_scripts.cpython-311.pyc
│  │     │  │     ├─ py36compat.cpython-311.pyc
│  │     │  │     ├─ register.cpython-311.pyc
│  │     │  │     ├─ rotate.cpython-311.pyc
│  │     │  │     ├─ saveopts.cpython-311.pyc
│  │     │  │     ├─ sdist.cpython-311.pyc
│  │     │  │     ├─ setopt.cpython-311.pyc
│  │     │  │     ├─ test.cpython-311.pyc
│  │     │  │     ├─ upload.cpython-311.pyc
│  │     │  │     ├─ upload_docs.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ config
│  │     │  │  ├─ expand.py
│  │     │  │  ├─ pyprojecttoml.py
│  │     │  │  ├─ setupcfg.py
│  │     │  │  ├─ _apply_pyprojecttoml.py
│  │     │  │  ├─ _validate_pyproject
│  │     │  │  │  ├─ error_reporting.py
│  │     │  │  │  ├─ extra_validations.py
│  │     │  │  │  ├─ fastjsonschema_exceptions.py
│  │     │  │  │  ├─ fastjsonschema_validations.py
│  │     │  │  │  ├─ formats.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ error_reporting.cpython-311.pyc
│  │     │  │  │     ├─ extra_validations.cpython-311.pyc
│  │     │  │  │     ├─ fastjsonschema_exceptions.cpython-311.pyc
│  │     │  │  │     ├─ fastjsonschema_validations.cpython-311.pyc
│  │     │  │  │     ├─ formats.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ expand.cpython-311.pyc
│  │     │  │     ├─ pyprojecttoml.cpython-311.pyc
│  │     │  │     ├─ setupcfg.cpython-311.pyc
│  │     │  │     ├─ _apply_pyprojecttoml.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ depends.py
│  │     │  ├─ dep_util.py
│  │     │  ├─ discovery.py
│  │     │  ├─ dist.py
│  │     │  ├─ errors.py
│  │     │  ├─ extension.py
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ glob.py
│  │     │  ├─ gui-32.exe
│  │     │  ├─ gui-64.exe
│  │     │  ├─ gui-arm64.exe
│  │     │  ├─ gui.exe
│  │     │  ├─ installer.py
│  │     │  ├─ launch.py
│  │     │  ├─ logging.py
│  │     │  ├─ monkey.py
│  │     │  ├─ msvc.py
│  │     │  ├─ namespaces.py
│  │     │  ├─ package_index.py
│  │     │  ├─ py34compat.py
│  │     │  ├─ sandbox.py
│  │     │  ├─ script (dev).tmpl
│  │     │  ├─ script.tmpl
│  │     │  ├─ unicode_utils.py
│  │     │  ├─ version.py
│  │     │  ├─ wheel.py
│  │     │  ├─ windows_support.py
│  │     │  ├─ _deprecation_warning.py
│  │     │  ├─ _distutils
│  │     │  │  ├─ archive_util.py
│  │     │  │  ├─ bcppcompiler.py
│  │     │  │  ├─ ccompiler.py
│  │     │  │  ├─ cmd.py
│  │     │  │  ├─ command
│  │     │  │  │  ├─ bdist.py
│  │     │  │  │  ├─ bdist_dumb.py
│  │     │  │  │  ├─ bdist_rpm.py
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ build_clib.py
│  │     │  │  │  ├─ build_ext.py
│  │     │  │  │  ├─ build_py.py
│  │     │  │  │  ├─ build_scripts.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ clean.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ install_data.py
│  │     │  │  │  ├─ install_egg_info.py
│  │     │  │  │  ├─ install_headers.py
│  │     │  │  │  ├─ install_lib.py
│  │     │  │  │  ├─ install_scripts.py
│  │     │  │  │  ├─ py37compat.py
│  │     │  │  │  ├─ register.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ upload.py
│  │     │  │  │  ├─ _framework_compat.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bdist.cpython-311.pyc
│  │     │  │  │     ├─ bdist_dumb.cpython-311.pyc
│  │     │  │  │     ├─ bdist_rpm.cpython-311.pyc
│  │     │  │  │     ├─ build.cpython-311.pyc
│  │     │  │  │     ├─ build_clib.cpython-311.pyc
│  │     │  │  │     ├─ build_ext.cpython-311.pyc
│  │     │  │  │     ├─ build_py.cpython-311.pyc
│  │     │  │  │     ├─ build_scripts.cpython-311.pyc
│  │     │  │  │     ├─ check.cpython-311.pyc
│  │     │  │  │     ├─ clean.cpython-311.pyc
│  │     │  │  │     ├─ config.cpython-311.pyc
│  │     │  │  │     ├─ install.cpython-311.pyc
│  │     │  │  │     ├─ install_data.cpython-311.pyc
│  │     │  │  │     ├─ install_egg_info.cpython-311.pyc
│  │     │  │  │     ├─ install_headers.cpython-311.pyc
│  │     │  │  │     ├─ install_lib.cpython-311.pyc
│  │     │  │  │     ├─ install_scripts.cpython-311.pyc
│  │     │  │  │     ├─ py37compat.cpython-311.pyc
│  │     │  │  │     ├─ register.cpython-311.pyc
│  │     │  │  │     ├─ sdist.cpython-311.pyc
│  │     │  │  │     ├─ upload.cpython-311.pyc
│  │     │  │  │     ├─ _framework_compat.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ config.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ cygwinccompiler.py
│  │     │  │  ├─ debug.py
│  │     │  │  ├─ dep_util.py
│  │     │  │  ├─ dir_util.py
│  │     │  │  ├─ dist.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ extension.py
│  │     │  │  ├─ fancy_getopt.py
│  │     │  │  ├─ filelist.py
│  │     │  │  ├─ file_util.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ msvc9compiler.py
│  │     │  │  ├─ msvccompiler.py
│  │     │  │  ├─ py38compat.py
│  │     │  │  ├─ py39compat.py
│  │     │  │  ├─ spawn.py
│  │     │  │  ├─ sysconfig.py
│  │     │  │  ├─ text_file.py
│  │     │  │  ├─ unixccompiler.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ versionpredicate.py
│  │     │  │  ├─ _collections.py
│  │     │  │  ├─ _functools.py
│  │     │  │  ├─ _macos_compat.py
│  │     │  │  ├─ _msvccompiler.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ archive_util.cpython-311.pyc
│  │     │  │     ├─ bcppcompiler.cpython-311.pyc
│  │     │  │     ├─ ccompiler.cpython-311.pyc
│  │     │  │     ├─ cmd.cpython-311.pyc
│  │     │  │     ├─ config.cpython-311.pyc
│  │     │  │     ├─ core.cpython-311.pyc
│  │     │  │     ├─ cygwinccompiler.cpython-311.pyc
│  │     │  │     ├─ debug.cpython-311.pyc
│  │     │  │     ├─ dep_util.cpython-311.pyc
│  │     │  │     ├─ dir_util.cpython-311.pyc
│  │     │  │     ├─ dist.cpython-311.pyc
│  │     │  │     ├─ errors.cpython-311.pyc
│  │     │  │     ├─ extension.cpython-311.pyc
│  │     │  │     ├─ fancy_getopt.cpython-311.pyc
│  │     │  │     ├─ filelist.cpython-311.pyc
│  │     │  │     ├─ file_util.cpython-311.pyc
│  │     │  │     ├─ log.cpython-311.pyc
│  │     │  │     ├─ msvc9compiler.cpython-311.pyc
│  │     │  │     ├─ msvccompiler.cpython-311.pyc
│  │     │  │     ├─ py38compat.cpython-311.pyc
│  │     │  │     ├─ py39compat.cpython-311.pyc
│  │     │  │     ├─ spawn.cpython-311.pyc
│  │     │  │     ├─ sysconfig.cpython-311.pyc
│  │     │  │     ├─ text_file.cpython-311.pyc
│  │     │  │     ├─ unixccompiler.cpython-311.pyc
│  │     │  │     ├─ util.cpython-311.pyc
│  │     │  │     ├─ version.cpython-311.pyc
│  │     │  │     ├─ versionpredicate.cpython-311.pyc
│  │     │  │     ├─ _collections.cpython-311.pyc
│  │     │  │     ├─ _functools.cpython-311.pyc
│  │     │  │     ├─ _macos_compat.cpython-311.pyc
│  │     │  │     ├─ _msvccompiler.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _entry_points.py
│  │     │  ├─ _imp.py
│  │     │  ├─ _importlib.py
│  │     │  ├─ _itertools.py
│  │     │  ├─ _path.py
│  │     │  ├─ _reqs.py
│  │     │  ├─ _vendor
│  │     │  │  ├─ importlib_metadata
│  │     │  │  │  ├─ _adapters.py
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _functools.py
│  │     │  │  │  ├─ _itertools.py
│  │     │  │  │  ├─ _meta.py
│  │     │  │  │  ├─ _text.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _adapters.cpython-311.pyc
│  │     │  │  │     ├─ _collections.cpython-311.pyc
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _functools.cpython-311.pyc
│  │     │  │  │     ├─ _itertools.cpython-311.pyc
│  │     │  │  │     ├─ _meta.cpython-311.pyc
│  │     │  │  │     ├─ _text.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ importlib_resources
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ readers.py
│  │     │  │  │  ├─ simple.py
│  │     │  │  │  ├─ _adapters.py
│  │     │  │  │  ├─ _common.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _itertools.py
│  │     │  │  │  ├─ _legacy.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-311.pyc
│  │     │  │  │     ├─ readers.cpython-311.pyc
│  │     │  │  │     ├─ simple.cpython-311.pyc
│  │     │  │  │     ├─ _adapters.cpython-311.pyc
│  │     │  │  │     ├─ _common.cpython-311.pyc
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _itertools.cpython-311.pyc
│  │     │  │  │     ├─ _legacy.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ jaraco
│  │     │  │  │  ├─ context.py
│  │     │  │  │  ├─ functools.py
│  │     │  │  │  ├─ text
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ context.cpython-311.pyc
│  │     │  │  │     ├─ functools.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ more_itertools
│  │     │  │  │  ├─ more.py
│  │     │  │  │  ├─ recipes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ more.cpython-311.pyc
│  │     │  │  │     ├─ recipes.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ ordered_set.py
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │     ├─ specifiers.cpython-311.pyc
│  │     │  │  │     ├─ tags.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ _manylinux.cpython-311.pyc
│  │     │  │  │     ├─ _musllinux.cpython-311.pyc
│  │     │  │  │     ├─ _structures.cpython-311.pyc
│  │     │  │  │     ├─ __about__.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyparsing
│  │     │  │  │  ├─ actions.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ diagram
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ helpers.py
│  │     │  │  │  ├─ results.py
│  │     │  │  │  ├─ testing.py
│  │     │  │  │  ├─ unicode.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ actions.cpython-311.pyc
│  │     │  │  │     ├─ common.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ helpers.cpython-311.pyc
│  │     │  │  │     ├─ results.cpython-311.pyc
│  │     │  │  │     ├─ testing.cpython-311.pyc
│  │     │  │  │     ├─ unicode.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ tomli
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ _types.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _parser.cpython-311.pyc
│  │     │  │  │     ├─ _re.cpython-311.pyc
│  │     │  │  │     ├─ _types.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ typing_extensions.py
│  │     │  │  ├─ zipp.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ordered_set.cpython-311.pyc
│  │     │  │     ├─ typing_extensions.cpython-311.pyc
│  │     │  │     ├─ zipp.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ archive_util.cpython-311.pyc
│  │     │     ├─ build_meta.cpython-311.pyc
│  │     │     ├─ depends.cpython-311.pyc
│  │     │     ├─ dep_util.cpython-311.pyc
│  │     │     ├─ discovery.cpython-311.pyc
│  │     │     ├─ dist.cpython-311.pyc
│  │     │     ├─ errors.cpython-311.pyc
│  │     │     ├─ extension.cpython-311.pyc
│  │     │     ├─ glob.cpython-311.pyc
│  │     │     ├─ installer.cpython-311.pyc
│  │     │     ├─ launch.cpython-311.pyc
│  │     │     ├─ logging.cpython-311.pyc
│  │     │     ├─ monkey.cpython-311.pyc
│  │     │     ├─ msvc.cpython-311.pyc
│  │     │     ├─ namespaces.cpython-311.pyc
│  │     │     ├─ package_index.cpython-311.pyc
│  │     │     ├─ py34compat.cpython-311.pyc
│  │     │     ├─ sandbox.cpython-311.pyc
│  │     │     ├─ unicode_utils.cpython-311.pyc
│  │     │     ├─ version.cpython-311.pyc
│  │     │     ├─ wheel.cpython-311.pyc
│  │     │     ├─ windows_support.cpython-311.pyc
│  │     │     ├─ _deprecation_warning.cpython-311.pyc
│  │     │     ├─ _entry_points.cpython-311.pyc
│  │     │     ├─ _imp.cpython-311.pyc
│  │     │     ├─ _importlib.cpython-311.pyc
│  │     │     ├─ _itertools.cpython-311.pyc
│  │     │     ├─ _path.cpython-311.pyc
│  │     │     ├─ _reqs.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ setuptools-65.5.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ _black_version.py
│  │     ├─ _black_version.pyi
│  │     ├─ _distutils_hack
│  │     │  ├─ override.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ override.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     └─ __pycache__
│  │        ├─ mypy_extensions.cpython-311.pyc
│  │        └─ _black_version.cpython-311.pyc
│  ├─ pyvenv.cfg
│  └─ Scripts
│     ├─ activate
│     ├─ activate.bat
│     ├─ Activate.ps1
│     ├─ black.exe
│     ├─ blackd.exe
│     ├─ deactivate.bat
│     ├─ pip.exe
│     ├─ pip3.11.exe
│     ├─ pip3.exe
│     ├─ python.exe
│     └─ pythonw.exe
└─ __pycache__
   ├─ enemy.cpython-311.pyc
   ├─ game.cpython-311.pyc
   ├─ player.cpython-311.pyc
   └─ settings.cpython-311.pyc

```
```
game
├─ assets
│  ├─ images
│  │  ├─ background
│  │  │  └─ background.png
│  │  ├─ enemy
│  │  │  ├─ enemy_1.png
│  │  │  ├─ enemy_2.png
│  │  │  └─ enemy_3.png
│  │  └─ player
│  │     ├─ player_1.png
│  │     ├─ player_2.png
│  │     └─ player_3.png
│  └─ sounds
│     └─ music.mp3
├─ enemy.py
├─ game.py
├─ main.py
├─ player.py
├─ README.md
├─ settings.py
├─ venv
│  ├─ Include
│  │  └─ site
│  │     └─ python3.11
│  │        └─ pygame
│  │           ├─ camera.h
│  │           ├─ font.h
│  │           ├─ freetype.h
│  │           ├─ include
│  │           │  ├─ bitmask.h
│  │           │  ├─ pgcompat.h
│  │           │  ├─ pgimport.h
│  │           │  ├─ pgplatform.h
│  │           │  ├─ pygame.h
│  │           │  ├─ pygame_bufferproxy.h
│  │           │  ├─ pygame_font.h
│  │           │  ├─ pygame_freetype.h
│  │           │  ├─ pygame_mask.h
│  │           │  ├─ pygame_mixer.h
│  │           │  ├─ sse2neon.h
│  │           │  └─ _pygame.h
│  │           ├─ mask.h
│  │           ├─ mixer.h
│  │           ├─ palette.h
│  │           ├─ pgarrinter.h
│  │           ├─ pgbufferproxy.h
│  │           ├─ pgcompat.h
│  │           ├─ pgopengl.h
│  │           ├─ pgplatform.h
│  │           ├─ pygame.h
│  │           ├─ scrap.h
│  │           ├─ simd_blitters.h
│  │           ├─ surface.h
│  │           ├─ _blit_info.h
│  │           ├─ _camera.h
│  │           ├─ _pygame.h
│  │           └─ _surface.h
│  ├─ Lib
│  │  └─ site-packages
│  │     ├─ 30fcd23745efe32ce681__mypyc.cp311-win_amd64.pyd
│  │     ├─ black
│  │     │  ├─ brackets.cp311-win_amd64.pyd
│  │     │  ├─ brackets.py
│  │     │  ├─ cache.cp311-win_amd64.pyd
│  │     │  ├─ cache.py
│  │     │  ├─ comments.cp311-win_amd64.pyd
│  │     │  ├─ comments.py
│  │     │  ├─ concurrency.py
│  │     │  ├─ const.cp311-win_amd64.pyd
│  │     │  ├─ const.py
│  │     │  ├─ debug.py
│  │     │  ├─ files.py
│  │     │  ├─ handle_ipynb_magics.cp311-win_amd64.pyd
│  │     │  ├─ handle_ipynb_magics.py
│  │     │  ├─ linegen.cp311-win_amd64.pyd
│  │     │  ├─ linegen.py
│  │     │  ├─ lines.cp311-win_amd64.pyd
│  │     │  ├─ lines.py
│  │     │  ├─ mode.cp311-win_amd64.pyd
│  │     │  ├─ mode.py
│  │     │  ├─ nodes.cp311-win_amd64.pyd
│  │     │  ├─ nodes.py
│  │     │  ├─ numerics.cp311-win_amd64.pyd
│  │     │  ├─ numerics.py
│  │     │  ├─ output.py
│  │     │  ├─ parsing.cp311-win_amd64.pyd
│  │     │  ├─ parsing.py
│  │     │  ├─ py.typed
│  │     │  ├─ ranges.cp311-win_amd64.pyd
│  │     │  ├─ ranges.py
│  │     │  ├─ report.py
│  │     │  ├─ resources
│  │     │  │  ├─ black.schema.json
│  │     │  │  ├─ __init__.cp311-win_amd64.pyd
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ rusty.cp311-win_amd64.pyd
│  │     │  ├─ rusty.py
│  │     │  ├─ schema.cp311-win_amd64.pyd
│  │     │  ├─ schema.py
│  │     │  ├─ strings.cp311-win_amd64.pyd
│  │     │  ├─ strings.py
│  │     │  ├─ trans.cp311-win_amd64.pyd
│  │     │  ├─ trans.py
│  │     │  ├─ _width_table.cp311-win_amd64.pyd
│  │     │  ├─ _width_table.py
│  │     │  ├─ __init__.cp311-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ brackets.cpython-311.pyc
│  │     │     ├─ cache.cpython-311.pyc
│  │     │     ├─ comments.cpython-311.pyc
│  │     │     ├─ concurrency.cpython-311.pyc
│  │     │     ├─ const.cpython-311.pyc
│  │     │     ├─ debug.cpython-311.pyc
│  │     │     ├─ files.cpython-311.pyc
│  │     │     ├─ handle_ipynb_magics.cpython-311.pyc
│  │     │     ├─ linegen.cpython-311.pyc
│  │     │     ├─ lines.cpython-311.pyc
│  │     │     ├─ mode.cpython-311.pyc
│  │     │     ├─ nodes.cpython-311.pyc
│  │     │     ├─ numerics.cpython-311.pyc
│  │     │     ├─ output.cpython-311.pyc
│  │     │     ├─ parsing.cpython-311.pyc
│  │     │     ├─ ranges.cpython-311.pyc
│  │     │     ├─ report.cpython-311.pyc
│  │     │     ├─ rusty.cpython-311.pyc
│  │     │     ├─ schema.cpython-311.pyc
│  │     │     ├─ strings.cpython-311.pyc
│  │     │     ├─ trans.cpython-311.pyc
│  │     │     ├─ _width_table.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ black-26.5.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ blackd
│  │     │  ├─ client.py
│  │     │  ├─ middlewares.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ client.cpython-311.pyc
│  │     │     ├─ middlewares.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ blib2to3
│  │     │  ├─ Grammar.txt
│  │     │  ├─ LICENSE
│  │     │  ├─ PatternGrammar.txt
│  │     │  ├─ pgen2
│  │     │  │  ├─ conv.cp311-win_amd64.pyd
│  │     │  │  ├─ conv.py
│  │     │  │  ├─ driver.cp311-win_amd64.pyd
│  │     │  │  ├─ driver.py
│  │     │  │  ├─ grammar.cp311-win_amd64.pyd
│  │     │  │  ├─ grammar.py
│  │     │  │  ├─ literals.cp311-win_amd64.pyd
│  │     │  │  ├─ literals.py
│  │     │  │  ├─ parse.cp311-win_amd64.pyd
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ pgen.cp311-win_amd64.pyd
│  │     │  │  ├─ pgen.py
│  │     │  │  ├─ token.cp311-win_amd64.pyd
│  │     │  │  ├─ token.py
│  │     │  │  ├─ tokenize.cp311-win_amd64.pyd
│  │     │  │  ├─ tokenize.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ conv.cpython-311.pyc
│  │     │  │     ├─ driver.cpython-311.pyc
│  │     │  │     ├─ grammar.cpython-311.pyc
│  │     │  │     ├─ literals.cpython-311.pyc
│  │     │  │     ├─ parse.cpython-311.pyc
│  │     │  │     ├─ pgen.cpython-311.pyc
│  │     │  │     ├─ token.cpython-311.pyc
│  │     │  │     ├─ tokenize.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ pygram.cp311-win_amd64.pyd
│  │     │  ├─ pygram.py
│  │     │  ├─ pytree.cp311-win_amd64.pyd
│  │     │  ├─ pytree.py
│  │     │  ├─ README
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ pygram.cpython-311.pyc
│  │     │     ├─ pytree.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ click
│  │     │  ├─ core.py
│  │     │  ├─ decorators.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formatting.py
│  │     │  ├─ globals.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ shell_completion.py
│  │     │  ├─ termui.py
│  │     │  ├─ testing.py
│  │     │  ├─ types.py
│  │     │  ├─ utils.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _termui_impl.py
│  │     │  ├─ _textwrap.py
│  │     │  ├─ _utils.py
│  │     │  ├─ _winconsole.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ core.cpython-311.pyc
│  │     │     ├─ decorators.cpython-311.pyc
│  │     │     ├─ exceptions.cpython-311.pyc
│  │     │     ├─ formatting.cpython-311.pyc
│  │     │     ├─ globals.cpython-311.pyc
│  │     │     ├─ parser.cpython-311.pyc
│  │     │     ├─ shell_completion.cpython-311.pyc
│  │     │     ├─ termui.cpython-311.pyc
│  │     │     ├─ testing.cpython-311.pyc
│  │     │     ├─ types.cpython-311.pyc
│  │     │     ├─ utils.cpython-311.pyc
│  │     │     ├─ _compat.cpython-311.pyc
│  │     │     ├─ _termui_impl.cpython-311.pyc
│  │     │     ├─ _textwrap.cpython-311.pyc
│  │     │     ├─ _utils.cpython-311.pyc
│  │     │     ├─ _winconsole.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ click-8.4.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ colorama
│  │     │  ├─ ansi.py
│  │     │  ├─ ansitowin32.py
│  │     │  ├─ initialise.py
│  │     │  ├─ tests
│  │     │  │  ├─ ansitowin32_test.py
│  │     │  │  ├─ ansi_test.py
│  │     │  │  ├─ initialise_test.py
│  │     │  │  ├─ isatty_test.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ winterm_test.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ansitowin32_test.cpython-311.pyc
│  │     │  │     ├─ ansi_test.cpython-311.pyc
│  │     │  │     ├─ initialise_test.cpython-311.pyc
│  │     │  │     ├─ isatty_test.cpython-311.pyc
│  │     │  │     ├─ utils.cpython-311.pyc
│  │     │  │     ├─ winterm_test.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ win32.py
│  │     │  ├─ winterm.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ ansi.cpython-311.pyc
│  │     │     ├─ ansitowin32.cpython-311.pyc
│  │     │     ├─ initialise.cpython-311.pyc
│  │     │     ├─ win32.cpython-311.pyc
│  │     │     ├─ winterm.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ colorama-0.4.6.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ distutils-precedence.pth
│  │     ├─ fd7dcdb10166ebd4db98__mypyc.cp311-win_amd64.pyd
│  │     ├─ mypy_extensions-1.1.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ mypy_extensions.py
│  │     ├─ packaging
│  │     │  ├─ dependency_groups.py
│  │     │  ├─ direct_url.py
│  │     │  ├─ errors.py
│  │     │  ├─ licenses
│  │     │  │  ├─ _spdx.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ _spdx.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ markers.py
│  │     │  ├─ metadata.py
│  │     │  ├─ py.typed
│  │     │  ├─ pylock.py
│  │     │  ├─ requirements.py
│  │     │  ├─ specifiers.py
│  │     │  ├─ tags.py
│  │     │  ├─ utils.py
│  │     │  ├─ version.py
│  │     │  ├─ _elffile.py
│  │     │  ├─ _manylinux.py
│  │     │  ├─ _musllinux.py
│  │     │  ├─ _parser.py
│  │     │  ├─ _structures.py
│  │     │  ├─ _tokenizer.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ dependency_groups.cpython-311.pyc
│  │     │     ├─ direct_url.cpython-311.pyc
│  │     │     ├─ errors.cpython-311.pyc
│  │     │     ├─ markers.cpython-311.pyc
│  │     │     ├─ metadata.cpython-311.pyc
│  │     │     ├─ pylock.cpython-311.pyc
│  │     │     ├─ requirements.cpython-311.pyc
│  │     │     ├─ specifiers.cpython-311.pyc
│  │     │     ├─ tags.cpython-311.pyc
│  │     │     ├─ utils.cpython-311.pyc
│  │     │     ├─ version.cpython-311.pyc
│  │     │     ├─ _elffile.cpython-311.pyc
│  │     │     ├─ _manylinux.cpython-311.pyc
│  │     │     ├─ _musllinux.cpython-311.pyc
│  │     │     ├─ _parser.cpython-311.pyc
│  │     │     ├─ _structures.cpython-311.pyc
│  │     │     ├─ _tokenizer.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ packaging-26.2.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ LICENSE.APACHE
│  │     │  │  └─ LICENSE.BSD
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pathspec
│  │     │  ├─ backend.py
│  │     │  ├─ gitignore.py
│  │     │  ├─ pathspec.py
│  │     │  ├─ pattern.py
│  │     │  ├─ patterns
│  │     │  │  ├─ gitignore
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ basic.py
│  │     │  │  │  ├─ spec.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ basic.cpython-311.pyc
│  │     │  │  │     ├─ spec.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ gitwildmatch.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ gitwildmatch.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ py.typed
│  │     │  ├─ util.py
│  │     │  ├─ _backends
│  │     │  │  ├─ agg.py
│  │     │  │  ├─ hyperscan
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ gitignore.py
│  │     │  │  │  ├─ pathspec.py
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ gitignore.cpython-311.pyc
│  │     │  │  │     ├─ pathspec.cpython-311.pyc
│  │     │  │  │     ├─ _base.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ re2
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ gitignore.py
│  │     │  │  │  ├─ pathspec.py
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ gitignore.cpython-311.pyc
│  │     │  │  │     ├─ pathspec.cpython-311.pyc
│  │     │  │  │     ├─ _base.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ simple
│  │     │  │  │  ├─ gitignore.py
│  │     │  │  │  ├─ pathspec.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ gitignore.cpython-311.pyc
│  │     │  │  │     ├─ pathspec.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ agg.cpython-311.pyc
│  │     │  │     ├─ _utils.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _meta.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _version.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ backend.cpython-311.pyc
│  │     │     ├─ gitignore.cpython-311.pyc
│  │     │     ├─ pathspec.cpython-311.pyc
│  │     │     ├─ pattern.cpython-311.pyc
│  │     │     ├─ util.cpython-311.pyc
│  │     │     ├─ _meta.cpython-311.pyc
│  │     │     ├─ _typing.cpython-311.pyc
│  │     │     ├─ _version.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ pathspec-1.1.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pip
│  │     │  ├─ py.typed
│  │     │  ├─ _internal
│  │     │  │  ├─ build_env.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ cli
│  │     │  │  │  ├─ autocompletion.py
│  │     │  │  │  ├─ base_command.py
│  │     │  │  │  ├─ cmdoptions.py
│  │     │  │  │  ├─ command_context.py
│  │     │  │  │  ├─ main.py
│  │     │  │  │  ├─ main_parser.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ progress_bars.py
│  │     │  │  │  ├─ req_command.py
│  │     │  │  │  ├─ spinners.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ autocompletion.cpython-311.pyc
│  │     │  │  │     ├─ base_command.cpython-311.pyc
│  │     │  │  │     ├─ cmdoptions.cpython-311.pyc
│  │     │  │  │     ├─ command_context.cpython-311.pyc
│  │     │  │  │     ├─ main.cpython-311.pyc
│  │     │  │  │     ├─ main_parser.cpython-311.pyc
│  │     │  │  │     ├─ parser.cpython-311.pyc
│  │     │  │  │     ├─ progress_bars.cpython-311.pyc
│  │     │  │  │     ├─ req_command.cpython-311.pyc
│  │     │  │  │     ├─ spinners.cpython-311.pyc
│  │     │  │  │     ├─ status_codes.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ commands
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ configuration.py
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ hash.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ inspect.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ show.py
│  │     │  │  │  ├─ uninstall.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cache.cpython-311.pyc
│  │     │  │  │     ├─ check.cpython-311.pyc
│  │     │  │  │     ├─ completion.cpython-311.pyc
│  │     │  │  │     ├─ configuration.cpython-311.pyc
│  │     │  │  │     ├─ debug.cpython-311.pyc
│  │     │  │  │     ├─ download.cpython-311.pyc
│  │     │  │  │     ├─ freeze.cpython-311.pyc
│  │     │  │  │     ├─ hash.cpython-311.pyc
│  │     │  │  │     ├─ help.cpython-311.pyc
│  │     │  │  │     ├─ index.cpython-311.pyc
│  │     │  │  │     ├─ inspect.cpython-311.pyc
│  │     │  │  │     ├─ install.cpython-311.pyc
│  │     │  │  │     ├─ list.cpython-311.pyc
│  │     │  │  │     ├─ search.cpython-311.pyc
│  │     │  │  │     ├─ show.cpython-311.pyc
│  │     │  │  │     ├─ uninstall.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ configuration.py
│  │     │  │  ├─ distributions
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ installed.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ installed.cpython-311.pyc
│  │     │  │  │     ├─ sdist.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ index
│  │     │  │  │  ├─ collector.py
│  │     │  │  │  ├─ package_finder.py
│  │     │  │  │  ├─ sources.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ collector.cpython-311.pyc
│  │     │  │  │     ├─ package_finder.cpython-311.pyc
│  │     │  │  │     ├─ sources.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ locations
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _sysconfig.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ _distutils.cpython-311.pyc
│  │     │  │  │     ├─ _sysconfig.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ main.py
│  │     │  │  ├─ metadata
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ importlib
│  │     │  │  │  │  ├─ _compat.py
│  │     │  │  │  │  ├─ _dists.py
│  │     │  │  │  │  ├─ _envs.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │  │     ├─ _dists.cpython-311.pyc
│  │     │  │  │  │     ├─ _envs.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ pkg_resources.py
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     ├─ pkg_resources.cpython-311.pyc
│  │     │  │  │     ├─ _json.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ models
│  │     │  │  │  ├─ candidate.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ format_control.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ installation_report.py
│  │     │  │  │  ├─ link.py
│  │     │  │  │  ├─ scheme.py
│  │     │  │  │  ├─ search_scope.py
│  │     │  │  │  ├─ selection_prefs.py
│  │     │  │  │  ├─ target_python.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ candidate.cpython-311.pyc
│  │     │  │  │     ├─ direct_url.cpython-311.pyc
│  │     │  │  │     ├─ format_control.cpython-311.pyc
│  │     │  │  │     ├─ index.cpython-311.pyc
│  │     │  │  │     ├─ installation_report.cpython-311.pyc
│  │     │  │  │     ├─ link.cpython-311.pyc
│  │     │  │  │     ├─ scheme.cpython-311.pyc
│  │     │  │  │     ├─ search_scope.cpython-311.pyc
│  │     │  │  │     ├─ selection_prefs.cpython-311.pyc
│  │     │  │  │     ├─ target_python.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ network
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ lazy_wheel.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ xmlrpc.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ auth.cpython-311.pyc
│  │     │  │  │     ├─ cache.cpython-311.pyc
│  │     │  │  │     ├─ download.cpython-311.pyc
│  │     │  │  │     ├─ lazy_wheel.cpython-311.pyc
│  │     │  │  │     ├─ session.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ xmlrpc.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ operations
│  │     │  │  │  ├─ build
│  │     │  │  │  │  ├─ build_tracker.py
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ metadata_editable.py
│  │     │  │  │  │  ├─ metadata_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ wheel_editable.py
│  │     │  │  │  │  ├─ wheel_legacy.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ build_tracker.cpython-311.pyc
│  │     │  │  │  │     ├─ metadata.cpython-311.pyc
│  │     │  │  │  │     ├─ metadata_editable.cpython-311.pyc
│  │     │  │  │  │     ├─ metadata_legacy.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel_editable.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel_legacy.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ install
│  │     │  │  │  │  ├─ editable_legacy.py
│  │     │  │  │  │  ├─ wheel.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ editable_legacy.cpython-311.pyc
│  │     │  │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ prepare.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ check.cpython-311.pyc
│  │     │  │  │     ├─ freeze.cpython-311.pyc
│  │     │  │  │     ├─ prepare.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyproject.py
│  │     │  │  ├─ req
│  │     │  │  │  ├─ constructors.py
│  │     │  │  │  ├─ req_file.py
│  │     │  │  │  ├─ req_install.py
│  │     │  │  │  ├─ req_set.py
│  │     │  │  │  ├─ req_uninstall.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ constructors.cpython-311.pyc
│  │     │  │  │     ├─ req_file.cpython-311.pyc
│  │     │  │  │     ├─ req_install.cpython-311.pyc
│  │     │  │  │     ├─ req_set.cpython-311.pyc
│  │     │  │  │     ├─ req_uninstall.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ resolution
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ legacy
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ resolver.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ resolvelib
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ candidates.py
│  │     │  │  │  │  ├─ factory.py
│  │     │  │  │  │  ├─ found_candidates.py
│  │     │  │  │  │  ├─ provider.py
│  │     │  │  │  │  ├─ reporter.py
│  │     │  │  │  │  ├─ requirements.py
│  │     │  │  │  │  ├─ resolver.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │  │     ├─ candidates.cpython-311.pyc
│  │     │  │  │  │     ├─ factory.cpython-311.pyc
│  │     │  │  │  │     ├─ found_candidates.cpython-311.pyc
│  │     │  │  │  │     ├─ provider.cpython-311.pyc
│  │     │  │  │  │     ├─ reporter.cpython-311.pyc
│  │     │  │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │  │     ├─ resolver.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ base.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ self_outdated_check.py
│  │     │  │  ├─ utils
│  │     │  │  │  ├─ appdirs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ compatibility_tags.py
│  │     │  │  │  ├─ datetime.py
│  │     │  │  │  ├─ deprecation.py
│  │     │  │  │  ├─ direct_url_helpers.py
│  │     │  │  │  ├─ egg_link.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ entrypoints.py
│  │     │  │  │  ├─ filesystem.py
│  │     │  │  │  ├─ filetypes.py
│  │     │  │  │  ├─ glibc.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ setuptools_build.py
│  │     │  │  │  ├─ subprocess.py
│  │     │  │  │  ├─ temp_dir.py
│  │     │  │  │  ├─ unpacking.py
│  │     │  │  │  ├─ urls.py
│  │     │  │  │  ├─ virtualenv.py
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ _jaraco_text.py
│  │     │  │  │  ├─ _log.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ appdirs.cpython-311.pyc
│  │     │  │  │     ├─ compat.cpython-311.pyc
│  │     │  │  │     ├─ compatibility_tags.cpython-311.pyc
│  │     │  │  │     ├─ datetime.cpython-311.pyc
│  │     │  │  │     ├─ deprecation.cpython-311.pyc
│  │     │  │  │     ├─ direct_url_helpers.cpython-311.pyc
│  │     │  │  │     ├─ egg_link.cpython-311.pyc
│  │     │  │  │     ├─ encoding.cpython-311.pyc
│  │     │  │  │     ├─ entrypoints.cpython-311.pyc
│  │     │  │  │     ├─ filesystem.cpython-311.pyc
│  │     │  │  │     ├─ filetypes.cpython-311.pyc
│  │     │  │  │     ├─ glibc.cpython-311.pyc
│  │     │  │  │     ├─ hashes.cpython-311.pyc
│  │     │  │  │     ├─ logging.cpython-311.pyc
│  │     │  │  │     ├─ misc.cpython-311.pyc
│  │     │  │  │     ├─ models.cpython-311.pyc
│  │     │  │  │     ├─ packaging.cpython-311.pyc
│  │     │  │  │     ├─ setuptools_build.cpython-311.pyc
│  │     │  │  │     ├─ subprocess.cpython-311.pyc
│  │     │  │  │     ├─ temp_dir.cpython-311.pyc
│  │     │  │  │     ├─ unpacking.cpython-311.pyc
│  │     │  │  │     ├─ urls.cpython-311.pyc
│  │     │  │  │     ├─ virtualenv.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     ├─ _jaraco_text.cpython-311.pyc
│  │     │  │  │     ├─ _log.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ vcs
│  │     │  │  │  ├─ bazaar.py
│  │     │  │  │  ├─ git.py
│  │     │  │  │  ├─ mercurial.py
│  │     │  │  │  ├─ subversion.py
│  │     │  │  │  ├─ versioncontrol.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bazaar.cpython-311.pyc
│  │     │  │  │     ├─ git.cpython-311.pyc
│  │     │  │  │     ├─ mercurial.cpython-311.pyc
│  │     │  │  │     ├─ subversion.cpython-311.pyc
│  │     │  │  │     ├─ versioncontrol.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ wheel_builder.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ build_env.cpython-311.pyc
│  │     │  │     ├─ cache.cpython-311.pyc
│  │     │  │     ├─ configuration.cpython-311.pyc
│  │     │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │     ├─ main.cpython-311.pyc
│  │     │  │     ├─ pyproject.cpython-311.pyc
│  │     │  │     ├─ self_outdated_check.cpython-311.pyc
│  │     │  │     ├─ wheel_builder.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ cachecontrol
│  │     │  │  │  ├─ adapter.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ caches
│  │     │  │  │  │  ├─ file_cache.py
│  │     │  │  │  │  ├─ redis_cache.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ file_cache.cpython-311.pyc
│  │     │  │  │  │     ├─ redis_cache.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ controller.py
│  │     │  │  │  ├─ filewrapper.py
│  │     │  │  │  ├─ heuristics.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ serialize.py
│  │     │  │  │  ├─ wrapper.py
│  │     │  │  │  ├─ _cmd.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ adapter.cpython-311.pyc
│  │     │  │  │     ├─ cache.cpython-311.pyc
│  │     │  │  │     ├─ controller.cpython-311.pyc
│  │     │  │  │     ├─ filewrapper.cpython-311.pyc
│  │     │  │  │     ├─ heuristics.cpython-311.pyc
│  │     │  │  │     ├─ serialize.cpython-311.pyc
│  │     │  │  │     ├─ wrapper.cpython-311.pyc
│  │     │  │  │     ├─ _cmd.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ certifi
│  │     │  │  │  ├─ cacert.pem
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ chardet
│  │     │  │  │  ├─ big5freq.py
│  │     │  │  │  ├─ big5prober.py
│  │     │  │  │  ├─ chardistribution.py
│  │     │  │  │  ├─ charsetgroupprober.py
│  │     │  │  │  ├─ charsetprober.py
│  │     │  │  │  ├─ cli
│  │     │  │  │  │  ├─ chardetect.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ chardetect.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ codingstatemachine.py
│  │     │  │  │  ├─ codingstatemachinedict.py
│  │     │  │  │  ├─ cp949prober.py
│  │     │  │  │  ├─ enums.py
│  │     │  │  │  ├─ escprober.py
│  │     │  │  │  ├─ escsm.py
│  │     │  │  │  ├─ eucjpprober.py
│  │     │  │  │  ├─ euckrfreq.py
│  │     │  │  │  ├─ euckrprober.py
│  │     │  │  │  ├─ euctwfreq.py
│  │     │  │  │  ├─ euctwprober.py
│  │     │  │  │  ├─ gb2312freq.py
│  │     │  │  │  ├─ gb2312prober.py
│  │     │  │  │  ├─ hebrewprober.py
│  │     │  │  │  ├─ jisfreq.py
│  │     │  │  │  ├─ johabfreq.py
│  │     │  │  │  ├─ johabprober.py
│  │     │  │  │  ├─ jpcntx.py
│  │     │  │  │  ├─ langbulgarianmodel.py
│  │     │  │  │  ├─ langgreekmodel.py
│  │     │  │  │  ├─ langhebrewmodel.py
│  │     │  │  │  ├─ langhungarianmodel.py
│  │     │  │  │  ├─ langrussianmodel.py
│  │     │  │  │  ├─ langthaimodel.py
│  │     │  │  │  ├─ langturkishmodel.py
│  │     │  │  │  ├─ latin1prober.py
│  │     │  │  │  ├─ macromanprober.py
│  │     │  │  │  ├─ mbcharsetprober.py
│  │     │  │  │  ├─ mbcsgroupprober.py
│  │     │  │  │  ├─ mbcssm.py
│  │     │  │  │  ├─ metadata
│  │     │  │  │  │  ├─ languages.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ languages.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ resultdict.py
│  │     │  │  │  ├─ sbcharsetprober.py
│  │     │  │  │  ├─ sbcsgroupprober.py
│  │     │  │  │  ├─ sjisprober.py
│  │     │  │  │  ├─ universaldetector.py
│  │     │  │  │  ├─ utf1632prober.py
│  │     │  │  │  ├─ utf8prober.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ big5freq.cpython-311.pyc
│  │     │  │  │     ├─ big5prober.cpython-311.pyc
│  │     │  │  │     ├─ chardistribution.cpython-311.pyc
│  │     │  │  │     ├─ charsetgroupprober.cpython-311.pyc
│  │     │  │  │     ├─ charsetprober.cpython-311.pyc
│  │     │  │  │     ├─ codingstatemachine.cpython-311.pyc
│  │     │  │  │     ├─ codingstatemachinedict.cpython-311.pyc
│  │     │  │  │     ├─ cp949prober.cpython-311.pyc
│  │     │  │  │     ├─ enums.cpython-311.pyc
│  │     │  │  │     ├─ escprober.cpython-311.pyc
│  │     │  │  │     ├─ escsm.cpython-311.pyc
│  │     │  │  │     ├─ eucjpprober.cpython-311.pyc
│  │     │  │  │     ├─ euckrfreq.cpython-311.pyc
│  │     │  │  │     ├─ euckrprober.cpython-311.pyc
│  │     │  │  │     ├─ euctwfreq.cpython-311.pyc
│  │     │  │  │     ├─ euctwprober.cpython-311.pyc
│  │     │  │  │     ├─ gb2312freq.cpython-311.pyc
│  │     │  │  │     ├─ gb2312prober.cpython-311.pyc
│  │     │  │  │     ├─ hebrewprober.cpython-311.pyc
│  │     │  │  │     ├─ jisfreq.cpython-311.pyc
│  │     │  │  │     ├─ johabfreq.cpython-311.pyc
│  │     │  │  │     ├─ johabprober.cpython-311.pyc
│  │     │  │  │     ├─ jpcntx.cpython-311.pyc
│  │     │  │  │     ├─ langbulgarianmodel.cpython-311.pyc
│  │     │  │  │     ├─ langgreekmodel.cpython-311.pyc
│  │     │  │  │     ├─ langhebrewmodel.cpython-311.pyc
│  │     │  │  │     ├─ langhungarianmodel.cpython-311.pyc
│  │     │  │  │     ├─ langrussianmodel.cpython-311.pyc
│  │     │  │  │     ├─ langthaimodel.cpython-311.pyc
│  │     │  │  │     ├─ langturkishmodel.cpython-311.pyc
│  │     │  │  │     ├─ latin1prober.cpython-311.pyc
│  │     │  │  │     ├─ macromanprober.cpython-311.pyc
│  │     │  │  │     ├─ mbcharsetprober.cpython-311.pyc
│  │     │  │  │     ├─ mbcsgroupprober.cpython-311.pyc
│  │     │  │  │     ├─ mbcssm.cpython-311.pyc
│  │     │  │  │     ├─ resultdict.cpython-311.pyc
│  │     │  │  │     ├─ sbcharsetprober.cpython-311.pyc
│  │     │  │  │     ├─ sbcsgroupprober.cpython-311.pyc
│  │     │  │  │     ├─ sjisprober.cpython-311.pyc
│  │     │  │  │     ├─ universaldetector.cpython-311.pyc
│  │     │  │  │     ├─ utf1632prober.cpython-311.pyc
│  │     │  │  │     ├─ utf8prober.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ colorama
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ ansitowin32.py
│  │     │  │  │  ├─ initialise.py
│  │     │  │  │  ├─ tests
│  │     │  │  │  │  ├─ ansitowin32_test.py
│  │     │  │  │  │  ├─ ansi_test.py
│  │     │  │  │  │  ├─ initialise_test.py
│  │     │  │  │  │  ├─ isatty_test.py
│  │     │  │  │  │  ├─ utils.py
│  │     │  │  │  │  ├─ winterm_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ ansitowin32_test.cpython-311.pyc
│  │     │  │  │  │     ├─ ansi_test.cpython-311.pyc
│  │     │  │  │  │     ├─ initialise_test.cpython-311.pyc
│  │     │  │  │  │     ├─ isatty_test.cpython-311.pyc
│  │     │  │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │  │     ├─ winterm_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ win32.py
│  │     │  │  │  ├─ winterm.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ ansi.cpython-311.pyc
│  │     │  │  │     ├─ ansitowin32.cpython-311.pyc
│  │     │  │  │     ├─ initialise.cpython-311.pyc
│  │     │  │  │     ├─ win32.cpython-311.pyc
│  │     │  │  │     ├─ winterm.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ distlib
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ database.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ locators.py
│  │     │  │  │  ├─ manifest.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ resources.py
│  │     │  │  │  ├─ scripts.py
│  │     │  │  │  ├─ t32.exe
│  │     │  │  │  ├─ t64-arm.exe
│  │     │  │  │  ├─ t64.exe
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ w32.exe
│  │     │  │  │  ├─ w64-arm.exe
│  │     │  │  │  ├─ w64.exe
│  │     │  │  │  ├─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ compat.cpython-311.pyc
│  │     │  │  │     ├─ database.cpython-311.pyc
│  │     │  │  │     ├─ index.cpython-311.pyc
│  │     │  │  │     ├─ locators.cpython-311.pyc
│  │     │  │  │     ├─ manifest.cpython-311.pyc
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ metadata.cpython-311.pyc
│  │     │  │  │     ├─ resources.cpython-311.pyc
│  │     │  │  │     ├─ scripts.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ wheel.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ distro
│  │     │  │  │  ├─ distro.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ distro.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ idna
│  │     │  │  │  ├─ codec.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ idnadata.py
│  │     │  │  │  ├─ intranges.py
│  │     │  │  │  ├─ package_data.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ uts46data.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ codec.cpython-311.pyc
│  │     │  │  │     ├─ compat.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ idnadata.cpython-311.pyc
│  │     │  │  │     ├─ intranges.cpython-311.pyc
│  │     │  │  │     ├─ package_data.cpython-311.pyc
│  │     │  │  │     ├─ uts46data.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ msgpack
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  ├─ fallback.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ ext.cpython-311.pyc
│  │     │  │  │     ├─ fallback.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │     ├─ specifiers.cpython-311.pyc
│  │     │  │  │     ├─ tags.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ _manylinux.cpython-311.pyc
│  │     │  │  │     ├─ _musllinux.cpython-311.pyc
│  │     │  │  │     ├─ _structures.cpython-311.pyc
│  │     │  │  │     ├─ __about__.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pkg_resources
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ platformdirs
│  │     │  │  │  ├─ android.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ macos.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ unix.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ android.cpython-311.pyc
│  │     │  │  │     ├─ api.cpython-311.pyc
│  │     │  │  │     ├─ macos.cpython-311.pyc
│  │     │  │  │     ├─ unix.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ windows.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ pygments
│  │     │  │  │  ├─ cmdline.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ filter.py
│  │     │  │  │  ├─ filters
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ formatter.py
│  │     │  │  │  ├─ formatters
│  │     │  │  │  │  ├─ bbcode.py
│  │     │  │  │  │  ├─ groff.py
│  │     │  │  │  │  ├─ html.py
│  │     │  │  │  │  ├─ img.py
│  │     │  │  │  │  ├─ irc.py
│  │     │  │  │  │  ├─ latex.py
│  │     │  │  │  │  ├─ other.py
│  │     │  │  │  │  ├─ pangomarkup.py
│  │     │  │  │  │  ├─ rtf.py
│  │     │  │  │  │  ├─ svg.py
│  │     │  │  │  │  ├─ terminal.py
│  │     │  │  │  │  ├─ terminal256.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ bbcode.cpython-311.pyc
│  │     │  │  │  │     ├─ groff.cpython-311.pyc
│  │     │  │  │  │     ├─ html.cpython-311.pyc
│  │     │  │  │  │     ├─ img.cpython-311.pyc
│  │     │  │  │  │     ├─ irc.cpython-311.pyc
│  │     │  │  │  │     ├─ latex.cpython-311.pyc
│  │     │  │  │  │     ├─ other.cpython-311.pyc
│  │     │  │  │  │     ├─ pangomarkup.cpython-311.pyc
│  │     │  │  │  │     ├─ rtf.cpython-311.pyc
│  │     │  │  │  │     ├─ svg.cpython-311.pyc
│  │     │  │  │  │     ├─ terminal.cpython-311.pyc
│  │     │  │  │  │     ├─ terminal256.cpython-311.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ lexer.py
│  │     │  │  │  ├─ lexers
│  │     │  │  │  │  ├─ python.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ python.cpython-311.pyc
│  │     │  │  │  │     ├─ _mapping.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ modeline.py
│  │     │  │  │  ├─ plugin.py
│  │     │  │  │  ├─ regexopt.py
│  │     │  │  │  ├─ scanner.py
│  │     │  │  │  ├─ sphinxext.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styles
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ token.py
│  │     │  │  │  ├─ unistring.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ cmdline.cpython-311.pyc
│  │     │  │  │     ├─ console.cpython-311.pyc
│  │     │  │  │     ├─ filter.cpython-311.pyc
│  │     │  │  │     ├─ formatter.cpython-311.pyc
│  │     │  │  │     ├─ lexer.cpython-311.pyc
│  │     │  │  │     ├─ modeline.cpython-311.pyc
│  │     │  │  │     ├─ plugin.cpython-311.pyc
│  │     │  │  │     ├─ regexopt.cpython-311.pyc
│  │     │  │  │     ├─ scanner.cpython-311.pyc
│  │     │  │  │     ├─ sphinxext.cpython-311.pyc
│  │     │  │  │     ├─ style.cpython-311.pyc
│  │     │  │  │     ├─ token.cpython-311.pyc
│  │     │  │  │     ├─ unistring.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ pyparsing
│  │     │  │  │  ├─ actions.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ diagram
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ helpers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ results.py
│  │     │  │  │  ├─ testing.py
│  │     │  │  │  ├─ unicode.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ actions.cpython-311.pyc
│  │     │  │  │     ├─ common.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ helpers.cpython-311.pyc
│  │     │  │  │     ├─ results.cpython-311.pyc
│  │     │  │  │     ├─ testing.cpython-311.pyc
│  │     │  │  │     ├─ unicode.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyproject_hooks
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _impl.py
│  │     │  │  │  ├─ _in_process
│  │     │  │  │  │  ├─ _in_process.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ _in_process.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _impl.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ requests
│  │     │  │  │  ├─ adapters.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ certs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ hooks.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packages.py
│  │     │  │  │  ├─ sessions.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ structures.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ _internal_utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __pycache__
│  │     │  │  │  │  ├─ adapters.cpython-311.pyc
│  │     │  │  │  │  ├─ api.cpython-311.pyc
│  │     │  │  │  │  ├─ auth.cpython-311.pyc
│  │     │  │  │  │  ├─ certs.cpython-311.pyc
│  │     │  │  │  │  ├─ compat.cpython-311.pyc
│  │     │  │  │  │  ├─ cookies.cpython-311.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-311.pyc
│  │     │  │  │  │  ├─ help.cpython-311.pyc
│  │     │  │  │  │  ├─ hooks.cpython-311.pyc
│  │     │  │  │  │  ├─ models.cpython-311.pyc
│  │     │  │  │  │  ├─ packages.cpython-311.pyc
│  │     │  │  │  │  ├─ sessions.cpython-311.pyc
│  │     │  │  │  │  ├─ status_codes.cpython-311.pyc
│  │     │  │  │  │  ├─ structures.cpython-311.pyc
│  │     │  │  │  │  ├─ utils.cpython-311.pyc
│  │     │  │  │  │  ├─ _internal_utils.cpython-311.pyc
│  │     │  │  │  │  ├─ __init__.cpython-311.pyc
│  │     │  │  │  │  └─ __version__.cpython-311.pyc
│  │     │  │  │  └─ __version__.py
│  │     │  │  ├─ resolvelib
│  │     │  │  │  ├─ compat
│  │     │  │  │  │  ├─ collections_abc.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ collections_abc.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ providers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ reporters.py
│  │     │  │  │  ├─ resolvers.py
│  │     │  │  │  ├─ structs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ providers.cpython-311.pyc
│  │     │  │  │     ├─ reporters.cpython-311.pyc
│  │     │  │  │     ├─ resolvers.cpython-311.pyc
│  │     │  │  │     ├─ structs.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ rich
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ box.py
│  │     │  │  │  ├─ cells.py
│  │     │  │  │  ├─ color.py
│  │     │  │  │  ├─ color_triplet.py
│  │     │  │  │  ├─ columns.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ constrain.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ control.py
│  │     │  │  │  ├─ default_styles.py
│  │     │  │  │  ├─ diagnose.py
│  │     │  │  │  ├─ emoji.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ filesize.py
│  │     │  │  │  ├─ file_proxy.py
│  │     │  │  │  ├─ highlighter.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ jupyter.py
│  │     │  │  │  ├─ layout.py
│  │     │  │  │  ├─ live.py
│  │     │  │  │  ├─ live_render.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ markup.py
│  │     │  │  │  ├─ measure.py
│  │     │  │  │  ├─ padding.py
│  │     │  │  │  ├─ pager.py
│  │     │  │  │  ├─ palette.py
│  │     │  │  │  ├─ panel.py
│  │     │  │  │  ├─ pretty.py
│  │     │  │  │  ├─ progress.py
│  │     │  │  │  ├─ progress_bar.py
│  │     │  │  │  ├─ prompt.py
│  │     │  │  │  ├─ protocol.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ region.py
│  │     │  │  │  ├─ repr.py
│  │     │  │  │  ├─ rule.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  ├─ screen.py
│  │     │  │  │  ├─ segment.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ status.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styled.py
│  │     │  │  │  ├─ syntax.py
│  │     │  │  │  ├─ table.py
│  │     │  │  │  ├─ terminal_theme.py
│  │     │  │  │  ├─ text.py
│  │     │  │  │  ├─ theme.py
│  │     │  │  │  ├─ themes.py
│  │     │  │  │  ├─ traceback.py
│  │     │  │  │  ├─ tree.py
│  │     │  │  │  ├─ _cell_widths.py
│  │     │  │  │  ├─ _emoji_codes.py
│  │     │  │  │  ├─ _emoji_replace.py
│  │     │  │  │  ├─ _export_format.py
│  │     │  │  │  ├─ _extension.py
│  │     │  │  │  ├─ _fileno.py
│  │     │  │  │  ├─ _inspect.py
│  │     │  │  │  ├─ _log_render.py
│  │     │  │  │  ├─ _loop.py
│  │     │  │  │  ├─ _null_file.py
│  │     │  │  │  ├─ _palettes.py
│  │     │  │  │  ├─ _pick.py
│  │     │  │  │  ├─ _ratio.py
│  │     │  │  │  ├─ _spinners.py
│  │     │  │  │  ├─ _stack.py
│  │     │  │  │  ├─ _timer.py
│  │     │  │  │  ├─ _win32_console.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ _windows_renderer.py
│  │     │  │  │  ├─ _wrap.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-311.pyc
│  │     │  │  │     ├─ align.cpython-311.pyc
│  │     │  │  │     ├─ ansi.cpython-311.pyc
│  │     │  │  │     ├─ bar.cpython-311.pyc
│  │     │  │  │     ├─ box.cpython-311.pyc
│  │     │  │  │     ├─ cells.cpython-311.pyc
│  │     │  │  │     ├─ color.cpython-311.pyc
│  │     │  │  │     ├─ color_triplet.cpython-311.pyc
│  │     │  │  │     ├─ columns.cpython-311.pyc
│  │     │  │  │     ├─ console.cpython-311.pyc
│  │     │  │  │     ├─ constrain.cpython-311.pyc
│  │     │  │  │     ├─ containers.cpython-311.pyc
│  │     │  │  │     ├─ control.cpython-311.pyc
│  │     │  │  │     ├─ default_styles.cpython-311.pyc
│  │     │  │  │     ├─ diagnose.cpython-311.pyc
│  │     │  │  │     ├─ emoji.cpython-311.pyc
│  │     │  │  │     ├─ errors.cpython-311.pyc
│  │     │  │  │     ├─ filesize.cpython-311.pyc
│  │     │  │  │     ├─ file_proxy.cpython-311.pyc
│  │     │  │  │     ├─ highlighter.cpython-311.pyc
│  │     │  │  │     ├─ json.cpython-311.pyc
│  │     │  │  │     ├─ jupyter.cpython-311.pyc
│  │     │  │  │     ├─ layout.cpython-311.pyc
│  │     │  │  │     ├─ live.cpython-311.pyc
│  │     │  │  │     ├─ live_render.cpython-311.pyc
│  │     │  │  │     ├─ logging.cpython-311.pyc
│  │     │  │  │     ├─ markup.cpython-311.pyc
│  │     │  │  │     ├─ measure.cpython-311.pyc
│  │     │  │  │     ├─ padding.cpython-311.pyc
│  │     │  │  │     ├─ pager.cpython-311.pyc
│  │     │  │  │     ├─ palette.cpython-311.pyc
│  │     │  │  │     ├─ panel.cpython-311.pyc
│  │     │  │  │     ├─ pretty.cpython-311.pyc
│  │     │  │  │     ├─ progress.cpython-311.pyc
│  │     │  │  │     ├─ progress_bar.cpython-311.pyc
│  │     │  │  │     ├─ prompt.cpython-311.pyc
│  │     │  │  │     ├─ protocol.cpython-311.pyc
│  │     │  │  │     ├─ region.cpython-311.pyc
│  │     │  │  │     ├─ repr.cpython-311.pyc
│  │     │  │  │     ├─ rule.cpython-311.pyc
│  │     │  │  │     ├─ scope.cpython-311.pyc
│  │     │  │  │     ├─ screen.cpython-311.pyc
│  │     │  │  │     ├─ segment.cpython-311.pyc
│  │     │  │  │     ├─ spinner.cpython-311.pyc
│  │     │  │  │     ├─ status.cpython-311.pyc
│  │     │  │  │     ├─ style.cpython-311.pyc
│  │     │  │  │     ├─ styled.cpython-311.pyc
│  │     │  │  │     ├─ syntax.cpython-311.pyc
│  │     │  │  │     ├─ table.cpython-311.pyc
│  │     │  │  │     ├─ terminal_theme.cpython-311.pyc
│  │     │  │  │     ├─ text.cpython-311.pyc
│  │     │  │  │     ├─ theme.cpython-311.pyc
│  │     │  │  │     ├─ themes.cpython-311.pyc
│  │     │  │  │     ├─ traceback.cpython-311.pyc
│  │     │  │  │     ├─ tree.cpython-311.pyc
│  │     │  │  │     ├─ _cell_widths.cpython-311.pyc
│  │     │  │  │     ├─ _emoji_codes.cpython-311.pyc
│  │     │  │  │     ├─ _emoji_replace.cpython-311.pyc
│  │     │  │  │     ├─ _export_format.cpython-311.pyc
│  │     │  │  │     ├─ _extension.cpython-311.pyc
│  │     │  │  │     ├─ _fileno.cpython-311.pyc
│  │     │  │  │     ├─ _inspect.cpython-311.pyc
│  │     │  │  │     ├─ _log_render.cpython-311.pyc
│  │     │  │  │     ├─ _loop.cpython-311.pyc
│  │     │  │  │     ├─ _null_file.cpython-311.pyc
│  │     │  │  │     ├─ _palettes.cpython-311.pyc
│  │     │  │  │     ├─ _pick.cpython-311.pyc
│  │     │  │  │     ├─ _ratio.cpython-311.pyc
│  │     │  │  │     ├─ _spinners.cpython-311.pyc
│  │     │  │  │     ├─ _stack.cpython-311.pyc
│  │     │  │  │     ├─ _timer.cpython-311.pyc
│  │     │  │  │     ├─ _win32_console.cpython-311.pyc
│  │     │  │  │     ├─ _windows.cpython-311.pyc
│  │     │  │  │     ├─ _windows_renderer.cpython-311.pyc
│  │     │  │  │     ├─ _wrap.cpython-311.pyc
│  │     │  │  │     ├─ __init__.cpython-311.pyc
│  │     │  │  │     └─ __main__.cpython-311.pyc
│  │     │  │  ├─ six.py
│  │     │  │  ├─ tenacity
│  │     │  │  │  ├─ after.py
│  │     │  │  │  ├─ before.py
│  │     │  │  │  ├─ before_sleep.py
│  │     │  │  │  ├─ nap.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ stop.py
│  │     │  │  │  ├─ tornadoweb.py
│  │     │  │  │  ├─ wait.py
│  │     │  │  │  ├─ _asyncio.py
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ after.cpython-311.pyc
│  │     │  │  │     ├─ before.cpython-311.pyc
│  │     │  │  │     ├─ before_sleep.cpython-311.pyc
│  │     │  │  │     ├─ nap.cpython-311.pyc
│  │     │  │  │     ├─ retry.cpython-311.pyc
│  │     │  │  │     ├─ stop.cpython-311.pyc
│  │     │  │  │     ├─ tornadoweb.cpython-311.pyc
│  │     │  │  │     ├─ wait.cpython-311.pyc
│  │     │  │  │     ├─ _asyncio.cpython-311.pyc
│  │     │  │  │     ├─ _utils.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ tomli
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ _types.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _parser.cpython-311.pyc
│  │     │  │  │     ├─ _re.cpython-311.pyc
│  │     │  │  │     ├─ _types.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ truststore
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ _api.py
│  │     │  │  │  ├─ _macos.py
│  │     │  │  │  ├─ _openssl.py
│  │     │  │  │  ├─ _ssl_constants.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _api.cpython-311.pyc
│  │     │  │  │     ├─ _macos.cpython-311.pyc
│  │     │  │  │     ├─ _openssl.cpython-311.pyc
│  │     │  │  │     ├─ _ssl_constants.cpython-311.pyc
│  │     │  │  │     ├─ _windows.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ typing_extensions.py
│  │     │  │  ├─ urllib3
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ connectionpool.py
│  │     │  │  │  ├─ contrib
│  │     │  │  │  │  ├─ appengine.py
│  │     │  │  │  │  ├─ ntlmpool.py
│  │     │  │  │  │  ├─ pyopenssl.py
│  │     │  │  │  │  ├─ securetransport.py
│  │     │  │  │  │  ├─ socks.py
│  │     │  │  │  │  ├─ _appengine_environ.py
│  │     │  │  │  │  ├─ _securetransport
│  │     │  │  │  │  │  ├─ bindings.py
│  │     │  │  │  │  │  ├─ low_level.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ bindings.cpython-311.pyc
│  │     │  │  │  │  │     ├─ low_level.cpython-311.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ appengine.cpython-311.pyc
│  │     │  │  │  │     ├─ ntlmpool.cpython-311.pyc
│  │     │  │  │  │     ├─ pyopenssl.cpython-311.pyc
│  │     │  │  │  │     ├─ securetransport.cpython-311.pyc
│  │     │  │  │  │     ├─ socks.cpython-311.pyc
│  │     │  │  │  │     ├─ _appengine_environ.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fields.py
│  │     │  │  │  ├─ filepost.py
│  │     │  │  │  ├─ packages
│  │     │  │  │  │  ├─ backports
│  │     │  │  │  │  │  ├─ makefile.py
│  │     │  │  │  │  │  ├─ weakref_finalize.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ __pycache__
│  │     │  │  │  │  │     ├─ makefile.cpython-311.pyc
│  │     │  │  │  │  │     ├─ weakref_finalize.cpython-311.pyc
│  │     │  │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  │  ├─ six.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ six.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ poolmanager.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  ├─ util
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ proxy.py
│  │     │  │  │  │  ├─ queue.py
│  │     │  │  │  │  ├─ request.py
│  │     │  │  │  │  ├─ response.py
│  │     │  │  │  │  ├─ retry.py
│  │     │  │  │  │  ├─ ssltransport.py
│  │     │  │  │  │  ├─ ssl_.py
│  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │     │  │  │  │  ├─ timeout.py
│  │     │  │  │  │  ├─ url.py
│  │     │  │  │  │  ├─ wait.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ connection.cpython-311.pyc
│  │     │  │  │  │     ├─ proxy.cpython-311.pyc
│  │     │  │  │  │     ├─ queue.cpython-311.pyc
│  │     │  │  │  │     ├─ request.cpython-311.pyc
│  │     │  │  │  │     ├─ response.cpython-311.pyc
│  │     │  │  │  │     ├─ retry.cpython-311.pyc
│  │     │  │  │  │     ├─ ssltransport.cpython-311.pyc
│  │     │  │  │  │     ├─ ssl_.cpython-311.pyc
│  │     │  │  │  │     ├─ ssl_match_hostname.cpython-311.pyc
│  │     │  │  │  │     ├─ timeout.cpython-311.pyc
│  │     │  │  │  │     ├─ url.cpython-311.pyc
│  │     │  │  │  │     ├─ wait.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ connection.cpython-311.pyc
│  │     │  │  │     ├─ connectionpool.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ fields.cpython-311.pyc
│  │     │  │  │     ├─ filepost.cpython-311.pyc
│  │     │  │  │     ├─ poolmanager.cpython-311.pyc
│  │     │  │  │     ├─ request.cpython-311.pyc
│  │     │  │  │     ├─ response.cpython-311.pyc
│  │     │  │  │     ├─ _collections.cpython-311.pyc
│  │     │  │  │     ├─ _version.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ vendor.txt
│  │     │  │  ├─ webencodings
│  │     │  │  │  ├─ labels.py
│  │     │  │  │  ├─ mklabels.py
│  │     │  │  │  ├─ tests.py
│  │     │  │  │  ├─ x_user_defined.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ labels.cpython-311.pyc
│  │     │  │  │     ├─ mklabels.cpython-311.pyc
│  │     │  │  │     ├─ tests.cpython-311.pyc
│  │     │  │  │     ├─ x_user_defined.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ six.cpython-311.pyc
│  │     │  │     ├─ typing_extensions.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ __pip-runner__.py
│  │     │  └─ __pycache__
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     ├─ __main__.cpython-311.pyc
│  │     │     └─ __pip-runner__.cpython-311.pyc
│  │     ├─ pip-24.0.dist-info
│  │     │  ├─ AUTHORS.txt
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pkg_resources
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _vendor
│  │     │  │  ├─ appdirs.py
│  │     │  │  ├─ importlib_resources
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ readers.py
│  │     │  │  │  ├─ simple.py
│  │     │  │  │  ├─ _adapters.py
│  │     │  │  │  ├─ _common.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _itertools.py
│  │     │  │  │  ├─ _legacy.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-311.pyc
│  │     │  │  │     ├─ readers.cpython-311.pyc
│  │     │  │  │     ├─ simple.cpython-311.pyc
│  │     │  │  │     ├─ _adapters.cpython-311.pyc
│  │     │  │  │     ├─ _common.cpython-311.pyc
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _itertools.cpython-311.pyc
│  │     │  │  │     ├─ _legacy.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ jaraco
│  │     │  │  │  ├─ context.py
│  │     │  │  │  ├─ functools.py
│  │     │  │  │  ├─ text
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ context.cpython-311.pyc
│  │     │  │  │     ├─ functools.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ more_itertools
│  │     │  │  │  ├─ more.py
│  │     │  │  │  ├─ recipes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ more.cpython-311.pyc
│  │     │  │  │     ├─ recipes.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │     ├─ specifiers.cpython-311.pyc
│  │     │  │  │     ├─ tags.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ _manylinux.cpython-311.pyc
│  │     │  │  │     ├─ _musllinux.cpython-311.pyc
│  │     │  │  │     ├─ _structures.cpython-311.pyc
│  │     │  │  │     ├─ __about__.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyparsing
│  │     │  │  │  ├─ actions.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ diagram
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ helpers.py
│  │     │  │  │  ├─ results.py
│  │     │  │  │  ├─ testing.py
│  │     │  │  │  ├─ unicode.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ actions.cpython-311.pyc
│  │     │  │  │     ├─ common.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ helpers.cpython-311.pyc
│  │     │  │  │     ├─ results.cpython-311.pyc
│  │     │  │  │     ├─ testing.cpython-311.pyc
│  │     │  │  │     ├─ unicode.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ zipp.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ appdirs.cpython-311.pyc
│  │     │  │     ├─ zipp.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ platformdirs
│  │     │  ├─ android.py
│  │     │  ├─ api.py
│  │     │  ├─ macos.py
│  │     │  ├─ py.typed
│  │     │  ├─ unix.py
│  │     │  ├─ version.py
│  │     │  ├─ windows.py
│  │     │  ├─ _xdg.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ android.cpython-311.pyc
│  │     │     ├─ api.cpython-311.pyc
│  │     │     ├─ macos.cpython-311.pyc
│  │     │     ├─ unix.cpython-311.pyc
│  │     │     ├─ version.cpython-311.pyc
│  │     │     ├─ windows.cpython-311.pyc
│  │     │     ├─ _xdg.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ platformdirs-4.10.0.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pygame
│  │     │  ├─ base.cp311-win_amd64.pyd
│  │     │  ├─ base.pyi
│  │     │  ├─ bufferproxy.cp311-win_amd64.pyd
│  │     │  ├─ bufferproxy.pyi
│  │     │  ├─ camera.py
│  │     │  ├─ camera.pyi
│  │     │  ├─ color.cp311-win_amd64.pyd
│  │     │  ├─ color.pyi
│  │     │  ├─ colordict.py
│  │     │  ├─ constants.cp311-win_amd64.pyd
│  │     │  ├─ constants.pyi
│  │     │  ├─ cursors.py
│  │     │  ├─ cursors.pyi
│  │     │  ├─ display.cp311-win_amd64.pyd
│  │     │  ├─ display.pyi
│  │     │  ├─ docs
│  │     │  │  ├─ generated
│  │     │  │  │  ├─ c_api
│  │     │  │  │  │  ├─ base.html
│  │     │  │  │  │  ├─ bufferproxy.html
│  │     │  │  │  │  ├─ color.html
│  │     │  │  │  │  ├─ display.html
│  │     │  │  │  │  ├─ event.html
│  │     │  │  │  │  ├─ freetype.html
│  │     │  │  │  │  ├─ mixer.html
│  │     │  │  │  │  ├─ rect.html
│  │     │  │  │  │  ├─ rwobject.html
│  │     │  │  │  │  ├─ slots.html
│  │     │  │  │  │  ├─ surface.html
│  │     │  │  │  │  ├─ surflock.html
│  │     │  │  │  │  └─ version.html
│  │     │  │  │  ├─ c_api.html
│  │     │  │  │  ├─ filepaths.html
│  │     │  │  │  ├─ genindex.html
│  │     │  │  │  ├─ index.html
│  │     │  │  │  ├─ LGPL.txt
│  │     │  │  │  ├─ logos.html
│  │     │  │  │  ├─ py-modindex.html
│  │     │  │  │  ├─ ref
│  │     │  │  │  │  ├─ bufferproxy.html
│  │     │  │  │  │  ├─ camera.html
│  │     │  │  │  │  ├─ cdrom.html
│  │     │  │  │  │  ├─ color.html
│  │     │  │  │  │  ├─ color_list.html
│  │     │  │  │  │  ├─ cursors.html
│  │     │  │  │  │  ├─ display.html
│  │     │  │  │  │  ├─ draw.html
│  │     │  │  │  │  ├─ event.html
│  │     │  │  │  │  ├─ examples.html
│  │     │  │  │  │  ├─ fastevent.html
│  │     │  │  │  │  ├─ font.html
│  │     │  │  │  │  ├─ freetype.html
│  │     │  │  │  │  ├─ gfxdraw.html
│  │     │  │  │  │  ├─ image.html
│  │     │  │  │  │  ├─ joystick.html
│  │     │  │  │  │  ├─ key.html
│  │     │  │  │  │  ├─ locals.html
│  │     │  │  │  │  ├─ mask.html
│  │     │  │  │  │  ├─ math.html
│  │     │  │  │  │  ├─ midi.html
│  │     │  │  │  │  ├─ mixer.html
│  │     │  │  │  │  ├─ mouse.html
│  │     │  │  │  │  ├─ music.html
│  │     │  │  │  │  ├─ overlay.html
│  │     │  │  │  │  ├─ pixelarray.html
│  │     │  │  │  │  ├─ pixelcopy.html
│  │     │  │  │  │  ├─ pygame.html
│  │     │  │  │  │  ├─ rect.html
│  │     │  │  │  │  ├─ scrap.html
│  │     │  │  │  │  ├─ sdl2_controller.html
│  │     │  │  │  │  ├─ sdl2_video.html
│  │     │  │  │  │  ├─ sndarray.html
│  │     │  │  │  │  ├─ sprite.html
│  │     │  │  │  │  ├─ surface.html
│  │     │  │  │  │  ├─ surfarray.html
│  │     │  │  │  │  ├─ tests.html
│  │     │  │  │  │  ├─ time.html
│  │     │  │  │  │  ├─ touch.html
│  │     │  │  │  │  └─ transform.html
│  │     │  │  │  ├─ search.html
│  │     │  │  │  ├─ searchindex.js
│  │     │  │  │  ├─ tut
│  │     │  │  │  │  ├─ CameraIntro.html
│  │     │  │  │  │  ├─ chimp.py.html
│  │     │  │  │  │  ├─ ChimpLineByLine.html
│  │     │  │  │  │  ├─ DisplayModes.html
│  │     │  │  │  │  ├─ ImportInit.html
│  │     │  │  │  │  ├─ MakeGames.html
│  │     │  │  │  │  ├─ MoveIt.html
│  │     │  │  │  │  ├─ newbieguide.html
│  │     │  │  │  │  ├─ PygameIntro.html
│  │     │  │  │  │  ├─ SpriteIntro.html
│  │     │  │  │  │  ├─ SurfarrayIntro.html
│  │     │  │  │  │  ├─ tom_games2.html
│  │     │  │  │  │  ├─ tom_games3.html
│  │     │  │  │  │  ├─ tom_games4.html
│  │     │  │  │  │  ├─ tom_games5.html
│  │     │  │  │  │  └─ tom_games6.html
│  │     │  │  │  ├─ _images
│  │     │  │  │  │  ├─ AdvancedInputOutput1.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput11.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput2.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput21.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput3.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput31.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput4.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput41.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput5.gif
│  │     │  │  │  │  ├─ AdvancedInputOutput51.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha1.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha11.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha2.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha21.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha3.gif
│  │     │  │  │  │  ├─ AdvancedOutputAlpha31.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess1.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess11.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess2.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess21.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess3.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess31.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess4.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess41.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess5.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess51.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess6.gif
│  │     │  │  │  │  ├─ AdvancedOutputProcess61.gif
│  │     │  │  │  │  ├─ angle_to.png
│  │     │  │  │  │  ├─ Bagic-INPUT-resultscreen.png
│  │     │  │  │  │  ├─ Bagic-INPUT-resultscreen1.png
│  │     │  │  │  │  ├─ Bagic-INPUT-sourcecode.png
│  │     │  │  │  │  ├─ Bagic-INPUT-sourcecode1.png
│  │     │  │  │  │  ├─ Bagic-ouput-result-screen.png
│  │     │  │  │  │  ├─ Bagic-ouput-result-screen1.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-resultscreen.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-resultscreen1.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-sourcecode.png
│  │     │  │  │  │  ├─ Bagic-PROCESS-sourcecode1.png
│  │     │  │  │  │  ├─ Basic-ouput-sourcecode.png
│  │     │  │  │  │  ├─ Basic-ouput-sourcecode1.png
│  │     │  │  │  │  ├─ camera_average.jpg
│  │     │  │  │  │  ├─ camera_background.jpg
│  │     │  │  │  │  ├─ camera_green.jpg
│  │     │  │  │  │  ├─ camera_hsv.jpg
│  │     │  │  │  │  ├─ camera_mask.jpg
│  │     │  │  │  │  ├─ camera_rgb.jpg
│  │     │  │  │  │  ├─ camera_thresh.jpg
│  │     │  │  │  │  ├─ camera_thresholded.jpg
│  │     │  │  │  │  ├─ camera_yuv.jpg
│  │     │  │  │  │  ├─ chimpshot.gif
│  │     │  │  │  │  ├─ draw_module_example.png
│  │     │  │  │  │  ├─ introduction-Battleship.png
│  │     │  │  │  │  ├─ introduction-Battleship1.png
│  │     │  │  │  │  ├─ introduction-PuyoPuyo.png
│  │     │  │  │  │  ├─ introduction-PuyoPuyo1.png
│  │     │  │  │  │  ├─ introduction-TPS.png
│  │     │  │  │  │  ├─ introduction-TPS1.png
│  │     │  │  │  │  ├─ intro_ball.gif
│  │     │  │  │  │  ├─ intro_blade.jpg
│  │     │  │  │  │  ├─ intro_freedom.jpg
│  │     │  │  │  │  ├─ joystick_calls.png
│  │     │  │  │  │  ├─ pygame_lofi.png
│  │     │  │  │  │  ├─ pygame_logo.png
│  │     │  │  │  │  ├─ pygame_powered.png
│  │     │  │  │  │  ├─ pygame_powered_lowres.png
│  │     │  │  │  │  ├─ pygame_tiny.png
│  │     │  │  │  │  ├─ surfarray_allblack.png
│  │     │  │  │  │  ├─ surfarray_flipped.png
│  │     │  │  │  │  ├─ surfarray_redimg.png
│  │     │  │  │  │  ├─ surfarray_rgbarray.png
│  │     │  │  │  │  ├─ surfarray_scaledown.png
│  │     │  │  │  │  ├─ surfarray_scaleup.png
│  │     │  │  │  │  ├─ surfarray_soften.png
│  │     │  │  │  │  ├─ surfarray_striped.png
│  │     │  │  │  │  ├─ surfarray_xfade.png
│  │     │  │  │  │  ├─ tom_basic.png
│  │     │  │  │  │  ├─ tom_event-flowchart.png
│  │     │  │  │  │  ├─ tom_formulae.png
│  │     │  │  │  │  └─ tom_radians.png
│  │     │  │  │  ├─ _sources
│  │     │  │  │  │  ├─ c_api.rst.txt
│  │     │  │  │  │  ├─ filepaths.rst.txt
│  │     │  │  │  │  ├─ index.rst.txt
│  │     │  │  │  │  ├─ logos.rst.txt
│  │     │  │  │  │  └─ ref
│  │     │  │  │  │     ├─ bufferproxy.rst.txt
│  │     │  │  │  │     ├─ camera.rst.txt
│  │     │  │  │  │     ├─ cdrom.rst.txt
│  │     │  │  │  │     ├─ color.rst.txt
│  │     │  │  │  │     ├─ color_list.rst.txt
│  │     │  │  │  │     ├─ cursors.rst.txt
│  │     │  │  │  │     ├─ display.rst.txt
│  │     │  │  │  │     ├─ draw.rst.txt
│  │     │  │  │  │     ├─ event.rst.txt
│  │     │  │  │  │     ├─ examples.rst.txt
│  │     │  │  │  │     ├─ fastevent.rst.txt
│  │     │  │  │  │     ├─ font.rst.txt
│  │     │  │  │  │     ├─ freetype.rst.txt
│  │     │  │  │  │     ├─ gfxdraw.rst.txt
│  │     │  │  │  │     ├─ image.rst.txt
│  │     │  │  │  │     ├─ joystick.rst.txt
│  │     │  │  │  │     ├─ key.rst.txt
│  │     │  │  │  │     ├─ locals.rst.txt
│  │     │  │  │  │     ├─ mask.rst.txt
│  │     │  │  │  │     ├─ math.rst.txt
│  │     │  │  │  │     ├─ midi.rst.txt
│  │     │  │  │  │     ├─ mixer.rst.txt
│  │     │  │  │  │     ├─ mouse.rst.txt
│  │     │  │  │  │     ├─ music.rst.txt
│  │     │  │  │  │     ├─ overlay.rst.txt
│  │     │  │  │  │     ├─ pixelarray.rst.txt
│  │     │  │  │  │     ├─ pixelcopy.rst.txt
│  │     │  │  │  │     ├─ pygame.rst.txt
│  │     │  │  │  │     ├─ rect.rst.txt
│  │     │  │  │  │     ├─ scrap.rst.txt
│  │     │  │  │  │     ├─ sdl2_controller.rst.txt
│  │     │  │  │  │     ├─ sdl2_video.rst.txt
│  │     │  │  │  │     ├─ sndarray.rst.txt
│  │     │  │  │  │     ├─ sprite.rst.txt
│  │     │  │  │  │     ├─ surface.rst.txt
│  │     │  │  │  │     ├─ surfarray.rst.txt
│  │     │  │  │  │     ├─ tests.rst.txt
│  │     │  │  │  │     ├─ time.rst.txt
│  │     │  │  │  │     ├─ touch.rst.txt
│  │     │  │  │  │     └─ transform.rst.txt
│  │     │  │  │  └─ _static
│  │     │  │  │     ├─ basic.css
│  │     │  │  │     ├─ doctools.js
│  │     │  │  │     ├─ documentation_options.js
│  │     │  │  │     ├─ file.png
│  │     │  │  │     ├─ language_data.js
│  │     │  │  │     ├─ legacy_logos.zip
│  │     │  │  │     ├─ minus.png
│  │     │  │  │     ├─ plus.png
│  │     │  │  │     ├─ pygame.css
│  │     │  │  │     ├─ pygame.ico
│  │     │  │  │     ├─ pygame_lofi.png
│  │     │  │  │     ├─ pygame_lofi.svg
│  │     │  │  │     ├─ pygame_logo.png
│  │     │  │  │     ├─ pygame_logo.svg
│  │     │  │  │     ├─ pygame_powered.png
│  │     │  │  │     ├─ pygame_powered.svg
│  │     │  │  │     ├─ pygame_powered_lowres.png
│  │     │  │  │     ├─ pygame_tiny.png
│  │     │  │  │     ├─ pygments.css
│  │     │  │  │     ├─ reset.css
│  │     │  │  │     ├─ searchtools.js
│  │     │  │  │     ├─ sphinx_highlight.js
│  │     │  │  │     └─ tooltip.css
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __main__.cpython-311.pyc
│  │     │  ├─ draw.cp311-win_amd64.pyd
│  │     │  ├─ draw.pyi
│  │     │  ├─ draw_py.py
│  │     │  ├─ event.cp311-win_amd64.pyd
│  │     │  ├─ event.pyi
│  │     │  ├─ examples
│  │     │  │  ├─ aacircle.py
│  │     │  │  ├─ aliens.py
│  │     │  │  ├─ arraydemo.py
│  │     │  │  ├─ audiocapture.py
│  │     │  │  ├─ blend_fill.py
│  │     │  │  ├─ blit_blends.py
│  │     │  │  ├─ camera.py
│  │     │  │  ├─ chimp.py
│  │     │  │  ├─ cursors.py
│  │     │  │  ├─ data
│  │     │  │  │  ├─ alien1.gif
│  │     │  │  │  ├─ alien1.jpg
│  │     │  │  │  ├─ alien1.png
│  │     │  │  │  ├─ alien2.gif
│  │     │  │  │  ├─ alien2.png
│  │     │  │  │  ├─ alien3.gif
│  │     │  │  │  ├─ alien3.png
│  │     │  │  │  ├─ arraydemo.bmp
│  │     │  │  │  ├─ asprite.bmp
│  │     │  │  │  ├─ background.gif
│  │     │  │  │  ├─ BGR.png
│  │     │  │  │  ├─ black.ppm
│  │     │  │  │  ├─ blue.gif
│  │     │  │  │  ├─ blue.mpg
│  │     │  │  │  ├─ bomb.gif
│  │     │  │  │  ├─ boom.wav
│  │     │  │  │  ├─ brick.png
│  │     │  │  │  ├─ car_door.wav
│  │     │  │  │  ├─ chimp.png
│  │     │  │  │  ├─ city.png
│  │     │  │  │  ├─ crimson.pnm
│  │     │  │  │  ├─ cursor.png
│  │     │  │  │  ├─ danger.gif
│  │     │  │  │  ├─ explosion1.gif
│  │     │  │  │  ├─ fist.png
│  │     │  │  │  ├─ green.pcx
│  │     │  │  │  ├─ grey.pgm
│  │     │  │  │  ├─ house_lo.mp3
│  │     │  │  │  ├─ house_lo.ogg
│  │     │  │  │  ├─ house_lo.wav
│  │     │  │  │  ├─ laplacian.png
│  │     │  │  │  ├─ liquid.bmp
│  │     │  │  │  ├─ midikeys.png
│  │     │  │  │  ├─ player1.gif
│  │     │  │  │  ├─ punch.wav
│  │     │  │  │  ├─ purple.xpm
│  │     │  │  │  ├─ red.jpg
│  │     │  │  │  ├─ sans.ttf
│  │     │  │  │  ├─ scarlet.webp
│  │     │  │  │  ├─ secosmic_lo.wav
│  │     │  │  │  ├─ shot.gif
│  │     │  │  │  ├─ static.png
│  │     │  │  │  ├─ teal.svg
│  │     │  │  │  ├─ turquoise.tif
│  │     │  │  │  ├─ whiff.wav
│  │     │  │  │  └─ yellow.tga
│  │     │  │  ├─ dropevent.py
│  │     │  │  ├─ eventlist.py
│  │     │  │  ├─ fonty.py
│  │     │  │  ├─ font_viewer.py
│  │     │  │  ├─ freetype_misc.py
│  │     │  │  ├─ glcube.py
│  │     │  │  ├─ go_over_there.py
│  │     │  │  ├─ grid.py
│  │     │  │  ├─ headless_no_windows_needed.py
│  │     │  │  ├─ joystick.py
│  │     │  │  ├─ liquid.py
│  │     │  │  ├─ mask.py
│  │     │  │  ├─ midi.py
│  │     │  │  ├─ moveit.py
│  │     │  │  ├─ music_drop_fade.py
│  │     │  │  ├─ pixelarray.py
│  │     │  │  ├─ playmus.py
│  │     │  │  ├─ README.rst
│  │     │  │  ├─ resizing_new.py
│  │     │  │  ├─ scaletest.py
│  │     │  │  ├─ scrap_clipboard.py
│  │     │  │  ├─ scroll.py
│  │     │  │  ├─ setmodescale.py
│  │     │  │  ├─ sound.py
│  │     │  │  ├─ sound_array_demos.py
│  │     │  │  ├─ sprite_texture.py
│  │     │  │  ├─ stars.py
│  │     │  │  ├─ testsprite.py
│  │     │  │  ├─ textinput.py
│  │     │  │  ├─ vgrade.py
│  │     │  │  ├─ video.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ aacircle.cpython-311.pyc
│  │     │  │     ├─ aliens.cpython-311.pyc
│  │     │  │     ├─ arraydemo.cpython-311.pyc
│  │     │  │     ├─ audiocapture.cpython-311.pyc
│  │     │  │     ├─ blend_fill.cpython-311.pyc
│  │     │  │     ├─ blit_blends.cpython-311.pyc
│  │     │  │     ├─ camera.cpython-311.pyc
│  │     │  │     ├─ chimp.cpython-311.pyc
│  │     │  │     ├─ cursors.cpython-311.pyc
│  │     │  │     ├─ dropevent.cpython-311.pyc
│  │     │  │     ├─ eventlist.cpython-311.pyc
│  │     │  │     ├─ fonty.cpython-311.pyc
│  │     │  │     ├─ font_viewer.cpython-311.pyc
│  │     │  │     ├─ freetype_misc.cpython-311.pyc
│  │     │  │     ├─ glcube.cpython-311.pyc
│  │     │  │     ├─ go_over_there.cpython-311.pyc
│  │     │  │     ├─ grid.cpython-311.pyc
│  │     │  │     ├─ headless_no_windows_needed.cpython-311.pyc
│  │     │  │     ├─ joystick.cpython-311.pyc
│  │     │  │     ├─ liquid.cpython-311.pyc
│  │     │  │     ├─ mask.cpython-311.pyc
│  │     │  │     ├─ midi.cpython-311.pyc
│  │     │  │     ├─ moveit.cpython-311.pyc
│  │     │  │     ├─ music_drop_fade.cpython-311.pyc
│  │     │  │     ├─ pixelarray.cpython-311.pyc
│  │     │  │     ├─ playmus.cpython-311.pyc
│  │     │  │     ├─ resizing_new.cpython-311.pyc
│  │     │  │     ├─ scaletest.cpython-311.pyc
│  │     │  │     ├─ scrap_clipboard.cpython-311.pyc
│  │     │  │     ├─ scroll.cpython-311.pyc
│  │     │  │     ├─ setmodescale.cpython-311.pyc
│  │     │  │     ├─ sound.cpython-311.pyc
│  │     │  │     ├─ sound_array_demos.cpython-311.pyc
│  │     │  │     ├─ sprite_texture.cpython-311.pyc
│  │     │  │     ├─ stars.cpython-311.pyc
│  │     │  │     ├─ testsprite.cpython-311.pyc
│  │     │  │     ├─ textinput.cpython-311.pyc
│  │     │  │     ├─ vgrade.cpython-311.pyc
│  │     │  │     ├─ video.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ fastevent.py
│  │     │  ├─ fastevent.pyi
│  │     │  ├─ font.cp311-win_amd64.pyd
│  │     │  ├─ font.pyi
│  │     │  ├─ freesansbold.ttf
│  │     │  ├─ freetype.dll
│  │     │  ├─ freetype.py
│  │     │  ├─ freetype.pyi
│  │     │  ├─ ftfont.py
│  │     │  ├─ gfxdraw.cp311-win_amd64.pyd
│  │     │  ├─ gfxdraw.pyi
│  │     │  ├─ image.cp311-win_amd64.pyd
│  │     │  ├─ image.pyi
│  │     │  ├─ imageext.cp311-win_amd64.pyd
│  │     │  ├─ joystick.cp311-win_amd64.pyd
│  │     │  ├─ joystick.pyi
│  │     │  ├─ key.cp311-win_amd64.pyd
│  │     │  ├─ key.pyi
│  │     │  ├─ libjpeg-9.dll
│  │     │  ├─ libmodplug-1.dll
│  │     │  ├─ libogg-0.dll
│  │     │  ├─ libopus-0.dll
│  │     │  ├─ libopusfile-0.dll
│  │     │  ├─ libpng16-16.dll
│  │     │  ├─ libtiff-5.dll
│  │     │  ├─ libwebp-7.dll
│  │     │  ├─ locals.py
│  │     │  ├─ locals.pyi
│  │     │  ├─ macosx.py
│  │     │  ├─ mask.cp311-win_amd64.pyd
│  │     │  ├─ mask.pyi
│  │     │  ├─ math.cp311-win_amd64.pyd
│  │     │  ├─ math.pyi
│  │     │  ├─ midi.py
│  │     │  ├─ midi.pyi
│  │     │  ├─ mixer.cp311-win_amd64.pyd
│  │     │  ├─ mixer.pyi
│  │     │  ├─ mixer_music.cp311-win_amd64.pyd
│  │     │  ├─ mixer_music.pyi
│  │     │  ├─ mouse.cp311-win_amd64.pyd
│  │     │  ├─ mouse.pyi
│  │     │  ├─ newbuffer.cp311-win_amd64.pyd
│  │     │  ├─ pixelarray.cp311-win_amd64.pyd
│  │     │  ├─ pixelarray.pyi
│  │     │  ├─ pixelcopy.cp311-win_amd64.pyd
│  │     │  ├─ pixelcopy.pyi
│  │     │  ├─ pkgdata.py
│  │     │  ├─ portmidi.dll
│  │     │  ├─ py.typed
│  │     │  ├─ pygame.ico
│  │     │  ├─ pygame_icon.bmp
│  │     │  ├─ pygame_icon.icns
│  │     │  ├─ pygame_icon_mac.bmp
│  │     │  ├─ pypm.cp311-win_amd64.pyd
│  │     │  ├─ rect.cp311-win_amd64.pyd
│  │     │  ├─ rect.pyi
│  │     │  ├─ rwobject.cp311-win_amd64.pyd
│  │     │  ├─ rwobject.pyi
│  │     │  ├─ scrap.cp311-win_amd64.pyd
│  │     │  ├─ scrap.pyi
│  │     │  ├─ SDL2.dll
│  │     │  ├─ SDL2_image.dll
│  │     │  ├─ SDL2_mixer.dll
│  │     │  ├─ SDL2_ttf.dll
│  │     │  ├─ sndarray.py
│  │     │  ├─ sndarray.pyi
│  │     │  ├─ sprite.py
│  │     │  ├─ sprite.pyi
│  │     │  ├─ surface.cp311-win_amd64.pyd
│  │     │  ├─ surface.pyi
│  │     │  ├─ surfarray.py
│  │     │  ├─ surfarray.pyi
│  │     │  ├─ surflock.cp311-win_amd64.pyd
│  │     │  ├─ surflock.pyi
│  │     │  ├─ sysfont.py
│  │     │  ├─ tests
│  │     │  │  ├─ base_test.py
│  │     │  │  ├─ blit_test.py
│  │     │  │  ├─ bufferproxy_test.py
│  │     │  │  ├─ camera_test.py
│  │     │  │  ├─ color_test.py
│  │     │  │  ├─ constants_test.py
│  │     │  │  ├─ controller_test.py
│  │     │  │  ├─ cursors_test.py
│  │     │  │  ├─ display_test.py
│  │     │  │  ├─ docs_test.py
│  │     │  │  ├─ draw_test.py
│  │     │  │  ├─ event_test.py
│  │     │  │  ├─ fixtures
│  │     │  │  │  ├─ fonts
│  │     │  │  │  │  ├─ A_PyGameMono-8.png
│  │     │  │  │  │  ├─ PlayfairDisplaySemibold.ttf
│  │     │  │  │  │  ├─ PyGameMono-18-100dpi.bdf
│  │     │  │  │  │  ├─ PyGameMono-18-75dpi.bdf
│  │     │  │  │  │  ├─ PyGameMono-8.bdf
│  │     │  │  │  │  ├─ PyGameMono.otf
│  │     │  │  │  │  ├─ test_fixed.otf
│  │     │  │  │  │  ├─ test_sans.ttf
│  │     │  │  │  │  └─ u13079_PyGameMono-8.png
│  │     │  │  │  └─ xbm_cursors
│  │     │  │  │     ├─ white_sizing.xbm
│  │     │  │  │     └─ white_sizing_mask.xbm
│  │     │  │  ├─ font_test.py
│  │     │  │  ├─ freetype_tags.py
│  │     │  │  ├─ freetype_test.py
│  │     │  │  ├─ ftfont_tags.py
│  │     │  │  ├─ ftfont_test.py
│  │     │  │  ├─ gfxdraw_test.py
│  │     │  │  ├─ imageext_tags.py
│  │     │  │  ├─ imageext_test.py
│  │     │  │  ├─ image_tags.py
│  │     │  │  ├─ image_test.py
│  │     │  │  ├─ image__save_gl_surface_test.py
│  │     │  │  ├─ joystick_test.py
│  │     │  │  ├─ key_test.py
│  │     │  │  ├─ locals_test.py
│  │     │  │  ├─ mask_test.py
│  │     │  │  ├─ math_test.py
│  │     │  │  ├─ midi_test.py
│  │     │  │  ├─ mixer_music_tags.py
│  │     │  │  ├─ mixer_music_test.py
│  │     │  │  ├─ mixer_tags.py
│  │     │  │  ├─ mixer_test.py
│  │     │  │  ├─ mouse_test.py
│  │     │  │  ├─ pixelarray_test.py
│  │     │  │  ├─ pixelcopy_test.py
│  │     │  │  ├─ rect_test.py
│  │     │  │  ├─ run_tests__tests
│  │     │  │  │  ├─ all_ok
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ fake_5_test.py
│  │     │  │  │  │  ├─ fake_6_test.py
│  │     │  │  │  │  ├─ no_assertions__ret_code_of_1__test.py
│  │     │  │  │  │  ├─ zero_tests_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_5_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_6_test.cpython-311.pyc
│  │     │  │  │  │     ├─ no_assertions__ret_code_of_1__test.cpython-311.pyc
│  │     │  │  │  │     ├─ zero_tests_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ everything
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ incomplete_todo_test.py
│  │     │  │  │  │  ├─ magic_tag_test.py
│  │     │  │  │  │  ├─ sleep_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ incomplete_todo_test.cpython-311.pyc
│  │     │  │  │  │     ├─ magic_tag_test.cpython-311.pyc
│  │     │  │  │  │     ├─ sleep_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exclude
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ invisible_tag_test.py
│  │     │  │  │  │  ├─ magic_tag_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ invisible_tag_test.cpython-311.pyc
│  │     │  │  │  │     ├─ magic_tag_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ failures1
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ incomplete
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ incomplete_todo
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ infinite_loop
│  │     │  │  │  │  ├─ fake_1_test.py
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_1_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ print_stderr
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ print_stdout
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ fake_3_test.py
│  │     │  │  │  │  ├─ fake_4_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_3_test.cpython-311.pyc
│  │     │  │  │  │     ├─ fake_4_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ run_tests__test.py
│  │     │  │  │  ├─ timeout
│  │     │  │  │  │  ├─ fake_2_test.py
│  │     │  │  │  │  ├─ sleep_test.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     ├─ fake_2_test.cpython-311.pyc
│  │     │  │  │  │     ├─ sleep_test.cpython-311.pyc
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ run_tests__test.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ rwobject_test.py
│  │     │  │  ├─ scrap_tags.py
│  │     │  │  ├─ scrap_test.py
│  │     │  │  ├─ sndarray_tags.py
│  │     │  │  ├─ sndarray_test.py
│  │     │  │  ├─ sprite_test.py
│  │     │  │  ├─ surface_test.py
│  │     │  │  ├─ surfarray_tags.py
│  │     │  │  ├─ surfarray_test.py
│  │     │  │  ├─ surflock_test.py
│  │     │  │  ├─ sysfont_test.py
│  │     │  │  ├─ test_utils
│  │     │  │  │  ├─ arrinter.py
│  │     │  │  │  ├─ async_sub.py
│  │     │  │  │  ├─ buftools.py
│  │     │  │  │  ├─ endian.py
│  │     │  │  │  ├─ png.py
│  │     │  │  │  ├─ run_tests.py
│  │     │  │  │  ├─ test_machinery.py
│  │     │  │  │  ├─ test_runner.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ arrinter.cpython-311.pyc
│  │     │  │  │     ├─ async_sub.cpython-311.pyc
│  │     │  │  │     ├─ buftools.cpython-311.pyc
│  │     │  │  │     ├─ endian.cpython-311.pyc
│  │     │  │  │     ├─ png.cpython-311.pyc
│  │     │  │  │     ├─ run_tests.cpython-311.pyc
│  │     │  │  │     ├─ test_machinery.cpython-311.pyc
│  │     │  │  │     ├─ test_runner.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ threads_test.py
│  │     │  │  ├─ time_test.py
│  │     │  │  ├─ touch_test.py
│  │     │  │  ├─ transform_test.py
│  │     │  │  ├─ version_test.py
│  │     │  │  ├─ video_test.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ base_test.cpython-311.pyc
│  │     │  │     ├─ blit_test.cpython-311.pyc
│  │     │  │     ├─ bufferproxy_test.cpython-311.pyc
│  │     │  │     ├─ camera_test.cpython-311.pyc
│  │     │  │     ├─ color_test.cpython-311.pyc
│  │     │  │     ├─ constants_test.cpython-311.pyc
│  │     │  │     ├─ controller_test.cpython-311.pyc
│  │     │  │     ├─ cursors_test.cpython-311.pyc
│  │     │  │     ├─ display_test.cpython-311.pyc
│  │     │  │     ├─ docs_test.cpython-311.pyc
│  │     │  │     ├─ draw_test.cpython-311.pyc
│  │     │  │     ├─ event_test.cpython-311.pyc
│  │     │  │     ├─ font_test.cpython-311.pyc
│  │     │  │     ├─ freetype_tags.cpython-311.pyc
│  │     │  │     ├─ freetype_test.cpython-311.pyc
│  │     │  │     ├─ ftfont_tags.cpython-311.pyc
│  │     │  │     ├─ ftfont_test.cpython-311.pyc
│  │     │  │     ├─ gfxdraw_test.cpython-311.pyc
│  │     │  │     ├─ imageext_tags.cpython-311.pyc
│  │     │  │     ├─ imageext_test.cpython-311.pyc
│  │     │  │     ├─ image_tags.cpython-311.pyc
│  │     │  │     ├─ image_test.cpython-311.pyc
│  │     │  │     ├─ image__save_gl_surface_test.cpython-311.pyc
│  │     │  │     ├─ joystick_test.cpython-311.pyc
│  │     │  │     ├─ key_test.cpython-311.pyc
│  │     │  │     ├─ locals_test.cpython-311.pyc
│  │     │  │     ├─ mask_test.cpython-311.pyc
│  │     │  │     ├─ math_test.cpython-311.pyc
│  │     │  │     ├─ midi_test.cpython-311.pyc
│  │     │  │     ├─ mixer_music_tags.cpython-311.pyc
│  │     │  │     ├─ mixer_music_test.cpython-311.pyc
│  │     │  │     ├─ mixer_tags.cpython-311.pyc
│  │     │  │     ├─ mixer_test.cpython-311.pyc
│  │     │  │     ├─ mouse_test.cpython-311.pyc
│  │     │  │     ├─ pixelarray_test.cpython-311.pyc
│  │     │  │     ├─ pixelcopy_test.cpython-311.pyc
│  │     │  │     ├─ rect_test.cpython-311.pyc
│  │     │  │     ├─ rwobject_test.cpython-311.pyc
│  │     │  │     ├─ scrap_tags.cpython-311.pyc
│  │     │  │     ├─ scrap_test.cpython-311.pyc
│  │     │  │     ├─ sndarray_tags.cpython-311.pyc
│  │     │  │     ├─ sndarray_test.cpython-311.pyc
│  │     │  │     ├─ sprite_test.cpython-311.pyc
│  │     │  │     ├─ surface_test.cpython-311.pyc
│  │     │  │     ├─ surfarray_tags.cpython-311.pyc
│  │     │  │     ├─ surfarray_test.cpython-311.pyc
│  │     │  │     ├─ surflock_test.cpython-311.pyc
│  │     │  │     ├─ sysfont_test.cpython-311.pyc
│  │     │  │     ├─ threads_test.cpython-311.pyc
│  │     │  │     ├─ time_test.cpython-311.pyc
│  │     │  │     ├─ touch_test.cpython-311.pyc
│  │     │  │     ├─ transform_test.cpython-311.pyc
│  │     │  │     ├─ version_test.cpython-311.pyc
│  │     │  │     ├─ video_test.cpython-311.pyc
│  │     │  │     ├─ __init__.cpython-311.pyc
│  │     │  │     └─ __main__.cpython-311.pyc
│  │     │  ├─ threads
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ time.cp311-win_amd64.pyd
│  │     │  ├─ time.pyi
│  │     │  ├─ transform.cp311-win_amd64.pyd
│  │     │  ├─ transform.pyi
│  │     │  ├─ version.py
│  │     │  ├─ version.pyi
│  │     │  ├─ zlib1.dll
│  │     │  ├─ _camera.cp311-win_amd64.pyd
│  │     │  ├─ _camera_opencv.py
│  │     │  ├─ _camera_vidcapture.py
│  │     │  ├─ _common.pyi
│  │     │  ├─ _freetype.cp311-win_amd64.pyd
│  │     │  ├─ _sdl2
│  │     │  │  ├─ audio.cp311-win_amd64.pyd
│  │     │  │  ├─ audio.pyi
│  │     │  │  ├─ controller.cp311-win_amd64.pyd
│  │     │  │  ├─ controller.pyi
│  │     │  │  ├─ mixer.cp311-win_amd64.pyd
│  │     │  │  ├─ sdl2.cp311-win_amd64.pyd
│  │     │  │  ├─ sdl2.pyi
│  │     │  │  ├─ touch.cp311-win_amd64.pyd
│  │     │  │  ├─ touch.pyi
│  │     │  │  ├─ video.cp311-win_amd64.pyd
│  │     │  │  ├─ video.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _sprite.cp311-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  ├─ __pycache__
│  │     │  │  ├─ camera.cpython-311.pyc
│  │     │  │  ├─ colordict.cpython-311.pyc
│  │     │  │  ├─ cursors.cpython-311.pyc
│  │     │  │  ├─ draw_py.cpython-311.pyc
│  │     │  │  ├─ fastevent.cpython-311.pyc
│  │     │  │  ├─ freetype.cpython-311.pyc
│  │     │  │  ├─ ftfont.cpython-311.pyc
│  │     │  │  ├─ locals.cpython-311.pyc
│  │     │  │  ├─ macosx.cpython-311.pyc
│  │     │  │  ├─ midi.cpython-311.pyc
│  │     │  │  ├─ pkgdata.cpython-311.pyc
│  │     │  │  ├─ sndarray.cpython-311.pyc
│  │     │  │  ├─ sprite.cpython-311.pyc
│  │     │  │  ├─ surfarray.cpython-311.pyc
│  │     │  │  ├─ sysfont.cpython-311.pyc
│  │     │  │  ├─ version.cpython-311.pyc
│  │     │  │  ├─ _camera_opencv.cpython-311.pyc
│  │     │  │  ├─ _camera_vidcapture.cpython-311.pyc
│  │     │  │  └─ __init__.cpython-311.pyc
│  │     │  └─ __pyinstaller
│  │     │     ├─ hook-pygame.py
│  │     │     ├─ __init__.py
│  │     │     └─ __pycache__
│  │     │        ├─ hook-pygame.cpython-311.pyc
│  │     │        └─ __init__.cpython-311.pyc
│  │     ├─ pygame-2.6.1.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pytokens
│  │     │  ├─ cli.py
│  │     │  ├─ py.typed
│  │     │  ├─ _mypyc_dummy.cp311-win_amd64.pyd
│  │     │  ├─ _mypyc_dummy.py
│  │     │  ├─ __init__.cp311-win_amd64.pyd
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  └─ __pycache__
│  │     │     ├─ cli.cpython-311.pyc
│  │     │     ├─ _mypyc_dummy.cpython-311.pyc
│  │     │     ├─ __init__.cpython-311.pyc
│  │     │     └─ __main__.cpython-311.pyc
│  │     ├─ pytokens-0.4.1.dist-info
│  │     │  ├─ INSTALLER
│  │     │  ├─ licenses
│  │     │  │  └─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ setuptools
│  │     │  ├─ archive_util.py
│  │     │  ├─ build_meta.py
│  │     │  ├─ cli-32.exe
│  │     │  ├─ cli-64.exe
│  │     │  ├─ cli-arm64.exe
│  │     │  ├─ cli.exe
│  │     │  ├─ command
│  │     │  │  ├─ alias.py
│  │     │  │  ├─ bdist_egg.py
│  │     │  │  ├─ bdist_rpm.py
│  │     │  │  ├─ build.py
│  │     │  │  ├─ build_clib.py
│  │     │  │  ├─ build_ext.py
│  │     │  │  ├─ build_py.py
│  │     │  │  ├─ develop.py
│  │     │  │  ├─ dist_info.py
│  │     │  │  ├─ easy_install.py
│  │     │  │  ├─ editable_wheel.py
│  │     │  │  ├─ egg_info.py
│  │     │  │  ├─ install.py
│  │     │  │  ├─ install_egg_info.py
│  │     │  │  ├─ install_lib.py
│  │     │  │  ├─ install_scripts.py
│  │     │  │  ├─ launcher manifest.xml
│  │     │  │  ├─ py36compat.py
│  │     │  │  ├─ register.py
│  │     │  │  ├─ rotate.py
│  │     │  │  ├─ saveopts.py
│  │     │  │  ├─ sdist.py
│  │     │  │  ├─ setopt.py
│  │     │  │  ├─ test.py
│  │     │  │  ├─ upload.py
│  │     │  │  ├─ upload_docs.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ alias.cpython-311.pyc
│  │     │  │     ├─ bdist_egg.cpython-311.pyc
│  │     │  │     ├─ bdist_rpm.cpython-311.pyc
│  │     │  │     ├─ build.cpython-311.pyc
│  │     │  │     ├─ build_clib.cpython-311.pyc
│  │     │  │     ├─ build_ext.cpython-311.pyc
│  │     │  │     ├─ build_py.cpython-311.pyc
│  │     │  │     ├─ develop.cpython-311.pyc
│  │     │  │     ├─ dist_info.cpython-311.pyc
│  │     │  │     ├─ easy_install.cpython-311.pyc
│  │     │  │     ├─ editable_wheel.cpython-311.pyc
│  │     │  │     ├─ egg_info.cpython-311.pyc
│  │     │  │     ├─ install.cpython-311.pyc
│  │     │  │     ├─ install_egg_info.cpython-311.pyc
│  │     │  │     ├─ install_lib.cpython-311.pyc
│  │     │  │     ├─ install_scripts.cpython-311.pyc
│  │     │  │     ├─ py36compat.cpython-311.pyc
│  │     │  │     ├─ register.cpython-311.pyc
│  │     │  │     ├─ rotate.cpython-311.pyc
│  │     │  │     ├─ saveopts.cpython-311.pyc
│  │     │  │     ├─ sdist.cpython-311.pyc
│  │     │  │     ├─ setopt.cpython-311.pyc
│  │     │  │     ├─ test.cpython-311.pyc
│  │     │  │     ├─ upload.cpython-311.pyc
│  │     │  │     ├─ upload_docs.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ config
│  │     │  │  ├─ expand.py
│  │     │  │  ├─ pyprojecttoml.py
│  │     │  │  ├─ setupcfg.py
│  │     │  │  ├─ _apply_pyprojecttoml.py
│  │     │  │  ├─ _validate_pyproject
│  │     │  │  │  ├─ error_reporting.py
│  │     │  │  │  ├─ extra_validations.py
│  │     │  │  │  ├─ fastjsonschema_exceptions.py
│  │     │  │  │  ├─ fastjsonschema_validations.py
│  │     │  │  │  ├─ formats.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ error_reporting.cpython-311.pyc
│  │     │  │  │     ├─ extra_validations.cpython-311.pyc
│  │     │  │  │     ├─ fastjsonschema_exceptions.cpython-311.pyc
│  │     │  │  │     ├─ fastjsonschema_validations.cpython-311.pyc
│  │     │  │  │     ├─ formats.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ expand.cpython-311.pyc
│  │     │  │     ├─ pyprojecttoml.cpython-311.pyc
│  │     │  │     ├─ setupcfg.cpython-311.pyc
│  │     │  │     ├─ _apply_pyprojecttoml.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ depends.py
│  │     │  ├─ dep_util.py
│  │     │  ├─ discovery.py
│  │     │  ├─ dist.py
│  │     │  ├─ errors.py
│  │     │  ├─ extension.py
│  │     │  ├─ extern
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ glob.py
│  │     │  ├─ gui-32.exe
│  │     │  ├─ gui-64.exe
│  │     │  ├─ gui-arm64.exe
│  │     │  ├─ gui.exe
│  │     │  ├─ installer.py
│  │     │  ├─ launch.py
│  │     │  ├─ logging.py
│  │     │  ├─ monkey.py
│  │     │  ├─ msvc.py
│  │     │  ├─ namespaces.py
│  │     │  ├─ package_index.py
│  │     │  ├─ py34compat.py
│  │     │  ├─ sandbox.py
│  │     │  ├─ script (dev).tmpl
│  │     │  ├─ script.tmpl
│  │     │  ├─ unicode_utils.py
│  │     │  ├─ version.py
│  │     │  ├─ wheel.py
│  │     │  ├─ windows_support.py
│  │     │  ├─ _deprecation_warning.py
│  │     │  ├─ _distutils
│  │     │  │  ├─ archive_util.py
│  │     │  │  ├─ bcppcompiler.py
│  │     │  │  ├─ ccompiler.py
│  │     │  │  ├─ cmd.py
│  │     │  │  ├─ command
│  │     │  │  │  ├─ bdist.py
│  │     │  │  │  ├─ bdist_dumb.py
│  │     │  │  │  ├─ bdist_rpm.py
│  │     │  │  │  ├─ build.py
│  │     │  │  │  ├─ build_clib.py
│  │     │  │  │  ├─ build_ext.py
│  │     │  │  │  ├─ build_py.py
│  │     │  │  │  ├─ build_scripts.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ clean.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ install_data.py
│  │     │  │  │  ├─ install_egg_info.py
│  │     │  │  │  ├─ install_headers.py
│  │     │  │  │  ├─ install_lib.py
│  │     │  │  │  ├─ install_scripts.py
│  │     │  │  │  ├─ py37compat.py
│  │     │  │  │  ├─ register.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  ├─ upload.py
│  │     │  │  │  ├─ _framework_compat.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ bdist.cpython-311.pyc
│  │     │  │  │     ├─ bdist_dumb.cpython-311.pyc
│  │     │  │  │     ├─ bdist_rpm.cpython-311.pyc
│  │     │  │  │     ├─ build.cpython-311.pyc
│  │     │  │  │     ├─ build_clib.cpython-311.pyc
│  │     │  │  │     ├─ build_ext.cpython-311.pyc
│  │     │  │  │     ├─ build_py.cpython-311.pyc
│  │     │  │  │     ├─ build_scripts.cpython-311.pyc
│  │     │  │  │     ├─ check.cpython-311.pyc
│  │     │  │  │     ├─ clean.cpython-311.pyc
│  │     │  │  │     ├─ config.cpython-311.pyc
│  │     │  │  │     ├─ install.cpython-311.pyc
│  │     │  │  │     ├─ install_data.cpython-311.pyc
│  │     │  │  │     ├─ install_egg_info.cpython-311.pyc
│  │     │  │  │     ├─ install_headers.cpython-311.pyc
│  │     │  │  │     ├─ install_lib.cpython-311.pyc
│  │     │  │  │     ├─ install_scripts.cpython-311.pyc
│  │     │  │  │     ├─ py37compat.cpython-311.pyc
│  │     │  │  │     ├─ register.cpython-311.pyc
│  │     │  │  │     ├─ sdist.cpython-311.pyc
│  │     │  │  │     ├─ upload.cpython-311.pyc
│  │     │  │  │     ├─ _framework_compat.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ config.py
│  │     │  │  ├─ core.py
│  │     │  │  ├─ cygwinccompiler.py
│  │     │  │  ├─ debug.py
│  │     │  │  ├─ dep_util.py
│  │     │  │  ├─ dir_util.py
│  │     │  │  ├─ dist.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ extension.py
│  │     │  │  ├─ fancy_getopt.py
│  │     │  │  ├─ filelist.py
│  │     │  │  ├─ file_util.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ msvc9compiler.py
│  │     │  │  ├─ msvccompiler.py
│  │     │  │  ├─ py38compat.py
│  │     │  │  ├─ py39compat.py
│  │     │  │  ├─ spawn.py
│  │     │  │  ├─ sysconfig.py
│  │     │  │  ├─ text_file.py
│  │     │  │  ├─ unixccompiler.py
│  │     │  │  ├─ util.py
│  │     │  │  ├─ version.py
│  │     │  │  ├─ versionpredicate.py
│  │     │  │  ├─ _collections.py
│  │     │  │  ├─ _functools.py
│  │     │  │  ├─ _macos_compat.py
│  │     │  │  ├─ _msvccompiler.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ archive_util.cpython-311.pyc
│  │     │  │     ├─ bcppcompiler.cpython-311.pyc
│  │     │  │     ├─ ccompiler.cpython-311.pyc
│  │     │  │     ├─ cmd.cpython-311.pyc
│  │     │  │     ├─ config.cpython-311.pyc
│  │     │  │     ├─ core.cpython-311.pyc
│  │     │  │     ├─ cygwinccompiler.cpython-311.pyc
│  │     │  │     ├─ debug.cpython-311.pyc
│  │     │  │     ├─ dep_util.cpython-311.pyc
│  │     │  │     ├─ dir_util.cpython-311.pyc
│  │     │  │     ├─ dist.cpython-311.pyc
│  │     │  │     ├─ errors.cpython-311.pyc
│  │     │  │     ├─ extension.cpython-311.pyc
│  │     │  │     ├─ fancy_getopt.cpython-311.pyc
│  │     │  │     ├─ filelist.cpython-311.pyc
│  │     │  │     ├─ file_util.cpython-311.pyc
│  │     │  │     ├─ log.cpython-311.pyc
│  │     │  │     ├─ msvc9compiler.cpython-311.pyc
│  │     │  │     ├─ msvccompiler.cpython-311.pyc
│  │     │  │     ├─ py38compat.cpython-311.pyc
│  │     │  │     ├─ py39compat.cpython-311.pyc
│  │     │  │     ├─ spawn.cpython-311.pyc
│  │     │  │     ├─ sysconfig.cpython-311.pyc
│  │     │  │     ├─ text_file.cpython-311.pyc
│  │     │  │     ├─ unixccompiler.cpython-311.pyc
│  │     │  │     ├─ util.cpython-311.pyc
│  │     │  │     ├─ version.cpython-311.pyc
│  │     │  │     ├─ versionpredicate.cpython-311.pyc
│  │     │  │     ├─ _collections.cpython-311.pyc
│  │     │  │     ├─ _functools.cpython-311.pyc
│  │     │  │     ├─ _macos_compat.cpython-311.pyc
│  │     │  │     ├─ _msvccompiler.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ _entry_points.py
│  │     │  ├─ _imp.py
│  │     │  ├─ _importlib.py
│  │     │  ├─ _itertools.py
│  │     │  ├─ _path.py
│  │     │  ├─ _reqs.py
│  │     │  ├─ _vendor
│  │     │  │  ├─ importlib_metadata
│  │     │  │  │  ├─ _adapters.py
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _functools.py
│  │     │  │  │  ├─ _itertools.py
│  │     │  │  │  ├─ _meta.py
│  │     │  │  │  ├─ _text.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _adapters.cpython-311.pyc
│  │     │  │  │     ├─ _collections.cpython-311.pyc
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _functools.cpython-311.pyc
│  │     │  │  │     ├─ _itertools.cpython-311.pyc
│  │     │  │  │     ├─ _meta.cpython-311.pyc
│  │     │  │  │     ├─ _text.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ importlib_resources
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ readers.py
│  │     │  │  │  ├─ simple.py
│  │     │  │  │  ├─ _adapters.py
│  │     │  │  │  ├─ _common.py
│  │     │  │  │  ├─ _compat.py
│  │     │  │  │  ├─ _itertools.py
│  │     │  │  │  ├─ _legacy.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ abc.cpython-311.pyc
│  │     │  │  │     ├─ readers.cpython-311.pyc
│  │     │  │  │     ├─ simple.cpython-311.pyc
│  │     │  │  │     ├─ _adapters.cpython-311.pyc
│  │     │  │  │     ├─ _common.cpython-311.pyc
│  │     │  │  │     ├─ _compat.cpython-311.pyc
│  │     │  │  │     ├─ _itertools.cpython-311.pyc
│  │     │  │  │     ├─ _legacy.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ jaraco
│  │     │  │  │  ├─ context.py
│  │     │  │  │  ├─ functools.py
│  │     │  │  │  ├─ text
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ context.cpython-311.pyc
│  │     │  │  │     ├─ functools.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ more_itertools
│  │     │  │  │  ├─ more.py
│  │     │  │  │  ├─ recipes.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ more.cpython-311.pyc
│  │     │  │  │     ├─ recipes.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ ordered_set.py
│  │     │  │  ├─ packaging
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ __about__.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ markers.cpython-311.pyc
│  │     │  │  │     ├─ requirements.cpython-311.pyc
│  │     │  │  │     ├─ specifiers.cpython-311.pyc
│  │     │  │  │     ├─ tags.cpython-311.pyc
│  │     │  │  │     ├─ utils.cpython-311.pyc
│  │     │  │  │     ├─ version.cpython-311.pyc
│  │     │  │  │     ├─ _manylinux.cpython-311.pyc
│  │     │  │  │     ├─ _musllinux.cpython-311.pyc
│  │     │  │  │     ├─ _structures.cpython-311.pyc
│  │     │  │  │     ├─ __about__.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ pyparsing
│  │     │  │  │  ├─ actions.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ diagram
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ __pycache__
│  │     │  │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ helpers.py
│  │     │  │  │  ├─ results.py
│  │     │  │  │  ├─ testing.py
│  │     │  │  │  ├─ unicode.py
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ actions.cpython-311.pyc
│  │     │  │  │     ├─ common.cpython-311.pyc
│  │     │  │  │     ├─ core.cpython-311.pyc
│  │     │  │  │     ├─ exceptions.cpython-311.pyc
│  │     │  │  │     ├─ helpers.cpython-311.pyc
│  │     │  │  │     ├─ results.cpython-311.pyc
│  │     │  │  │     ├─ testing.cpython-311.pyc
│  │     │  │  │     ├─ unicode.cpython-311.pyc
│  │     │  │  │     ├─ util.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ tomli
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ _types.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ __pycache__
│  │     │  │  │     ├─ _parser.cpython-311.pyc
│  │     │  │  │     ├─ _re.cpython-311.pyc
│  │     │  │  │     ├─ _types.cpython-311.pyc
│  │     │  │  │     └─ __init__.cpython-311.pyc
│  │     │  │  ├─ typing_extensions.py
│  │     │  │  ├─ zipp.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __pycache__
│  │     │  │     ├─ ordered_set.cpython-311.pyc
│  │     │  │     ├─ typing_extensions.cpython-311.pyc
│  │     │  │     ├─ zipp.cpython-311.pyc
│  │     │  │     └─ __init__.cpython-311.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ archive_util.cpython-311.pyc
│  │     │     ├─ build_meta.cpython-311.pyc
│  │     │     ├─ depends.cpython-311.pyc
│  │     │     ├─ dep_util.cpython-311.pyc
│  │     │     ├─ discovery.cpython-311.pyc
│  │     │     ├─ dist.cpython-311.pyc
│  │     │     ├─ errors.cpython-311.pyc
│  │     │     ├─ extension.cpython-311.pyc
│  │     │     ├─ glob.cpython-311.pyc
│  │     │     ├─ installer.cpython-311.pyc
│  │     │     ├─ launch.cpython-311.pyc
│  │     │     ├─ logging.cpython-311.pyc
│  │     │     ├─ monkey.cpython-311.pyc
│  │     │     ├─ msvc.cpython-311.pyc
│  │     │     ├─ namespaces.cpython-311.pyc
│  │     │     ├─ package_index.cpython-311.pyc
│  │     │     ├─ py34compat.cpython-311.pyc
│  │     │     ├─ sandbox.cpython-311.pyc
│  │     │     ├─ unicode_utils.cpython-311.pyc
│  │     │     ├─ version.cpython-311.pyc
│  │     │     ├─ wheel.cpython-311.pyc
│  │     │     ├─ windows_support.cpython-311.pyc
│  │     │     ├─ _deprecation_warning.cpython-311.pyc
│  │     │     ├─ _entry_points.cpython-311.pyc
│  │     │     ├─ _imp.cpython-311.pyc
│  │     │     ├─ _importlib.cpython-311.pyc
│  │     │     ├─ _itertools.cpython-311.pyc
│  │     │     ├─ _path.cpython-311.pyc
│  │     │     ├─ _reqs.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     ├─ setuptools-65.5.0.dist-info
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ _black_version.py
│  │     ├─ _black_version.pyi
│  │     ├─ _distutils_hack
│  │     │  ├─ override.py
│  │     │  ├─ __init__.py
│  │     │  └─ __pycache__
│  │     │     ├─ override.cpython-311.pyc
│  │     │     └─ __init__.cpython-311.pyc
│  │     └─ __pycache__
│  │        ├─ mypy_extensions.cpython-311.pyc
│  │        └─ _black_version.cpython-311.pyc
│  ├─ pyvenv.cfg
│  └─ Scripts
│     ├─ activate
│     ├─ activate.bat
│     ├─ Activate.ps1
│     ├─ black.exe
│     ├─ blackd.exe
│     ├─ deactivate.bat
│     ├─ pip.exe
│     ├─ pip3.11.exe
│     ├─ pip3.exe
│     ├─ python.exe
│     └─ pythonw.exe
└─ __pycache__
   ├─ enemy.cpython-311.pyc
   ├─ game.cpython-311.pyc
   ├─ player.cpython-311.pyc
   └─ settings.cpython-311.pyc

```