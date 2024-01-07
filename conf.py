# conf.py

import sys; 
sys.setrecursionlimit(1500000)

# Add Read the Docs Theme
import sphinx_rtd_theme

import os
import re

# Prefer to use the version of the theme in this repo
# and not the installed version of the theme.
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('./customizing_parameters/'))


extensions = [
    # ... other extensions
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

project = u'Focalx documentations'
author = u'Pritam Bolenwar, Focalx'
copyright = author
language = 'en'


highlight_language = 'none'  # Or any other default language


html_theme = "sphinx_rtd_theme"

html_logo = "logo/logo.svg"

templates_path = ['_templates']

# html_css_files = [
#     'custom.css',
# ]

html_theme_options = {
    'navigation_depth': 4
}
html_context = {}