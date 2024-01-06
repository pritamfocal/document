# conf.py

import sys; 
sys.setrecursionlimit(1500000)

# Add Read the Docs Theme
import sphinx_rtd_theme

extensions = [
    # ... other extensions
    "sphinx_rtd_theme",
]

html_theme = "sphinx_rtd_theme"

html_logo = "logo/logo.jpg"
