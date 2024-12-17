# RedSun plugin prompt reference

When you first run the template to build a RedSun plugin, you will be prompted
for some configuration options. Your answers to these prompts will determine
some aspects of your plugin package including its name, versioning behaviour,
license, etc. None of these configuration options are set in stone - you
can always change these later, but it may require some effort.

This document details what each of the prompts is asking, what the effect
of your choice will be on your package directory/plugin, and any potential
pitfalls of selecting one option over another.

## full_name

This is the name of the main author of this plugin, and will appear in your
`pyproject.toml` file. If you publish your plugin to PyPI, this name will also be listed
in the author metadata field.

## email

This is your preferred contact email address and will appear in your `pyproject.toml`
file. If you publish your plugin to PyPI, this contact email address wil be
listed next to the author's name.

## github_username_or_organization

This is the GitHub username under whose account the GitHub repository for the
plugin will be hosted. This username will be used to create the GitHub url
for this plugin and will appear as part of the `[project.urls]` field in `pyproject.toml`.

This username could be your personal username or the organization under which
you plan to host the plugin on GitHub. If you do not wish to provide a username,
simply press `Enter` at this prompt, and choose `provide later` at the
`github_repository_url` prompt - this will omit the `[project.urls]` field in `pyproject.toml`
entirely, and you may add it later if you wish.

## plugin_name

This is the desired name for your RedSun plugin, and will also be the name
of the Python package directory we create for you. The plugin name you choose
will be listed in `pyproject.toml` under the `name` field, as well as under
`[options.entry_points]`. If you publish your package to PyPI, users will be able
to install your package using

```
pip install plugin_name
```

The convention for these packages is that they should have short, all-lowercase
names, with hyphens preferred over underscores for separating words.

## github_repository_url

This will be the code repository link that is stored in the `[project.urls]` field in
`pyproject.toml`. The default option is generated using your `github_username_or_organization` and `plugin_name`.

Choose `provide later` at this prompt if the default generated url is incorrect,
or if you do not wish to provide a url at all. You can then add this link to your
`pyproject.toml` later, under the `[project.urls]` field.

## module_name

This is the name of the Python module where the code for your plugin will live.
We create a folder with this name inside the top level directory of your plugin,
and populate it with code templates.

This module will also be added as the entry point to your plugin in `pyproject.toml`.
This is how RedSun discovers plugins on launch.

## display_name

> [!NOTE]
> TODO

## short_description

This should be a short description of what your plugin does. It will be listed
in `pyproject.toml` under the `description` field. If you publish your plugin to PyPI,
this description will also be listed alongside your package name in search results.

## install_precommit

The default for this prompt is `"n"`.

If you choose "y" for this prompt, then [pre-commit](ttps://pre-commit.com/) will be installed.
Among other things, it includes checks for code linting and best practices in RedSun plugins.

## install_dependabot

The default for this prompt is `"n"`.

If you choose "y" for this prompt, then a [Dependabot](https://docs.github.com/en/code-security/dependabot) configuration file will be created at `.github/dependabot.yml`.

You will still need to enable Dependabot in your github settings, [see the instructions at this link](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#managing-dependabot-security-updates-for-your-repositories).


## license

This prompt allows you to choose from a variety of open source licensing options
for your plugin. Choosing any of the options will lead to a boilerplate `LICENSE`
file being added to the root of your plugin directory, as well as the [SPDX identifier](https://spdx.org/licenses/)
for that license being listed in your `setup.cfg` under the `license` field.

License options include: [BSD-3], [MIT], [MPL v2.0], [Apache v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

[mit]: http://opensource.org/licenses/MIT
[mpl v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
