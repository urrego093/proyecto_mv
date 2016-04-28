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

def register_machine():
    form = SQLFORM(db1.machine).process()
    if form.accepted:
        registrar_host(form.vars.id)
        session.flash = T(" Machine Create!")
        redirect(URL('index'))
    return locals()

def registrar_host(id_machine):
    for row in P_HOST:
        db1.port_machine.insert(ip_machine=id_machine, number_port=row)
        db1.commit()
    
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
    member = db1.auth_membership(request.args(0, cast=int) or redirect(URL('index')))
    if member:
        member.update(group_id=2)
        db1.auth_membership.user_id.writable = False
        db1.auth_membership.user_id.reable = False
        db1.auth_membership.group_id.writable = False
        db1.auth_membership.group_id.reable = False    
        form = SQLFORM(db1.auth_membership, member, showid=False)

        if form.process().accepted:        
            response.flash = T ('User Agree to Teacher Group')
            redirect(URL('agree_teacher'))
        elif form.errors:
            response.flash = T ('Group No Update')
    else:
        redirect(URL('index'))
    return locals()

def mostrar_macxuser():
    course = db1.course(request.args(1, cast=int) or redirect(URL('index')))
    machine = db1.machine(request.args(0, cast=int) or redirect(URL('index')))
    c_group = db1((db1.course_group.cod_course==course.id)& (db1.course_group.id_teacher==auth.user_id)).select()
    return locals()


def show_couxuser():
    course = db1.course(request.args(0, cast=int) or redirect(URL('index')))
    c_machine= db1((db1.machine.code_course==course.id)).select()
    return locals()

def show_ports():
    semes = request.args(0)
    course = db1.course(request.args(2, cast=int) or redirect(URL('index')))
    machine = db1.machine(request.args(1, cast=int) or redirect(URL('index')))
    num_group = request.args(3) or redirect(URL('index'))
    port_mac = db1(db1.port_machine.ip_machine==machine.id).select()
    response.flash = T (num_group)
    list_port = []
    
    for port_m in port_mac:
        list_est = db1((db1.student_x_machine.ip_machine==port_m.id) &
                       (db1.student_x_machine.semester==semes)).select(db1.student_x_machine.name_student, db1.student_x_machine.code_student)
        for l_est in list_est:
            list_port.append((port_m.number_port, port_m.hostname, l_est.code_student, l_est.name_student))

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
