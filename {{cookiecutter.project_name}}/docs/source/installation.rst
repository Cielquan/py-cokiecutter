.. highlight:: console

Installation
============

This part of the documentation covers how to install the package.
It is recommended to install the package in a virtual environment.


Create virtual environment
--------------------------
There are several packages/modules for creating python virtual environments.
Here is a
`manual <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`__
by the PyPA.


Installation from PyPI
----------------------

You can simply install the package from PyPI::

    $ pip install {{cookiecutter.project_slug}}


Installation from source
------------------------
You can install ``{{cookiecutter.project_slug}}`` directly from a Git repository clone.
This can be done either by cloning the repository and installing from the local clone::

    $ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.git
    $ cd {{cookiecutter.project_slug}}
    $ pip install .


Or installing directly via git::

    $ pip install git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.git


You can also download the current version as `tar.gz` or `zip` file, extract it and
install it with pip like above.

.. highlight:: default
