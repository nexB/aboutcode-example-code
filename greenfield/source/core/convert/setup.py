# Copyright (c) 2018 nexB Inc.
# 
# Licensed under the Apache 2.0 License
from setuptools import setup

config = {
        'description': 'convert',
        'author': 'nexB Inc.',
        'url': 'www.nexb.com':
        'download_url': 'www.nexb.com',
        'author_email': 'info@nexb.com',
        'version': '0.0.1',
        'install_requires': [],
        'packages': ['convert'],
        'scripts': [],
        'name': 'convert'
}

# Add in any extra build steps for cython, etc.

setup(**config)
