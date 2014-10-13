#!/usr/bin/env python
"""
sentry-bearychat
============

An extension for `Sentry <https://getsentry.com>`_ which posts notifications to `Bearychat <https://bearychat.com>`_.

:copyright: (c) 2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=5.0.0',
]

setup(
    name='sentry-bearychat',
    version='0.1.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductons.com',
    url='https://github.com/getsentry/sentry-bearychat',
    description='A Sentry extension which posts notifications to Bearychat (https://bearychat.com/).',
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
            'bearychat = sentry_bearychat.plugin:BearychatPlugin',
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
