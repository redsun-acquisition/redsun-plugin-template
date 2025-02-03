# Getting started

Before downloading the template, the following installations are required:

- [git](https://git-scm.com/)
- an installed version of [Python](https://www.python.org/) (minimum required version is 3.9);
  - alternatively, either [conda](https://docs.conda.io/projects/conda/en/stable/) or [mamba](https://mamba.readthedocs.io/en/latest/) installed
- [hatch](https://hatch.pypa.io/1.13/install/)


The recomended development environment is [VSCode](https://code.visualstudio.com/). The template provides a [pre-shipped configuration](https://github.com/redsun-acquisition/redsun-plugin-template/tree/main/template/%7B%7B%20vscode%20%7D%7D) with the standard tooling used accross the Redsun ecosystem.

## Setup environment

First, create the folder which will contain your plugin. In this example, we'll use the name `my-plugin`, but feel free to chose any other name.

```{code-block} shell
mkdir my-plugin
```

Then, create a virtual environment and activate it.

::::{tab-set}
:::{tab-item} venv
```{code-block} shell
# python version depends
# on the globally installed python
python -m venv my-plugin

# for Windows, you'll need to use
# Activate.ps1
venv\scripts\Activate
```
:::
:::{tab-item} conda
```{code-block} shell
conda create -n my-plugin python=3.9
conda activate my-plugin
```
:::
:::{tab-item} mamba
```{code-block} shell
mamba create -n my-plugin python=3.9
mamba activate my-plugin
```
:::
::::

In your currently active environment, install the following dependencies via `pip`:

- [`copier`]
- [`copier-templates-extensions`]
- [`jinja2-time`]

[`copier`]: https://github.com/copier-org/copier
[`copier-templates-extensions`]: https://github.com/copier-org/copier-templates-extensions
[`jinja2-time`]: https://github.com/hackebrot/jinja2-time

```{code-block} shell
python -m pip install copier copier-templates-extensions jinja2-time
```

## Download the template

In your active environment, generate a new Redsun plugin with the following command:

```{code-block} shell
# "my-plugin" is the name of your plugin folder;
# change it accordingly
copier copy --trust https://github.com/napari/napari-plugin-template my-plugin
```

At this point, follow the command line [prompts] to generate your plugin.

[prompts]: ./prompts.md