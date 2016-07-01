# -*- coding: utf-8 -*-
# intente algo como
#def index(): return dict(message="hello from usuarios.py")
import evaluar_expresion

@auth.requires_login()
def crear():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('user_name', label='User name', requires=IS_NOT_EMPTY()),
        Field('password', 'password', label='Password', requires=[IS_LENGTH(minsize=6), IS_STRONG(min=6,special=0, upper=1)]),
        Field('confirm_password', 'password', label='Confirm password', requires=[
                IS_STRONG(min=6, special=0, upper=1), IS_EQUAL_TO(request.vars.password, error_message='passwords do not match')]),
        Field('admin', 'boolean', label='Admin')
    ).process()

    if form.accepted:
        name = request.vars.user_name
        name = evaluar_expresion.evaluar(name)

        password = request.vars.password
        admin = 'yes' if request.vars.admin else 'no'

        variables_extra = dict( remote='all', username=name, password=password, admin=admin, action="create_user")
        #redirect(URL('mostrar'))
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='user', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario

    return dict(form=form)

@auth.requires_login()
def eliminar_usuario():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('user_name', label=T('User name'), requires=IS_NOT_EMPTY())
    ).process()

    if form.accepted:
        name = request.vars.user_name
        name = evaluar_expresion.evaluar(name)
        print 'NAME ES :' , name
        variables_extra = dict( remote='all', username=name, action='delete_user')
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion="user", variables_extra = variables_extra)))
    return dict(form= form)


@auth.requires_login()
def cambiar_pass():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('user_name', label='User name', requires=IS_NOT_EMPTY()),
        Field('password', 'password', label='Password', requires=[IS_LENGTH(minsize=6), IS_STRONG(min=6,special=0, upper=1)]),
        Field('confirm_password', 'password', label='Confirm password', requires=[
                IS_STRONG(min=6, special=0, upper=1), IS_EQUAL_TO(request.vars.password, error_message='passwords do not match')])
    ).process()

    if form.accepted:
        name = request.vars.user_name
        name = evaluar_expresion.evaluar(name)

        password = request.vars.password

        variables_extra = dict( remote='all', username=name, password=password, action="change_pass")
        #redirect(URL('mostrar'))
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='user', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario
    return locals()
