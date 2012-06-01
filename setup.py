#!/usr/bin/env python

import os
import sys

# Support setuptools or distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Import ourselves for version info
import lexicon
v = lexicon.__version__

long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='lexicon',
    version=v,
    description='Powerful dict subclass(es) with aliasing & attribute access',
    license='BSD',

    long_description=long_description,
    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',
    url='https://github.com/bitprophet/lexicon',

    packages=["lexicon"],

    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
