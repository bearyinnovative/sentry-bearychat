#!/usr/bin/env python
"""
sentry-bearychat
================

An extension for `Sentry <https://getsentry.com>`_ which posts notifications to `BearyChat <https://bearychat.com>`_.

:copyright: (c) 2015 by the BearyInnovative Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=5.0.0',
]

setup(
    name='sentry-bearychat',
    version='0.2.1',
    author='BearyInnovative',
    author_email='info@bearyinnovative.com',
    url='https://github.com/bearyinnovative/sentry-bearychat',
    description='A Sentry extension which posts notifications to BearyChat (https://bearychat.com/).',
    keywords='bearychat sentry',
    long_description=open('README.rst').read(),
    license='BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'bearychat = sentry_bearychat',
        ],
        'sentry.plugins': [
            'bearychat = sentry_bearychat.plugin:BearyChatPlugin',
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
