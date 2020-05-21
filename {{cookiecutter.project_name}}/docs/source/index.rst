.. This is the documentation's base file.

{{ "=" * (11 + cookiecutter.project_name|length + 17) }}
Welcome to {{ cookiecutter.project_name }}'s documentation!
{{ "=" * (11 + cookiecutter.project_name|length + 17) }}

{{ cookiecutter.project_short_description }}


.. include:: _badges.rst


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage


.. toctree::
   :maxdepth: 2
   :caption: Miscellaneous:

   changelog
   license
