# Pyskel

An empty Python installable project to bootstrap new code development.

Features:

 - Installable using `pip`;
 - Distributable using `python setup.py sdist` (`tar.gz` archive) and `python
   setup.py bdist_wheel` (python wheel);
 - The python wheel can be uploaded to PyPI via `twine`;
 - Automated versioning via
   [python-versioneer](https://github.com/python-versioneer/python-versioneer)
   (embedded);
 - Configuration file support via
   [configobj](https://github.com/DiffSK/configobj) (embedded).