# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    response.flash = T("Hello People UD")
    return locals();

@auth.requires_membership('administrador')
def register_course():
    form = SQLFORM(db1.course).process()
    if form.accepted:
        session.flash = T("Course Create!")
        redirect(URL('index'))
    return locals()

@auth.requires_login()
@auth.requires_membership('administrador')
def agree_teacher():
    rows = db1(db1.auth_user.registration_key=='pending').select()
    return locals()


def show_teacher():
    user = db1.auth_user(request.args(0, cast=int))
    user.update(registration_key='')
    db1.auth_user.first_name.writable = False
    db1.auth_user.first_name.reable = False
    db1.auth_user.last_name.writable = False
    db1.auth_user.last_name.reable = False
    form = SQLFORM(db1.auth_user, user, deletable=True, showid=False)

    if form.process(next=URL('update_group_teacher', args=user.id)).accepted:        
        response.flash = T ('Teacher accepted')        
    elif form.errors:
        response.flash = T ('Teacher No Update')
    

    
    return locals()

def update_group_teacher():
    member = db1.auth_membership(request.args(0, cast=int))
    member.update(group_id=2)
    db1.auth_membership.user_id.writable = False
    db1.auth_membership.user_id.reable = False
    db1.auth_membership.group_id.writable = False
    db1.auth_membership.group_id.reable = False    
    form = SQLFORM(db1.auth_membership, member, showid=False)
    
    if form.process().accepted:        
        response.flash = T ('User Agree to Teacher Group')        
    elif form.errors:
        response.flash = T ('Group No Update')

    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
