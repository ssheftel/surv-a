
# -*- coding: utf-8 -*-

"""
"""

from eve import Eve
from eve.auth import BasicAuth
from werkzeug.security import check_password_hash
from flask import current_app as app

class RolesAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        peoples = app.data.driver.db['people']
        person = peoples.find_one({'username': username})
        if resource in {'people'}:
            if method in {'POST', 'DELETE', 'PATCH', 'PUT'}:
                return person.get('admin', False)
        # if allowed_roles:
        #     # only retrieve a user if his roles match ``allowed_roles``
        #     lookup['roles'] = {'$in': allowed_roles}
        # account = accounts.find_one(lookup)
        # return account and check_password_hash(account['password'], password)
