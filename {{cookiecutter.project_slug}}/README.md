# {{ cookiecutter.project_name }}

[![CI](https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }})
{%- if cookiecutter.publish_to_pypi == "yes" %}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }})
{%- endif %}
{%- if cookiecutter.host_docs_on_github_io == "yes" %}
[![docs](https://img.shields.io/badge/docs-latest-blue.svg)](https://{{ cookiecutter.github_owner }}.github.io/{{ cookiecutter.project_slug }}/)
{%- endif %}

{{ cookiecutter.project_short_description }}

## Installation

{% if cookiecutter.publish_to_pypi == "yes" -%}
```bash
pip install {{ cookiecutter.project_name }}
```
{%- else -%}
```bash
pip install git+https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}
```
{%- endif %}

## Development

This project uses [uv](https://docs.astral.sh/uv/) and
[just](https://just.systems). To set up a development environment:

```bash
git clone https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
just install
```

See [CONTRIBUTING.md](https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/blob/main/CONTRIBUTING.md)
for more, or run `just` to list all available recipes.
