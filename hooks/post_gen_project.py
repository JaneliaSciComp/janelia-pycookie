"""Remove optional scaffolding that the user opted out of.

Cookiecutter can only conditionally render file *contents*, not skip files, so
anything that should disappear entirely is deleted here after generation.
"""

import shutil
from pathlib import Path

HOST_DOCS = "{{ cookiecutter.host_docs_on_github_io }}" == "yes"

DOCS_PATHS = [
    "mkdocs.yml",
    "docs",
    ".github/workflows/docs.yaml",
]


def remove(relative_path: str) -> None:
    path = Path(relative_path)
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def main() -> None:
    if not HOST_DOCS:
        for relative_path in DOCS_PATHS:
            remove(relative_path)


if __name__ == "__main__":
    main()
