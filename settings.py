
# -*- coding: utf-8 -*-

"""
"""

import os

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = int(os.environ.get('MONGO_PORT'))
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')

PUBLIC_METHODS = ['GET']

# Disable XML - cause it sucks
XML = False

people = {
    'schema': {
        'name': {'type': 'string', 'required': True},
        'admin': {'type': 'boolean', 'default': False},
        'manager': {'type': 'string', 'default': ''}
    },
    'public_methods': ['GET']
}

serve

DOMAIN = {}

