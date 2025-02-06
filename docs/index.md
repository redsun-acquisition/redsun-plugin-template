# Redsun plugin template

[copier](https://copier.readthedocs.io/en/stable/) template for authoring Redsun plugins.

```{caution} 
This template is still a work in progress. You should not use this until the author removes this notice.
```

```{tip}
This repo is not meant to be cloned/forked directly!
```

## Features

- [hatchling](https://hatch.pypa.io/latest/) as build backend
  - [hatch-vcs](https://github.com/ofek/hatch-vcs) for version management
- [VSCode](https://code.visualstudio.com/) extensions setup
- [ruff](https://docs.astral.sh/ruff/) for linting and code formatting
- [mypy](https://github.com/python/mypy) for type checking
- [pre-commit](https://pre-commit.com/) hooks for ruff and file checking
- - automatic license selection between the following choices:
  - [BSD-3]
  - [MIT]
  - [Apache v2.0]
  - [GNU GPL v3.0]
  - [GNU LGPL v3.0]


```{toctree}
:maxdepth: 1

getting_started
prompts
changelog
license
```

[redsun]: https://redsun-acquisition.github.io/
[copier]: https://copier.readthedocs.io/en/stable/
[mit]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0