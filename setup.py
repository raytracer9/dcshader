# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
import setuptools


with open('README.rst') as f:
    readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='dcshader',
    version='0.0.1',
    description='Datashader Helper',
    long_description=readme,
    author='M A',
    author_email='',
    url='https://github.com/raytracer9/dcshader',
    # license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)