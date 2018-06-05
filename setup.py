#!/usr/bin/env python

from contracts import contract, new_contract
from setuptools import setup, find_packages
import os

# Code From: https://pythonhosted.org/an_example_pypi_project/setuptools.html
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

new_contract('valid_fname', lambda fname: isinstance(fname, str) and len(fname)>0)
new_contract('valid_read_return', lambda read_return: isinstance(read_return, str) and len(read_return)>0)
@contract(fname='valid_fname', returns='valid_read_return')
def read(fname):
    read_return = open(os.path.join(os.path.dirname(__file__), fname)).read()
    return read_return

REQUIREMENTS = []
EXCLUDE_FROM_PACKAGES = []

setup(
    name='diskspace',
    version='0.0.1',
    url='https://github.com/matheusfaria/diskspace',
    author='Matheus Faria',
    author_email='matheus.sousa.faria@gmail.com',
    description='Command to analyze how much each file occupies in a folder',
    license='LICENSE.txt',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    entry_points={'console_scripts': [
        'diskspace = diskspace.diskspace:main',
    ]},
    long_description=read('README.md'),
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Shells',
    ],
)
