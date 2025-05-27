#!/usr/bin/env python

from setuptools import setup

# Version info -- read without importing
# TODO: what's the modern method for this? it used to be pkg-utils or
# project_metadata? in tandem with...moving version to be static? that seems
# arguably best (have runtime know how to source this info from packaging
# metadata one way or another)?
_locals = {}
with open("lexicon/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

setup(
    version=version,
)
