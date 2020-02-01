{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

| |license| |black|
|
| |travis| |appveyor| |codecov|
| |docs| |reqs|
|
| |py_versions| |implementations|
| |pypi| |status| |format| |wheel| |downloads|
|
| |release| |commits_since| |last_commit|
| |stars| |forks| |contributors|
|


{{ cookiecutter.project_short_description }}

{% if cookiecutter.license != 'Not open source' -%}
Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.

{% endif %}
.. .############################### LINKS ###############################

.. BADGES START

.. info block
.. |license| image:: https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}.svg?style=flat-square
    :alt: License
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/blob/master/LICENSE.rst

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square
    :alt: Code Style: Black
    :target: https://github.com/psf/black


.. tests block
.. |travis| image:: https://img.shields.io/travis/com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/master.svg?style=flat-square&logo=travis-ci&logoColor=FBE072
    :alt: Travis - Build Status
    :target: https://travis-ci.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}

.. |appveyor| image:: https://img.shields.io/appveyor/ci/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/master.svg?style=flat-square&logo=appveyor
    :alt: AppVeyor - Build Status
    :target: https://ci.appveyor.com/project/Cielquan/pytest-cov

.. |codecov| image:: https://img.shields.io/codecov/c/github/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/master.svg?style=flat-square&logo=codecov
    :alt: Codecov - Test Coverage
    :target: https://codecov.io/gh/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}

.. |docs| image:: https://img.shields.io/readthedocs/{{cookiecutter.project_slug}}/latest.svg?style=flat-square&logo=read-the-docs&logoColor=white
    :alt: Read the Docs (latest) - Status
    :target: https://python-test-cielquan.readthedocs.io/en/latest/?badge=latest

.. |reqs| image:: https://img.shields.io/requires/github/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}.svg?style=flat-square
    :alt: Requires.io - Requirements status
    :target: https://requires.io/github/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/requirements/?branch=master


.. PyPI block
.. |py_versions| image:: https://img.shields.io/pypi/pyversions/coverage.svg?style=flat-square&logo=python&logoColor=FBE072
    :alt: PyPI - Python versions supported
    :target: https://pypi.org/project/{{cookiecutter.project_slug}}/

.. |implementations| image:: https://img.shields.io/pypi/implementation/coverage.svg?style=flat-square&logo=python&logoColor=FBE072
    :alt: PyPI - Implementations supported
    :target: https://pypi.org/project/{{cookiecutter.project_slug}}/

.. |pypi| image:: https://img.shields.io/pypi/v/coverage.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :alt: PyPI - Package latest release
    :target: https://pypi.org/project/{{cookiecutter.project_slug}}/

.. |status| image:: https://img.shields.io/pypi/status/coverage.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :alt: PyPI - Package stability
    :target: https://pypi.org/project/{{cookiecutter.project_slug}}/

.. |format| image:: https://img.shields.io/pypi/format/coverage.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :alt: PyPI - Format
    :target: https://pypi.org/project/{{cookiecutter.project_slug}}/

.. |wheel| image:: https://img.shields.io/pypi/wheel/coverage.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :alt: PyPI - Wheel
    :target: https://pypi.org/project/{{cookiecutter.project_slug}}/

.. |downloads| image:: https://img.shields.io/pypi/dm/coverage.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/{{cookiecutter.project_slug}}/
    :alt: PyPI - Monthly downloads


.. Github block
.. |release| image:: https://img.shields.io/github/v/release/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}.svg?style=flat-square&logo=github
    :alt: Github Latest Release
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/releases/latest

.. |commits_since| image:: https://img.shields.io/github/commits-since/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/latest.svg?style=flat-square&logo=github
    :alt: GitHub commits since latest release
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/commits/master

.. |last_commit| image:: https://img.shields.io/github/last-commit/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}.svg?style=flat-square&logo=github
    :alt: GitHub last commit
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/commits/master

.. |stars| image:: https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}.svg?style=flat-square&logo=github
    :alt: Github stars
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/stargazers

.. |forks| image:: https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}.svg?style=flat-square&logo=github
    :alt: Github forks
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/network/members

.. |contributors| image:: https://img.shields.io/github/contributors/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}.svg?style=flat-square&logo=github
    :alt: Github Contributors
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_slug}}/graphs/contributors

..  BADGES END
