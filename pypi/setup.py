# -*- coding: utf-8 -*-
# python setup.py register sdist upload
from setuptools import setup

import os
f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name = 'PyMCP2221A',
    version = '1.0.6',
    url="https://github.com/nonNoise/PyMCP2221A",
    keywords = ('Hardware,USB,HID,MCP2221,I2C,GPIO'),
    description = 'This is a Microchip MCP2221(A) HID Library in python(3).',
    license = 'MIT License',
    install_requires = ["hidapi"],
    long_description=long_description,
    packages=['PyMCP2221A'],
    author = ' Yuta KItagami',
    author_email = 'kitagami@artifactnoise.com',
    platforms = ['Linux','Windows','Mac'],
)
