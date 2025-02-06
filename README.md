[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
![GitHub Release](https://img.shields.io/github/v/release/redsun-acquisition/redsun-plugin-template)

# redsun-plugin-template

[copier](https://copier.readthedocs.io/en/stable/) template for authoring Redsun plugins.

> [!WARNING]
> The Redsun ecosystem is still a work in progress. You may use this template at your discretion,
but be aware of possible breaking changes in [Redsun](https://github.com/redsun-acquisition/redsun) or [Sunflare](https://github.com/redsun-acquisition/sunflare).

> [!NOTE]
> This repo is not meant to be cloned/forked directly!

## Features

- [hatchling](https://hatch.pypa.io/latest/) as build backend
  - [hatch-vcs](https://github.com/ofek/hatch-vcs) for version management
- [VSCode](https://code.visualstudio.com/) extensions setup
- [ruff](https://docs.astral.sh/ruff/) for linting and code formatting
- [mypy](https://github.com/python/mypy) for type checking
- [pre-commit](https://pre-commit.com/) hooks for ruff and file checking
- [sphinx](https://www.sphinx-doc.org/en/master/) template in markdown language using [myst-parser](https://myst-parser.readthedocs.io/en/stable/)
- automatic license selection between the following choices:
  - [BSD-3](http://opensource.org/licenses/BSD-3-Clause)
  - [MIT]
  - [Apache v2.0]
  - [GNU GPL v3.0]
  - [GNU LGPL v3.0]

## Usage

See the [Getting started](https://redsun-acquisition.github.io/redsun-plugin-template/getting_started/) page in the documentation to use the template.

## Contributing

If you encounter problems in using the template, please [file an issue].

## Changelog 

All noteable changes are reported [here](https://redsun-acquisition.github.io/redsun-plugin-template/changelog/).

## License

Distributed under the terms of the [BSD-3](#license) license, `redsun-plugin-template`
is free and open source software.


[file an issue]: https://github.com/redsun-acquisition/redsun-plugin-template/issues
[mit]: http://opensource.org/licenses/MIT
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
