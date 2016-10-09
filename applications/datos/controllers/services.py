# -*- coding: utf-8 -*-
# essayez quelque chose comme
import evaluar_expresion


def index(): return dict(message="hello from services.py")


@auth.requires_login()
def services():
    ids = request.vars["ids"]
    variables_extra = dict( remote='all', action='check')
    
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='services', variables_extra = variables_extra, is_debug=True)))
    return dict()

@auth.requires_login()
def start_services():
    services = []
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('services', label='Services', requires=IS_NOT_EMPTY()),
    ).process()

    if form.accepted:
        services = request.vars.services
        services = evaluar_expresion.separar_x_comas(services)
    
        variables_extra = dict( remote='all', action='start', services=services)
    
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='services', variables_extra = variables_extra)))
    return locals()


@auth.requires_login()
def stop_services():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('services', label='Services', requires=IS_NOT_EMPTY()),
    ).process()

    if form.accepted:
        services = request.vars.services
        services = evaluar_expresion.separar_x_comas(services)
    
        variables_extra = dict( remote='all', action='stop', services=services)
    
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='services', variables_extra = variables_extra)))
    return locals()


@auth.requires_login()
def restart_services():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('services', label='Services', requires=IS_NOT_EMPTY()),
    ).process()

    if form.accepted:
        services = request.vars.services
        services = evaluar_expresion.separar_x_comas(services)
    
        variables_extra = dict( remote='all', action='restart', services=services)
    
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='services', variables_extra = variables_extra)))
    return locals()

@auth.requires_login()
def reload_services():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('services', label='Services', requires=IS_NOT_EMPTY()),
    ).process()

    if form.accepted:
        services = request.vars.services
        services = evaluar_expresion.separar_x_comas(services)
    
        variables_extra = dict( remote='all', action='reload', services=services)
    
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='services', variables_extra = variables_extra)))
    return locals()
