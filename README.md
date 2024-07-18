# Temppy

Toy project to work on documentation.

## Building docs

```bash
# Install the required packages
pip install sphinx==7.3.7 myst-parser

# Move to the docs folder
cd docs

# Build the documentation
sphinx-apidoc -o . ../temppy
make html
```

open `docs/_build/html/index.html` with your favourite browser.
