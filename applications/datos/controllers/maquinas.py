# -*- coding: utf-8 -*-
# intente algo como
import os
import ast

'''
def index():
    cabezas = ["ip_machine", "code_course", "operative_system", "memory", "processor"]
    filas =  db1((db1.machine.ip_machine)).select(
        db1.machine.ip_machine, db1.machine.code_course, db1.machine.operative_system,db1.machine.memory,db1.machine.processor
    )
    acciones = [T("Restart"),T("Add user")]
    return locals()
'''
@auth.requires_login()
def mostrar():
    # Crear un campo pasando un arreglo para los campos http://web2py.com/books/default/chapter/29/05/the-views#HTML-helpers
    # como agregar campos a un formulario https://web2py.wordpress.com/2010/05/01/more-customization-on-forms/
    opciones = [T("Restart"), T("Create User"), T("Delete User"), T("Copy Files")]
    #test2 = SQLFORM.factory(
    #    Field('accion',requires=IS_IN_SET(opciones))
    #)
    test = SELECT(*opciones, **dict(_name="accion", _id="accion") )

    grid = SQLFORM.grid(db1.machine,         csv=False, editable=False, deletable=False,
        #query = asdasdasdasdasads
        selectable = lambda ids :
                        redirect(     URL(  'maquinas', 'configurar', vars=dict(ids=ids)    )  )
    )
    grid[1][0].insert(1, test)
    #grid[1][0].insert(1, test2)
    grid[1]['_align'] = "center" # jejeje

    #GRACIAS!!!!   https://groups.google.com/forum/#!topic/web2py/3kSpuDgo1Lw
    x = grid[1][0].process()
    x["_method"] ='post'
    if x.accepted:
        if x.vars.records:
            if x.vars.accion == T("Restart"):
                redirect (URL('reiniciar', vars=dict(ids= x.vars.records)))
            elif x.vars.accion == T("Create User"):
                redirect(URL('usuarios',vars=dict(ids= x.vars.records)))
            elif x.vars.accion == T("Delete User"):
                redirect(URL('eliminar_usuario',vars=dict(ids= x.vars.records)))
            elif x.vars.accion == T("Copy Files"):
                redirect(URL('copiar_archivos',vars=dict(ids= x.vars.records)))
            else:
                pass
        else:
            response.flash = T('Please select at least one machine')
            #redirect ( URL(  'maquinas', 'configurar', vars=dict(accion=x.vars.accion, id= x.vars.records) ))
    #elif x.errors:
        #response.flash = T('Please select at leats one id')
    return locals()

@auth.requires_login()
def usuarios():
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
        password = request.vars.password
        admin = 'yes' if request.vars.admin else 'no'

        variables_extra = dict( remote='all', username=name, password=password, admin=admin, action='create_user')
        redirect(URL('ejecutar', vars= dict(ids=ids, opcion='create_user', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario

    return dict(form=form)

@auth.requires_login()
def eliminar_usuario():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('user_name', label=T('User name'), requires=IS_NOT_EMPTY())
    ).process()

    if form.accepted:
        name = request.vars.user_name
        variables_extra = dict( remote='all', username=name, action='delete_user')
        redirect(URL('ejecutar', vars= dict(ids=ids, opcion="delete_user", variables_extra = variables_extra)))
    return dict(form= form)

@auth.requires_login()
def reiniciar():
    ids = request.vars["ids"]
    form = FORM(_method='post').confirm(T('Restart'),{T('Back'):URL('mostrar#')})
    form["_align"] = "center"
    
    pregunta = T('Do you really whish to restart the selected machines?')
    
    if form.accepted:
        print "se reiniciara la maquina"
        redirect(URL('ejecutar', vars= dict(ids=ids, opcion='restart')))
        #print tarea
    return locals()

@auth.requires_login()
def copiar_archivos():
    #Recuperamos los ids
    ids = request.vars["ids"]
    #recuperamos el path para subir los archivos 
    ruta_basica = os.path.join(request.folder, 'uploads/')
    HOSTNAME=['Carlos','centos']
    #url = URL('download')
    # https://groups.google.com/forum/#!topic/web2py/X5xmXyTCavY Checkbox Multiple
    form = SQLFORM.factory(  Field("archivo", "upload", uploadfolder=ruta_basica, autodelete=True), #widget=SQLFORM.widgets.upload.widget),
        Field("hostname", "list:string",
              default=HOSTNAME,widget=SQLFORM.widgets.checkboxes.widget,
              requires=[IS_IN_SET(HOSTNAME,multiple=True),IS_NOT_EMPTY()]))
    form.add_button(T('Back'), URL('mostrar#'))

    #var_extra = dict(origen=request.vars.archivo, somelist=request.vars.hostname)
    var_extra = ""#"origen=" +str("") + "somelist=" + str(request.vars.hostname)

    #print "\n\n ********************************** \n\n"
    if form.accepts(request.vars, session):
        #http://stackoverflow.com/questions/8008213/web2py-upload-with-original-filename todo un día intentado hacer lo que este chico me soluciono :D
        coded_name = form.vars.archivo
        orig_name = request.vars.archivo.filename
        os.rename(ruta_basica + coded_name, ruta_basica + orig_name)
        redirect(URL('ejecutar', vars= dict(ids=ids, opcion='copyFile', variables_extra=dict(origen=ruta_basica + orig_name,
                                                                                             somelist=request.vars.hostname))))
    return locals()

def ejecutar():
    #un diccionario con los nombres de los playbooks segun la opcion elegida
    playbooks= dict(restart='reiniciar.yml', create_user='usuarios/linux_users.yml', delete_user='usuarios/linux_users.yml', copyFile='copiarArchivo.yml')
     
    #los ids de las maquinas selccionadas y la opcion elegida
    ids = request.vars["ids"]
    opcion = request.vars['opcion']
    variables_extra = request.vars['variables_extra']
    print str(ids)+ "opcion " + str(playbooks[opcion]) + str(variables_extra) 
    
    #se crea el nombre de los archivos de la tarea con primerNombre_segundoNombre
    indentificador = auth.user_id
    #nombres = db1(db1.auth_user.id == indentificador).select(db1.auth_user.first_name,      db1.auth_user.last_name)

    ruta_basica = os.path.join(request.folder, 'private/Ansible/')

    trabajos_usuario = db1(db1.job.user_id == auth.user_id).select()
    total_trabajos = len(trabajos_usuario)


    nombre = str(indentificador) + '_' + str(total_trabajos)

    #se construye un diccionario para ejecutar el playbook
    variables = dict(
        nombre= ruta_basica + "resultados/" + nombre,
        playbook=ruta_basica + "Playbooks/" +  playbooks[opcion],
        hosts= ruta_basica + '' + nombre,
        ruta_extra=ruta_basica + "variables/" + nombre,
        variables=variables_extra
    )
    
    

    #se pide al worker o proceso en segundo plano que ejcuta el playbook en maximo 10 minutos
    tarea = scheduler.queue_task(
        "playbook", pargs=ids, pvars=variables, stop_time = None, timeout = 120 ,repeats = 1
    )
    print "id " + str(tarea.id) #id de la tarea 
    #se inserta un registro de la tarea en la base de datos con la referencia al campo en la tabla scheduler_task,
    #dicha tabla maneja los estados de una tarea, registra los errores, guarda los argumentos(parametros en un arreglo)
    # y las variables(parametros en un diccionario)
    db1.job.insert(name = nombre, user_id = indentificador, task_id = tarea.id)

    #db1.commit()
    redirect(URL('maquinas', 'mostrar'))
