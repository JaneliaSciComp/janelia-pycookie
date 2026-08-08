"""{{ cookiecutter.project_short_description }}"""

from importlib.metadata import PackageNotFoundError, version

from ._example import greet

try:
    __version__ = version("{{ cookiecutter.project_name }}")
except PackageNotFoundError:  # package is not installed
    __version__ = "uninstalled"

# Everything listed here becomes the public API and gets an API docs page.
# Implementation lives in underscore-prefixed modules; see CONTRIBUTING.md.
__all__ = ["__version__", "greet"]
