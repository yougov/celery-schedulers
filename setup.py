#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='celery-schedulers',
    version='0.0.4',
    author='Brent Tubbs',
    author_email='brent.tubbs@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://bitbucket.org/btubbs/celery-schedulers',
    description='Celery scheduler backends for Redis and MongoDB',
    install_requires=[
        'six',
    ],
    tests_require=[
        'celery',
        'redis',
        'pymongo',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
