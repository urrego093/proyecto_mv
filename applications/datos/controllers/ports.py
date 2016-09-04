# -*- coding: utf-8 -*-
# essayez quelque chose comme
import evaluar_expresion


def index(): return dict(message="hello from ports.py")


@auth.requires_login()
def ports():
    ids = request.vars["ids"]
    variables_extra = dict( remote='all', action='check')
    
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='ports', variables_extra = variables_extra, is_debug=True)))
    return dict()

@auth.requires_login()
def open_ports():
    ids = request.vars["ids"]
    form = SQLFORM.factory(  Field('ports', label='Ports', requires=IS_NOT_EMPTY())).process()
    form['_align'] = "center"
    if form.accepted:
        puertos = request.vars.ports
        puertos = evaluar_expresion.separar_x_comas(puertos)
        #servicio = 'yes' if request.vars.servicio else 'no'
        variables_extra = dict( remote='all', action='open', puertos=puertos)
    
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='ports', variables_extra = variables_extra)))
    return locals()

@auth.requires_login()
def close_ports():
    ids = request.vars["ids"]
    form = SQLFORM.factory(  Field('ports', label='Ports', requires=IS_NOT_EMPTY())).process()
    form['_align'] = "center"
    if form.accepted:
        puertos = request.vars.ports
        puertos = evaluar_expresion.separar_x_comas(puertos)
        #servicio = 'yes' if request.vars.servicio else 'no'
        variables_extra = dict( remote='all', action='close', puertos=puertos)
    
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='ports', variables_extra = variables_extra)))
    return locals()
