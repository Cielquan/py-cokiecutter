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
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    # "sphinx.ext.autodoc",
    # "sphinx_autodoc_typehints", # sphinx-autodoc-typehints
    # "sphinx_click.ext", # sphinx-click
]


#: -- LINKS ----------------------------------------------------------------------------

#: Linkcheck - 1 Worker 5 Retries to fix 429 error
linkcheck_workers = 1
linkcheck_retries = 5
linkcheck_timeout = 30

tls_cacerts = os.getenv("SSL_CERT_FILE")

intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}

extlinks = {
    "issue": ("https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/issues/%s", "#"),
    "pull": ("https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/pull/%s", "p"),
    "user": ("https://github.com/%s", "@"),
}


#: -- FILES ----------------------------------------------------------------------------

#: Index source file
master_doc = "index"

#: Files to exclude for source of doc
exclude_patterns = [".changes/*"]

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
