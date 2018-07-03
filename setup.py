#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='ansible-satellite6',
    version='0.0.1',
    description='Ansible-based tools to help automating testing Foreman with Robottelo.',
    long_description=readme,
    author=u'TBD',
    author_email='TBD',
    url='https://github.com/SatelliteQE/ansible-satellite6',
    packages=['automation_tools', 'automation_tools/satellite6'],
    package_data={'': ['LICENSE']},
    package_dir={'automation_tools': 'automation_tools'},
    include_package_data=True,
    install_requires=[
        'pytest',
        'ansible-runner'
    ],
    license='GNU GPL v3.0',
    classifiers=(
        'Development Status :: 1 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
)
