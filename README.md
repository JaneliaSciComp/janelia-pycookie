# pycookie

A cookie cutter repository for setting up Python libraries/repositories.


## Quickstart

```
uvx cookiecutter https://github.com/JaneliaSciComp/janelia-pycookie/
```

## What you get

A `src/`-layout Python package wired up with:

| Area | Tool |
| --- | --- |
| Environment / packaging | [uv](https://docs.astral.sh/uv/) with PEP 735 `[dependency-groups]`; `uv.lock` is committed |
| Build backend | setuptools + setuptools-scm (version from git tags) |
| Task runner | [just](https://just.systems) |
| Lint + format | [ruff](https://docs.astral.sh/ruff/) (line length 100) |
| Type checking | mypy (`strict`), `py.typed` |
| Testing | pytest + pytest-cov, warnings as errors |
| Docs | mkdocs-material + mkdocstrings + mkdocs-api-autonav, versioned with mike |
| Hooks | pre-commit (typos, ruff, validate-pyproject, mypy) |
| CI | GitHub Actions: test matrix (3 OSes x supported Pythons x `highest`/`lowest-direct`), mypy, codecov, tag -> PyPI, docs to gh-pages |
| Dependencies | Dependabot PRs for in-range bumps; a monthly issue reporting releases held back by upper bounds |

## Prerequisites

To generate a project you need:

- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — provides
  `uvx`, which runs cookiecutter without installing it. If you would rather not
  use uv, any other cookiecutter install works too (`pipx install cookiecutter`,
  `pip install cookiecutter`); just drop the `uvx` prefix from the commands below.
- **git** — cookiecutter clones the template from its URL.

To work in the generated project you also need:

- **uv** — dependency management (`uv sync`, `uv run`).
- **git** — `setuptools-scm` derives the version from tags, and the pre-commit
  hooks need a repository.
- **[just](https://just.systems/man/en/packages.html)** — the task runner. It is
  a convenience wrapper; every recipe is a one-line `uv run ...` you can copy out
  of the `justfile` and run directly if you would rather not install it.

Everything else (ruff, mypy, pytest, mkdocs, pre-commit) is declared in the
generated `pyproject.toml` and installed by `uv sync`.


## Prompts

| Variable | Description |
| --- | --- |
| `full_name` / `email` | Package author metadata. No default — you must fill these in |
| `github_owner` | The user or organization the repo lives under. Used for repo, docs and badge URLs. Defaults to `JaneliaSciComp` |
| `project_name` | Distribution name on PyPI |
| `project_slug` | Import name (defaults to a normalized `project_name`) |
| `project_short_description` | Used in the docstring, README and package metadata |
| `minimum_python_version` | Lowest supported Python; sets `requires-python`, ruff `target-version`, classifiers and the CI matrix |
| `copyright_holder` | Copyright holder in `LICENSE`; defaults to HHMI Janelia Research Campus |
| `year` | Copyright year in `LICENSE` |
| `host_docs_on_github_io` | Include the mkdocs setup and docs workflow. Only valid for public repos — GitHub Pages from a `gh-pages` branch requires a paid plan on private repos |
| `publish_to_pypi` | Include the PyPI build-and-publish step in the release job |

Projects are BSD 3-Clause licensed (the Janelia standard); this is not a prompt.

Answering `no` to either question removes the corresponding configuration
entirely rather than leaving it inert:

- **`host_docs_on_github_io: no`** — drops `mkdocs.yml`, `docs/`, the docs
  workflow, the `docs` dependency group, the `docs-serve` / `docs-build`
  recipes, the documentation URL and the docs badge.
- **`publish_to_pypi: no`** — drops the build and publish steps, the
  `id-token` permission and the PyPI badge. Tags still cut a GitHub release,
  and `just build` still produces a wheel locally.

## After generating

```
cd <project_slug>
git init && git add -A && git commit -m "initial commit"
just install     # uv sync + install pre-commit hooks
just             # list all available recipes
```
And push to GitHub.

A few things need one-time setup on the hosting side:

- **PyPI publishing** (if enabled) uses
  [trusted publishing](https://docs.pypi.org/trusted-publishers/), which must be
  configured for the project on PyPI.
- **Docs** (if enabled) are deployed to the `gh-pages` branch by `mike`; enable
  GitHub Pages for that branch.
- **Codecov** works out of the box for public repos; private repos need a
  `CODECOV_TOKEN` secret.
- Releases are cut by pushing a tag: `just release v0.1.0`.
