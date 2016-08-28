# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def index(): 
    return locals()

@auth.requires_login()
def users():
    return locals()

@auth.requires_login()
def system():
    return locals()

@auth.requires_login()
def files():
    return locals()
