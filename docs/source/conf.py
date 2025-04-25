# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Artes Com Madeira'
copyright = '2025, MBM'
author = 'Michel Braz de Morais'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

html_static_path = ['_static', '_static/css']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'Pt_Br'
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    #'style_nav_header_background': 'blue',
    'display_version' : False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_show_sourcelink = False

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

#https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig_format
numfig = True

numfig_format = {'figure':'Figure %s' }
# -- Options for HTML output

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', '_static/css']

#A list of regular expressions that match URIs that should not be checked when doing a linkcheck build. Example:
linkcheck_ignore = [r'http://localhost:\d+/']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Artes Com Madeira'

html_theme = 'sphinx_rtd_theme'
imgmath_image_format = 'png'
imgmath_font_size = 14
# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    dir(app)
    try:
        app.add_css_file( "css/hatnotes.css" )
        app.add_css_file( "css/image_rotate.css" )
    except:
        app.add_stylesheet( "css/hatnotes.css" )
        app.add_stylesheet( "css/image_rotate.css" )

from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/png',
    'image/gif',
    'image/jpeg'
]
