#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='core-finance',
    version='0.0',
    description='',
    author='Ricardo Ribeiro',
    author_email='ricardo.ribeiro@research.fchampalimaud.org',
    packages=find_packages(),
    install_requires=['xlrd', 'openpyxl']
)
