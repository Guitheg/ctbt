# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from mlcf import __version__
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'MLCF'
copyright = '2022, CGrbi'
author = 'CGrbi'
version=__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx_math_dollar',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    "sphinx_rtd_theme"
]

math_number_all=True
# -- Math Latex ------------------------------------------------
mathjax_config = {
    'tex2jax': {
        'inlineMath': [ ["$","$"] ],
        'displayMath': [["\\[","\\]"] ],
    },
}
dmath_double_inline=True
math_dollar_debug = True
from sphinx_math_dollar import NODE_BLACKLIST
from docutils.nodes import header

math_dollar_node_blacklist = NODE_BLACKLIST + (header,)
# --------------------------------------------------------------


# -- Google-style napoleon config ------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

source_suffix = ['.rst', '.md']
# --------------------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

todo_include_todos = False
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_title = "MLCF documentation"
html_short_title = "MLCF documentation"
html_codeblock_linenos_style='inline'


html_theme_options = {
    'prev_next_buttons_location': 'bottom',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'titles_only': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_show_sourcelink=False
html_copy_source=False