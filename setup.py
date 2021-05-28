# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""
from setuptools import setup
import versioneer

with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')


setup(
    name='pyskel',
    packages=['pyskel', 'pyskel.scripts', 'pyskel.configobj'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['pyskel = pyskel.scripts.pyskel:main']
        },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='A short description',
    long_description=long_descr,
    long_description_content_type='text/markdown',
    author='Author Name',
    author_email='author@email.com',
    url='http://mypage.com',
    license='CeCILL Free Software License Agreement, Version 2.1',
    platforms='OS Independent',
    classifiers=[
            'Development Status :: Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre '
                'License, version 2.1 (CeCILL-2.1)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Physics'],
    install_requires=[],
    python_requires='>3.7'
    )
