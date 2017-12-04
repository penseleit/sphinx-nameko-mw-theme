# -*- coding: utf-8 -*-
"""Sphinx Readable Theme documentation build configuration file.

This file is execfile()d with the current directory set to its containing dir.

"""

import os
import sys
import pkg_resources
import sphinx_nameko_mw_theme


# Adding this directory to the sys path, to build autodoc of example module.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


# -- General configuration ----------------------------------------------------

# Defining Sphinx extension modules.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx']

autodoc_default_flags = ['members', 'show-inheritance']
autodoc_member_order = 'bysource'

# Don't display module names before objects titles, it's more readable.
add_module_names = False

intersphinx_mapping = {
    'python': ('http://docs.python.org/2.7', None),
}

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Sphinx Nameko MW Theme'
copyright = u'2017'

# The version info for the project, acts as replacement for |version| and
# |release|, also used in various other places throughout the built documents.
#
# The short X.Y version.
version = '0.0.4'
# The full version, including alpha/beta/rc tags.
release = '0.0.4'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme_path = [sphinx_nameko_mw_theme.get_html_theme_path()]
html_theme = 'nameko-mw'

# html_theme_options = {}
html_theme_options = {
  # show a logo in the document below the relative links
  'doc_logo': '',

  # Include a link to the currently used theme in the footer
  'linktotheme': 'True'
}
