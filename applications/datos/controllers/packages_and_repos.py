# -*- coding: utf-8 -*-
# essayez quelque chose comme
import evaluar_expresion


def index(): return dict(message="hello from packages_and_repos.py")

@auth.requires_login()
def install_packages():
    ids = request.vars["ids"]
    accion = "install_packages"
    form = SQLFORM.factory(  Field('paquetes', label='Packages', requires=IS_NOT_EMPTY()) ).process()
    form['_align'] = "center"
    if form.accepted:
        paquetes = request.vars.paquetes
        paquetes = evaluar_expresion.separar_x_comas(paquetes)
        #servicio = 'yes' if request.vars.servicio else 'no'

        variables_extra = dict( remote='all', paquetes=paquetes, accion=accion)
                               #, admin=admin)
        #redirect(URL('mostrar'))
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='paquete', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario
                       
    return dict(form=form)

@auth.requires_login()
def remove_packages():
    ids = request.vars["ids"]
    accion = "remove_packages"
    form = SQLFORM.factory(  Field('paquetes', label='Packages', requires=IS_NOT_EMPTY())).process()
    form['_align'] = "center"
    if form.accepted:
        paquetes = request.vars.paquetes
        paquetes = evaluar_expresion.separar_x_comas(paquetes)
        #servicio = 'yes' if request.vars.servicio else 'no'

        variables_extra = dict( remote='all', paquetes=paquetes, accion=accion)
                               #, admin=admin)
        #redirect(URL('mostrar'))
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='paquete', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario
    return locals()

@auth.requires_login()
def add_repositories():
    ids = request.vars["ids"]
    accion = "add_repo"
    form = SQLFORM.factory(  Field('repositorios', label='Repositories', requires=IS_NOT_EMPTY())).process()
    form['_align'] = "center"
    if form.accepted:
        repositorios = request.vars.repositorios
        repositorios = evaluar_expresion.separar_x_comas(repositorios)
        #servicio = 'yes' if request.vars.servicio else 'no'

        variables_extra = dict( remote='all', repositorios=repositorios, accion=accion)
                               #, admin=admin)
        #redirect(URL('mostrar'))
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='paquete', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario           
    return locals()

@auth.requires_login()
def remove_repositories():
    ids = request.vars["ids"]
    accion = "remove_repo"
    form = SQLFORM.factory(  Field('repositorios', label='Repositories', requires=IS_NOT_EMPTY())).process()
    form['_align'] = "center"
    if form.accepted:
        repositorios = request.vars.repositorios
        repositorios = evaluar_expresion.separar_x_comas(repositorios)
        #servicio = 'yes' if request.vars.servicio else 'no'

        variables_extra = dict( remote='all', repositorios=repositorios, accion=accion)
                               #, admin=admin)
        #redirect(URL('mostrar'))
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='paquete', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario                       
    return locals()
