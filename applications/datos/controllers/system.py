# -*- coding: utf-8 -*-
# intente algo como
import evaluar_expresion


def index(): return dict(message="hello from system.py")

@auth.requires_login()
def reiniciar():
    ids = request.vars["ids"]
    form = FORM(_method='post').confirm(T('Restart'),{T('Back'):URL('maquinas','mostrar', vars=dict(accion= 'reboot'))})
    form["_align"] = "center"

    if form.accepted:
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='restart')))
        #print tarea
    return locals()

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

@auth.requires_login()
def ports():
    ids = request.vars["ids"]
    variables_extra = dict( remote='all', action='check')
    
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='ports', variables_extra = variables_extra, is_debug=True)))
    return dict()

@auth.requires_login()
def enable_vnc():
    id_maquina = request.vars["ids"]
    puertos = db1(db1.port_machine.ip_machine == id_maquina).select(db1.port_machine.number_port, db1.port_machine.hostname)
    print " ---- -- - - -LOS PUERTOS DE LA MAQUINA SON  - - - - -- - - - - - - -- -"
    #print puertos
    datos = []
    for linea in puertos:
        puerto = -1
        usuario = "default_user"
        for llave in linea:
            if llave == "number_port":
                puerto = int(linea[llave]) - 5900
            elif llave == "hostname":
                usuario = linea[llave]
        datos.append(dict(name = usuario, vnc_num = puerto, vnc_port = puerto+5900)) 
    variables = dict(vnc_users = datos)
    
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=id_maquina, opcion='vnc_config', variables_extra = variables)))
    return locals()
    
@auth.requires_login()
def first_time():
    ids = request.vars["ids"]
    
    campo = db1(db1.machine.id == ids).select()

    ip = campo[0]["ip_machine"]
    os = campo[0]["operative_system"]
    
    variables_extra = dict(IP = ip, OS = os)
        
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='first_time', variables_extra=variables_extra))) 

        
    #redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='vnc_install')))
    return locals()

@auth.requires_login()
def update_packges():
    minutos = ["*"]
    minutos += range(0,60)
    
    horas = ["*"]
    horas += range(0,24)
    
    dias = ["*"]
    dias += range(0,32)
    
    nombre_dias = ["*"]
    nombre_dias += ['sun','mon','tue','wed','thu','fri','sat']
    
    nombre_mes = ["*"]
    nombre_mes += ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    
    #Recuperamos los ids
    ids = request.vars["ids"]
    
    #Se crea el formulario
    form = SQLFORM.factory(
        Field('minute', label=T('Minute'), requires=IS_IN_SET(minutos, zero='Select one', error_message=T('Too small or too big!'))),
        Field('hour', label=T('Hour'), requires=IS_IN_SET(horas, zero='Select one',error_message=T('Too small or too big!'))),
        Field('day', label=T('Day of Month'),requires=IS_IN_SET(dias, zero='Select one',error_message=T('Too small or too big!'))),
        Field('month', requires=IS_IN_SET(nombre_mes,zero='Select one' ,error_message=T('¡Error!'))),
        Field('weekday', label=T('Weekday'), requires=IS_IN_SET(nombre_dias, zero='Select one', error_message=T('error')))
    )
    form.add_button(T('Back'), URL('maquinas','mostrar#'))
    
    if form.process().accepted:
        response.flash = T('Form accepted')
        redirect(URL('maquinas','ejecutar', vars= dict(ids=ids, opcion='crontab', 
            variables_extra=dict(minute=request.vars.minute, hour = request.vars.hour, day = request.vars.day,
                month = request.vars.month, weekday = request.vars.weekday, accion = "update_packges"
            )))
        )

    elif form.errors:
        response.flash = T('Form contains errors')

    return locals()


@auth.requires_login()
def delete_task():   
    #Recuperamos los ids
    ids = request.vars["ids"]
    
    #Creamos el formulario
    form = SQLFORM.factory(
        Field('name', label=T('Name'), requires=IS_NOT_EMPTY()),
    ) 
    form.add_button(T('Back'), URL('maquinas','mostrar#'))
    
    if form.process().accepted:
        nombre = request.vars.name
        nombre = evaluar_expresion.separar_x_comas(nombre)
        
        response.flash = T('Form accepted')
        redirect(URL('maquinas','ejecutar', 
            vars= dict(ids=ids, opcion='crontab', variables_extra = dict( accion = "delete_task",nombre = nombre) ))
        )

    elif form.errors:
        response.flash = T('Form contains errors')

    return locals()
