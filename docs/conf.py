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

extensions = ['myst_parser', 'sphinx.ext.githubpages', 'sphinx_design']
myst_enable_extensions = ['attrs_block', 'colon_fence']

github_user = "redsun-acquisition"
github_repo = "redsun-plugin-template"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Redsun plugin template"
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_context = {
    # this doesn't really matter;
    # adding it only for completion
    "default_mode": "auto",
}
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": f"https://github.com/{github_repo}/{github_user}",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
   ]
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_heading_anchors = 3
