#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='git-dlist',
    version='0.1',
    description='Small tool to keep a directory of git repositories in sync.',
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='http://github.com/mbr/gitlist',
    license='MIT',
    packages=find_packages(exclude=['test']),
    install_requires=['colorama'],
    entry_points={
        'console_scripts': [
            'git-dlist = gitdlist:main',
        ],
    }
)
