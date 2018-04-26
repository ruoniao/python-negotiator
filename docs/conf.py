"""Sphinx documentation build configuration file."""

import os
import sys

# Add the host/guest/common directories to the module path.
docs_directory = os.path.dirname(os.path.abspath(__file__))
for package_directory in ['host', 'guest', 'common']:
    sys.path.insert(0, os.path.join(docs_directory, '..', package_directory))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'negotiator'
copyright = u'2015, Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from negotiator_host import __version__ as negotiator_version

# The short X.Y version.
version = '.'.join(negotiator_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = negotiator_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    python2=('https://docs.python.org/2/', None),
    python3=('https://docs.python.org/3/', None),
    humanfriendly=('https://humanfriendly.readthedocs.io/en/latest/', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# Output file base name for HTML help builder.
htmlhelp_basename = 'negotiatordoc'

# -- Customizing autodoc output ------------------------------------------------


def setup(app):
    """Instruct autodoc not to omit ``__init__()``."""
    # Based on http://stackoverflow.com/a/5599712/788200.
    app.connect('autodoc-skip-member', (lambda app, what, name, obj, skip, options:
                                        False if name == '__init__' else skip))
