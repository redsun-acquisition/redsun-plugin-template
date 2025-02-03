# Getting started

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
conda create -n my-plugin python=3.10
conda activate my-plugin
```
:::
:::{tab-item} mamba
```{code-block} shell
mamba create -n my-plugin python=3.10
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