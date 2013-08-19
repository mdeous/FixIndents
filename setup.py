#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

import fixindents


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read().strip()
DEPENDENCIES = ['distribute']


setup(
    name=fixindents.NAME,
    version=fixindents.VERSION,
    description=fixindents.DESC,
    long_description=README,
    author=fixindents.AUTHOR,
    author_email='mattoufootu@gmail.com',
    url='https://github.com/mattoufoutu/FixIndents',
    zip_safe=False,
    license='MIT',
    keywords='indentation indent tab space convert',
    install_requires=DEPENDENCIES,
    package_dir={'': '.'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': ['fixindents = fixindents:main']
    }
)
