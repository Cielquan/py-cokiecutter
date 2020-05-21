Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will
always install the most recent stable release.


From source
-----------

The source for {{ cookiecutter.project_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_lower_case }}

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_lower_case }}/tarball/master

Once you have a copy of the source, you can install directly with pip:

.. code-block:: console

    $ pip install .


You can also grab the repo in either `tar.gz`__ or `zip`__ format.
After downloading and extracting you can install it with :command:`pip` like above.


.. _Github repo: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_lower_case }}
.. _tarball: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_lower_case }}/tarball/master
.. __: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_lower_case }}/archive/master.tar.gz
.. __: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_lower_case }}/archive/master.zip
