#!/bin/sh

# Navigate to the documentation directory
cd /docs

# Pull the latest changes from the repository
git pull

# Rebuild the Sphinx documentation
#make html

sphinx-build -b html . _build/html

cd /docs/_build/html
python -m http.server 8000

exec "$@"