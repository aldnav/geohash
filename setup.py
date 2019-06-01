#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['cffi>=1.12.3']

setup_requirements = ['pytest-runner', 'cffi']

test_requirements = ['pytest', ]

setup(
    author="Aldrin Navarro",
    author_email='aldrinnavarro16@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Encode/decode Geohashes http://geohash.org",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='geohash',
    name='geohashcx',
    packages=find_packages(include=['geohash']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/aldnav/geohash',
    version='0.1.3',
    zip_safe=False,
    cffi_modules=["geohash/geohash_build.py:ffi"],  # @TODO: cffi_modules here
)
