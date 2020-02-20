{% if cookiecutter.command_line_interface|lower == 'click' -%}
# ======================================================================================
# Copyright (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
#
# This file 'conf.py' created {{ cookiecutter.iso_date }}
# is part of the project/program '{{ cookiecutter.project_name }}'.
{% if cookiecutter.license == "GPL-3.0" -%}
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
{% elif cookiecutter.license == "LGPL-3.0" -%}
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
{% elif cookiecutter.license == "MIT" -%}
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by
# the Massachusetts Institute of Technology.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# MIT License for more details.
#
# You should have received a copy of the MIT License
# along with this program. If not, see <https://opensource.org/licenses/MIT>.
{% elif cookiecutter.license == "BSD3" -%}
# This program is free software: you can redistribute it and/or modify
# it under the terms of the BSD 3-Clause License as published by
# the Regents of the University of California.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# BSD 3-Clause License for more details.
#
# You should have received a copy of the BSD 3-Clause License
# along with this program. If not, see <https://opensource.org/licenses/BSD-3-Clause>.
{% endif -%}
#
# Github: https://github.com/{{ cookiecutter.github_username }}/
# ======================================================================================
"""
    {{cookiecutter.project_slug}}.cli
    {% for _ in cookiecutter.project_slug %}~{% endfor %}~~~~

    Console script for {{cookiecutter.project_slug}}

    {% if cookiecutter.license != "Not open source" -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    :license: {{ cookiecutter.license }}, see LICENSE.rst for more details
    {%- else -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    {%- endif %}
"""
import sys

import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
{% endif -%}
