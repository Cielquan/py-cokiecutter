Welcome to {{ cookiecutter.project_name }}'s documentation!
{{ "=" * (11 + cookiecutter.project_name|length + 17) }}

.. include:: _badges.rst


**{{ cookiecutter.project_short_description }}**


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage


.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api


.. toctree::
   :maxdepth: 2
   :caption: Miscellaneous:

   contribution/index
   changelog
   authors
   license
