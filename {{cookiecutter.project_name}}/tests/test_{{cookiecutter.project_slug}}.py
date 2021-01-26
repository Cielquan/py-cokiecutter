"""
    tests.test_{{cookiecutter.project_slug}}
    {{ "~" * (11 + cookiecutter.project_slug|length) }}

    Test for module: {{cookiecutter.project_slug}}

    :copyright: (c) {{cookiecutter.year}}, {{cookiecutter.full_name}} and AUTHORS
    :license: {{cookiecutter.license}}, see LICENSE for details
"""  # noqa: D205,D208,D400
from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}


def test_dummy() -> None:
    """Test a dummy to silence pytest exit code 5."""
    print({{cookiecutter.project_slug}})

    result = 1 + 1

    assert result == 2
