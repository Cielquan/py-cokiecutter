# noqa: D205,D208,D400
"""
    {{cookiecutter.project_slug}}
    {{ "~" * cookiecutter.project_slug|length }}

    {{cookiecutter.project_short_description}}

    {% if cookiecutter.license != "Not open source" -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    :license: {{ cookiecutter.license }}, see LICENSE.rst for more details
    {%- else -%}
    :copyright: (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
    {%- endif %}

    This file is part of the project/program
    '{{ cookiecutter.project_name }}'.
{%- if cookiecutter.license == "GPL-3.0" %}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
{%- elif cookiecutter.license == "LGPL-3.0" %}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
{%- elif cookiecutter.license == "MIT" %}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the MIT License as published by
    the Massachusetts Institute of Technology.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    MIT License for more details.

    You should have received a copy of the MIT License
    along with this program. If not, see <https://opensource.org/licenses/MIT>.
{%- elif cookiecutter.license == "BSD3" %}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the BSD 3-Clause License as published by
    the Regents of the University of California.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    BSD 3-Clause License for more details.

    You should have received a copy of the BSD 3-Clause License
    along with this program. If not, see <https://opensource.org/licenses/BSD-3-Clause>.
{%- endif %}
"""
try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version  # type: ignore

__version__ = version(__name__)
