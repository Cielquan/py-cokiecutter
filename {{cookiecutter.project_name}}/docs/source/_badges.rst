+-------------------+---------------------------------------------------------------------------------------------+
| **General**       | |maintenance_n| |license| |rtd|                                                             |
|                   +---------------------------------------------------------------------------------------------+
|                   | |semver|                                                                                    |
+-------------------+---------------------------------------------------------------------------------------------+
| **PyPI**          | |pypi_release| |pypi_py_versions| |pypi_implementations|                                    |
|                   +---------------------------------------------------------------------------------------------+
|                   | |pypi_status| |pypi_format| |pypi_downloads|                                                |
+-------------------+---------------------------------------------------------------------------------------------+
| **Pipeline**      | |gha_test_code| |codeclimate_cov|                                                           |
|                   +---------------------------------------------------------------------------------------------+
|                   | |gha_code_quality| |pre-commit-ci| |codeclimate_maintain|                                   |
|                   +---------------------------------------------------------------------------------------------+
|                   | |gha_test_docs| |gha_dep_safety|                                                            |
+-------------------+---------------------------------------------------------------------------------------------+
| **Github**        | |gh_release| |gh_commits_since| |gh_last_commit|                                            |
|                   +---------------------------------------------------------------------------------------------+
|                   | |gh_stars| |gh_forks| |gh_contributors| |gh_watchers|                                       |
+-------------------+---------------------------------------------------------------------------------------------+


.. Change badges in README also

.. General

.. Change maintenance status in README also

.. |maintenance_n| image:: https://img.shields.io/badge/Maintenance%20Intended-✖-red.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - not intended

.. |maintenance_y| image:: https://img.shields.io/badge/Maintenance%20Intended-✔-green.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - intended

.. |license| image:: https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.svg?style=flat-square&label=License
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/blob/main/LICENSE
    :alt: License

.. |rtd| image:: https://img.shields.io/readthedocs/{{cookiecutter.project_lower_case}}/latest.svg?style=flat-square&logo=read-the-docs&logoColor=white&label=Read%20the%20Docs
    :target: https://{{cookiecutter.project_lower_case}}.readthedocs.io/en/latest/
    :alt: Read the Docs - Build Status (latest)

.. |semver| image:: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square
    :target: https://semver.org/
    :alt: Semantic Versioning - 2.0.0


.. PyPI

.. |pypi_release| image:: https://img.shields.io/pypi/v/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/{{cookiecutter.project_lower_case}}/
    :alt: PyPI - Package latest release

.. |pypi_py_versions| image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=python&logoColor=FBE072
    :target: https://pypi.org/project/{{cookiecutter.project_lower_case}}/
    :alt: PyPI - Supported Python Versions

.. |pypi_implementations| image:: https://img.shields.io/pypi/implementation/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=python&logoColor=FBE072
    :target: https://pypi.org/project/{{cookiecutter.project_lower_case}}/
    :alt: PyPI - Supported Implementations

.. |pypi_status| image:: https://img.shields.io/pypi/status/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/{{cookiecutter.project_lower_case}}/
    :alt: PyPI - Stability

.. |pypi_format| image:: https://img.shields.io/pypi/format/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/{{cookiecutter.project_lower_case}}/
    :alt: PyPI - Format

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/{{cookiecutter.project_lower_case}}/
    :alt: PyPI - Monthly downloads


.. Pipeline

.. |gha_test_code| image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/Test%20code/main?style=flat-square&logo=github&label=Test%20code
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/actions?query=workflow%3A%22Test+code%22
    :alt: GitHub Actions - Test code

.. |codeclimate_cov| image:: https://img.shields.io/codeclimate/coverage/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}?style=flat-square&logo=code-climate
    :target: https://codeclimate.com/github/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}
    :alt: Code Climate - Coverage

.. |gha_code_quality| image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/Code%20qualitiy/main?style=flat-square&logo=github&label=Code%20qualitiy
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/actions?query=workflow%3A%22Code+qualitiy%22
    :alt: GitHub Actions - Code qualitiy

.. |pre-commit-ci| image:: https://results.pre-commit.ci/badge/github/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/main.svg
   :target: https://results.pre-commit.ci/latest/github/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/main
   :alt: pre-commit.ci status

.. |codeclimate_maintain| image:: https://img.shields.io/codeclimate/maintainability/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}?style=flat-square&logo=code-climate
    :target: https://codeclimate.com/github/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}
    :alt: Code Climate - Maintainability

.. |gha_test_docs| image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/Test%20documentation/main?style=flat-square&logo=github&label=Test%20documentation
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/actions?query=workflow%3A%22Test+documentation%22
    :alt: GitHub Actions - Test docs

.. |gha_dep_safety| image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/Dependency%20safety/main?style=flat-square&logo=github&label=Dependency%20safety
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/actions?query=workflow%3A%22Dependency+safety%22
    :alt: GitHub Actions - Dependency safety

.. TODO:#i# readd dependabot badge when https://github.com/dependabot/dependabot-core/issues/1912 is fixed

.. |dependabot| image:: https://api.dependabot.com/badges/status?host=github&repo=Cielquan/{{cookiecutter.project_lower_case}}
    :target: https://dependabot.com
    :alt: Dependabot status


.. GitHub

.. |gh_release| image:: https://img.shields.io/github/v/release/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=github
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/releases/latest
    :alt: Github - Latest Release

.. |gh_commits_since| image:: https://img.shields.io/github/commits-since/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/latest.svg?style=flat-square&logo=github
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/commits/main
    :alt: GitHub - Commits since latest release

.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=github
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/commits/main
    :alt: GitHub - Last Commit

.. |gh_stars| image:: https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=github
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/stargazers
    :alt: Github - Stars

.. |gh_forks| image:: https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=github
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/network/members
    :alt: Github - Forks

.. |gh_contributors| image:: https://img.shields.io/github/contributors/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=github
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/graphs/contributors
    :alt: Github - Contributors

.. |gh_watchers| image:: https://img.shields.io/github/watchers/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}.svg?style=flat-square&logo=github
    :target: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_lower_case}}/watchers/
    :alt: Github - Watchers
