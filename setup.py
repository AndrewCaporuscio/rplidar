#!/usr/bin/env python3
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'rplidar-mrumel',
    py_modules = ['rplidar'],
    version = '1.1.2',
    description = 'Simple and lightweight module for working with RPLidar laser scanners',
    author='Merrick Rumel',
    author_email='merrick.rumel@fisherco.com',
    url='https://github.com/mrumel/rplidar',
    license='MIT',
    install_requires=['pyserial'],
    zip_safe=True,
    long_description='This module aims to implement communication protocol '
        'with RPLidar laser scanners. It\'s Python 2 and 3 '
        'compatible but was mainly tested using Python 3.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Hardware',
    ],
)
