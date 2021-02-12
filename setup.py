#!/usr/bin/env python

import os

# Support setuptools or distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fd:
    long_description = fd.read()

setup(
    name='lexicon',
    version="2.0.0",
    description='Powerful dict subclass(es) with aliasing & attribute access',
    license='BSD',
    long_description=long_description,
    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',
    url='https://github.com/bitprophet/lexicon',

    packages=["lexicon"],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
