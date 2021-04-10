#!/usr/bin/env python

import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as fd:
    long_description = fd.read()

setup(
    name="lexicon",
    version="2.0.0",
    description="Powerful dict subclass(es) with aliasing & attribute access",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Jeff Forcier",
    author_email="jeff@bitprophet.org",
    url="https://github.com/bitprophet/lexicon",
    project_urls={
        "Home": "https://github.com/bitprophet/lexicon#what",
        "Source": "https://github.com/bitprophet/lexicon",
        "Changelog": "https://github.com/bitprophet/lexicon/blob/main/CHANGES",
        "CI": "https://app.circleci.com/pipelines/github/bitprophet/lexicon",
    },
    packages=["lexicon"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
