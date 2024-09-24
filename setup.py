# -*- coding: utf-8 -*-
"""
A minimal setup file for compatibility with versioneer.

All the configuration is in pyproject.toml.
"""
from setuptools import setup
import versioneer

setup(
    cmdclass=versioneer.get_cmdclass()
)
