#!/usr/bin/env python
import os
from codecs import open

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'r', 'utf-8') as handle:
    readme = handle.read()

setup(
    name='classmaker',
    version='0.1',
    description='Make complex classes compatible with both python 2 and 3',
    long_description=readme,
    author='Michele Simionato, David Park',
    url='http://github.com/daphtdazz/classmaker',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'six'
    ],
    extras_require={
        'develop': [
            "flake8>=3.2.1",
            "pytest"
        ],
        'docs': [
        ],
    },
    entry_points={
    },
    zip_safe=True,
    license='PSF license',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ]
)
