#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib, os

class User(object):

    def __init__(self):
        self.username = None
        self.passwd_hash = None

    def set_password(self, password):
        salt = os.urandom(8)
        self.passwd_hash = hashlib.md5(salt + password.encode()).hexdigest() + b':' + salt

    def check_passwd(self, tobechecked):
        passwd_hash, salt = self.passwd_hash.split(b':')
        result = hashlib.md5(salt + tobechecked.encode()).hexdigest()
        return result == passwd_hash

if __name__ == '__main__':
    user = User()
    user.set_password('apple')
    print user.check_passwd('apple') or 'Wrong password'
    print user.check_passwd('pear') or 'Wrong password'
    print user.check_passwd('man') or 'Wrong password'
    user.set_password('pear')
    print user.check_passwd('apple') or 'Wrong password'
    print user.check_passwd('pear') or 'Wrong password'
    print user.check_passwd('man') or 'Wrong password'


