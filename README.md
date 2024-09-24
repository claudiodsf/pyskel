# Pyskel

An empty Python installable project to bootstrap new code development.

Features:

- Installable using `pip` (or `pip -e` for editable mode);
- A `tar.gz` archive and a Python wheel can be built using `python -m build`;
- The Python wheel can be uploaded to PyPI via `twine`;
- Automated versioning via
  [python-versioneer](https://github.com/python-versioneer/python-versioneer);
- Configuration file support via
  [configobj](https://github.com/DiffSK/configobj) (embedded).

Use the provided script `set_package_and_author.py` to change the name of the
package, and the author's name and email.
