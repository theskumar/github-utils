#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="github-utils",
    version="0.1.0",
    author="Saurabh Kumar",
    author_email="me@saurabh-kumar.com",
    packages=[
        "github-utils",
    ],
    include_package_data=True,
    install_requires=[
        "github3.py==0.9.3"
    ],
    zip_safe=False,
    scripts=["github-utils/github-repos.py"],
)
