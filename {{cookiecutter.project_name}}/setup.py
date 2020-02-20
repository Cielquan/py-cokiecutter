"""Setup"""
import setuptools


setuptools.setup(
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "write_to": "src/{{cookiecutter.project_slug}}/version.py",
        "write_to_template": "__version__ = {version!r}",
    },
)
