# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup

VERSION = '0.1.0.post1'


def get_long_description():
    desc = ''
    with open('README.rst') as f:
        desc = f.read()
    return desc


setup(
    name='mccabe-console-script',
    version=VERSION,
    description='Console script for the McCabe checker',
    long_description=get_long_description(),
    keywords='flake8 mccabe',
    author='Ian Cordasco',
    author_email='graffatcolmingov@gmail.com',
    url='https://gitlab.com/pycqa/mccabe-console-script',
    license='Expat license',
    install_requires=['mccabe >= 0.3'],
    entry_points={
        'console_scripts': [
            'mccabe = mccabe:main',
        ],
    },
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
