# -*- coding: utf-8 -*-
# essayez quelque chose comme
def index(): return dict(message="hello from crontab.py")


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

@auth.requires_login()
def custom_task():
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
        Field('name', label=T('Name'), requires=IS_NOT_EMPTY()),
        Field('command', label=T('Command'), requires=IS_NOT_EMPTY()),
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
            variables_extra=dict(
                minute= request.vars.minute, hour= request.vars.hour, day= request.vars.day,
                month=  request.vars.month, weekday= request.vars.weekday, accion= "custom_task",
                nombre= request.vars.name, comando= request.vars.command
            )))
        )

    elif form.errors:
        response.flash = T('Form contains errors')

    return locals()
