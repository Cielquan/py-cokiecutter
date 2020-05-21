"""
    docs.source.conf
    ~~~~~~~~~~~~~~~~

    Configuration file for the Sphinx documentation builder.

    {% if cookiecutter.license != "Not open source" -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    :license: {{ cookiecutter.license }}, see LICENSE.rst for more details
    {%- else -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    {%- endif %}
"""
#: pylint: disable=C0103
import os
import sys

from datetime import datetime
from pathlib import Path
from typing import List

import sphinx_rtd_theme  # type: ignore

from {{ cookiecutter.project_slug }} import __version__


#: Add Repo to path
sys.path.insert(0, os.path.abspath("../.."))

#: Vars
CONF_DIR = Path(__file__)
TODAY = datetime.today()
YEAR = f"{TODAY.year}"


#: -- PROJECT INFORMATION --------------------------------------------------------------

project = "{{ cookiecutter.project_name }}"
author = "{{ cookiecutter.full_name }}"
release_year = "{{ cookiecutter.year }}"
copyright = (
    f"{release_year}{('-' + YEAR) if YEAR != release_year else ''}, "
    + author
)  #: pylint: disable=W0622
#: The full version, including alpha/beta/rc tags
release = __version__
#: Major version like (X.Y)
version = __version__[0:3]
#: Release date
release_date = f"{TODAY}"


#: -- SPHINX CONFIG --------------------------------------------------------------------

#: Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
]

intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}


#: -- FILES ----------------------------------------------------------------------------

#: Index source file
master_doc = "index"

#: Files to exclude for source of doc
exclude_patterns: List[str] = []

#: Folder for static files, if folder exists
html_static_path = []
if Path(CONF_DIR, "_static").exists():
    html_static_path = ["_static"]

#: Folder for template files, if folder exists
templates_path = []
if Path(CONF_DIR, "_templates").exists():
    templates_path = ["_templates"]


#: -- HTML OUTPUT ----------------------------------------------------------------------

#: Theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_last_updated_fmt = TODAY.isoformat()

#: Add links to *.rst source files on HTML pages
html_show_sourcelink = True

#: Pygments syntax highlighting style
pygments_style = "sphinx"
