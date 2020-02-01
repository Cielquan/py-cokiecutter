.. This file 'index.rst' created {{ cookiecutter.iso_date }} is part of the project/program '{{ cookiecutter.project_name }}'.
.. Copyright (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}, see LICENSE for more details


Welcome to {{ cookiecutter.project_name }}'s documentation!
==========={% for _ in cookiecutter.project_name %}={% endfor %}=================


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

   changelog
   license
