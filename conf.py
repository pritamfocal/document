# conf.py

import sys; 
sys.setrecursionlimit(1500000)

# Add Read the Docs Theme
import sphinx_rtd_theme

extensions = [
    # ... other extensions
    "sphinx_rtd_theme",
    "sphinxcontrib.jquery",
]

project = u'Focalx documentations'
author = u'Pritam Bolenwar, Focalx'
copyright = author
language = 'en'

html_theme = "sphinx_rtd_theme"

html_logo = "logo/logo.svg"

#templates_path = ['_templates']

#html_css_files = [
#    'custom.css',
#]

html_theme_options = {
    'navigation_depth': 6
}
