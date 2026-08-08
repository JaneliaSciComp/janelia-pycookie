"""Validate the answers before anything is written to disk.

`project_name` has no default, so an empty value is easy to produce with
`--no-input`. Cookiecutter's own failure for that case is an opaque
`"." directory already exists`, so check it here and say what is actually wrong.
"""

import re
import sys

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
GITHUB_OWNER = "{{ cookiecutter.github_owner }}"

# A valid Python identifier for each dotted segment: the slug becomes the
# import name, so `import <slug>` has to work.
SLUG_PATTERN = re.compile(r"^[a-z_][a-z0-9_]*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not PROJECT_NAME.strip():
        fail("project_name must not be empty (it is the distribution name on PyPI).")

    if not SLUG_PATTERN.match(PROJECT_SLUG):
        fail(
            f"project_slug {PROJECT_SLUG!r} is not a valid Python identifier. "
            "Use lowercase letters, digits and underscores, starting with a "
            "letter or underscore."
        )

    if not GITHUB_OWNER.strip():
        print(
            "WARNING: github_owner is empty, so the repository, documentation "
            "and badge URLs will be incomplete.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
