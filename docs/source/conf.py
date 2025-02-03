# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'redsun-plugin-template'
copyright = '2025, Jacopo Abramo'
author = 'Jacopo Abramo'

exclude_patterns = ['_build']

extensions = ['myst-parser']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_context = {
   # this doesn't really matter;
   # adding it only for completion
   "default_mode": "auto"
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
