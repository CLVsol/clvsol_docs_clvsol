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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os

# -- Project information -----------------------------------------------------

project = 'CLVsol'
copyright = '2020, Carlos Eduardo Vercelino - CLVsol'
author = 'Carlos Eduardo Vercelino - CLVsol'

# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'pt_BR'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None
html_favicon = '_static/CLVsol_favicon.ico'

html_logo = '_static/CLVsol_logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

on_rtd = os.environ.get('READTHEDOCS') == 'True'

if on_rtd:

    # html_theme = 'default'
    html_theme = 'sphinx_rtd_theme'

    # html_theme_options = {}
    html_theme_options = {
        'canonical_url': '',
        'logo_only': False,
        'display_version': True,
        # 'prev_next_buttons_location': 'bottom',
        'prev_next_buttons_location': 'both',
        # 'style_external_links': False,
        'style_external_links': True,
        # 'vcs_pageview_mode': '',
        # 'style_nav_header_background': 'white',
        'style_nav_header_background': '#2980B9',
        # Toc options
        'collapse_navigation': False,
        'sticky_navigation': True,
        'navigation_depth': 4,
        # 'navigation_depth': -1,
        'includehidden': True,
        'titles_only': False
    }

# else:

#     html_theme = 'alabaster'
#     # html_theme = 'classic'
#     # html_theme = 'sphinxdoc'
#     # html_theme = 'agogo'
#     # html_theme = 'nature'
#     # html_theme = 'pyramid'
#     # html_theme = 'traditional'
#     # html_theme = 'bizstyle'
#     # html_theme = 'sphinx_rtd_theme'

#     html_sidebars = {
#         '**': [
#             'about.html',
#             # 'globaltoc.html',
#             # 'localtoc.html',
#             'navigation.html',
#             # 'relations.html',
#             'sourcelink.html',
#             'searchbox.html',
#         ],
#     }

#     # Theme options are theme-specific and customize the look and feel of a theme
#     # further.  For a list of options available for each theme, see the
#     # documentation.
#     #
#     # html_theme_options = {}
#     html_theme_options = {
#         'logo': 'CLVsol_logo.png',
#         'logo_name': True,
#         'description': 'Documentação do CLVhealth-JCAFB',
#         'show_powered_by': True,
#         # 'page_width': 'auto',
#         'page_width': '1220px',
#         # 'sidebar_width': '220px',
#         'sidebar_width': '302px',
#         'fixed_sidebar': False,
#         'show_related': True,
#     }

else:

    # html_theme = 'alabaster'
    # html_theme = 'classic'
    # html_theme = 'sphinxdoc'
    # html_theme = 'agogo'
    # html_theme = 'nature'
    # html_theme = 'pyramid'
    # html_theme = 'traditional'
    # html_theme = 'bizstyle'
    html_theme = 'sphinx_rtd_theme'

    # html_sidebars = {
    #     '**': [
    #         'about.html',
    #         # 'globaltoc.html',
    #         # 'localtoc.html',
    #         'navigation.html',
    #         # 'relations.html',
    #         'sourcelink.html',
    #         'searchbox.html',
    #     ],
    # }

    # Theme options are theme-specific and customize the look and feel of a theme
    # further.  For a list of options available for each theme, see the
    # documentation.
    #
    # html_theme_options = {}
    html_theme_options = {
        'canonical_url': '',
        # 'analytics_id': 'UA-XXXXXXX-1',  # Provided by Google in your dashboard
        'logo_only': False,
        'display_version': True,
        # 'prev_next_buttons_location': 'bottom',
        'prev_next_buttons_location': 'both',
        # 'style_external_links': False,
        'style_external_links': True,
        # 'vcs_pageview_mode': '',
        # 'style_nav_header_background': 'white',
        'style_nav_header_background': '#2980B9',
        # Toc options
        'collapse_navigation': False,
        'sticky_navigation': True,
        'navigation_depth': 4,
        # 'navigation_depth': -1,
        'includehidden': True,
        'titles_only': False
    }

master_doc = 'index'
