#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages

setup(
    name="github-utils",
    version="0.1.0",
    author="Saurabh Kumar",
    author_email="me@saurabh-kumar.com",
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    install_requires=[
        "github3.py==0.9.3"
    ],
    zip_safe=False,
    scripts=["github-utils/github-repos.py"],
)
