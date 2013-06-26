#!/usr/bin/env python
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

setup(
    name='django-qsstats-magic',
    version='0.8.0',
    description='A django microframework that eases the generation of aggregate data for querysets.',
    long_description = open('README.rst').read(),
    author='Matt Croydon, Mikhail Korobov, Abd Allah Diab',
    author_email='mcroydon@gmail.com, kmike84@gmail.com, mpcabd@gmail.com',
    url='https://github.com/mpcabd/django-qsstats-magic/',
    packages=['qsstats'],
    requires=['dateutil(>=1.4.1, < 2.0)'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
