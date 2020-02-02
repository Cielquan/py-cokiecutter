#!/usr/bin/env python3

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
    tests.test_{{cookiecutter.project_slug}}
    ~~~~~~~~~~~{% for _ in cookiecutter.project_slug %}~{% endfor %}

    Test for {{cookiecutter.project_slug}}

    {% if cookiecutter.license != "Not open source" -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    :license: {{ cookiecutter.license }}, see LICENSE.rst for more details
    {%- else -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    {%- endif %}
"""
{% if cookiecutter.command_line_interface|lower == "click" -%}
import pytest
from click.testing import CliRunner

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }} import cli
{% else -%}
import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{% endif -%}
{% if cookiecutter.command_line_interface|lower == 'click' %}

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{% endif -%}
