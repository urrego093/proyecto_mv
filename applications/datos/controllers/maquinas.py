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
    is_admin = False
    
    macxuser = []
    db_machine = []
    
    for c_group in db1(db1.course_group.id_teacher==auth.user_id).select(db1.course_group.cod_course, distinct=True):
        for row in db1(db1.machine.code_course==c_group.cod_course.id).select(db1.machine.ip_machine, db1.machine.id, distinct=True):
            macxuser.append(row.id) #/id_machine/id_course
            
    adminis = db1((db1.auth_membership.user_id == auth.user_id)).select()

    for row in adminis:
        if row.group_id.role =="Administrador":
            is_admin = True
            db_machine = db1.machine
        elif row.group_id.role=="Docente":
            db_machine = db1(db1.machine.id.belongs(macxuser))#http://web2py.com/books/default/chapter/29/6#belongs
            
    todas_maquinas = db1(db1.machine).select()

    if len(todas_maquinas) > 0:
        campos_maquina = [db1.machine.ip_machine, db1.machine.operative_system, db1.machine.memory, db1.machine.processor, db1.machine.description_machine]
        grid = SQLFORM.grid(db_machine, fields = campos_maquina ,csv=False, editable=False, deletable=False, create=False, details=False,
            searchable=False, # Quitar comentario si se quiere ocultar la barra de busqueda
                               #se tiene q revisar el por que al ver un registro la linea x = grid[1][0].process() genera error si 
            selectable = lambda ids :
                            redirect(     URL(  'maquinas', 'configurar', vars=dict(ids=ids)    )  )
        )
        #grid[1][0].insert(1, test)
        grid[1]['_align'] = "center" # jejeje

        #GRACIAS!!!!   https://groups.google.com/forum/#!topic/web2py/3kSpuDgo1Lw
        #Si no hay maquinas se muere, ya q grid[1][0] queda siendo un div y no es posible llamar process(), corregir~! 
        #print "   ------------------ ///// --------------- " ,grid[1][0]

        x = grid[1][0].process()

        x["_method"] ='post'
        if x.accepted:
            if x.vars.records:
                accion = request.vars.accion
    #### General
                if accion == T("reboot"):
                    redirect (URL('system', 'reiniciar', vars=dict(ids= x.vars.records)))
                
                elif accion == T("first_time"):
                    ids = x.vars.records
                    if type(ids) == str:  
                        redirect(URL('system','first_time', vars=dict(ids=ids)))
                    else:
                        response.flash = T("For this task, please select just one machine")
                    
                    

    #### Users and passwords                
                elif accion == T("create_users"):
                    redirect(URL('usuarios', 'crear' ,vars=dict(ids= x.vars.records)))

                elif accion == T("delete_users"):
                    redirect(URL('usuarios','eliminar_usuario',vars=dict(ids= x.vars.records)))

                elif accion == T('change_users_pass'):
                    redirect(URL('usuarios','cambiar_pass',vars=dict(ids= x.vars.records)))

    #### Files                
                elif accion == T("copy_files"):
                    ids= x.vars.records
                    if type(ids) == str:  
                        redirect(URL('copiar_archivos',vars=dict(ids = ids)))
                    else:
                        response.flash = T("For this task, please select just one machine")

                elif accion == T("re_copy_files"):
                    ids= x.vars.records
                    if type(ids) == str:  
                        redirect(URL('copiar_archivos_subidos',vars=dict(ids= ids, archi = request.vars.archi), ))
                    else:
                        response.flash = T("For this task, please select just one machine")

                elif accion == T("limpiar"):
                    redirect(URL('files','clean_machines',vars=dict(ids= x.vars.records)))

    #### Packages and repositories
                elif accion == T("install_package"):
                    redirect(URL('system', 'install_packages', vars=dict(ids= x.vars.records)))

                elif accion == T("remove_packages"):
                    redirect(URL('system', 'remove_packages', vars=dict(ids= x.vars.records)))

                elif accion == T("add_repo"):
                    redirect(URL('system', 'add_repositories', vars=dict(ids= x.vars.records)))

                elif accion == T("remove_repo"):
                    redirect(URL('system', 'remove_repositories', vars=dict(ids= x.vars.records)))

    #### Servicios
                elif accion == T("services"):
                    redirect(URL('system', 'services', vars=dict(ids= x.vars.records)))

                elif accion == T("start_services"):
                    redirect(URL('system', 'start_services', vars=dict(ids= x.vars.records)))

                elif accion == T("stop_services"):
                    redirect(URL('system', 'stop_services', vars=dict(ids= x.vars.records)))

                elif accion == T("restart_services"):
                    redirect(URL('system', 'restart_services', vars=dict(ids= x.vars.records)))

                elif accion == T("reload_services"):
                    redirect(URL('system', 'reload_services', vars=dict(ids= x.vars.records)))

    #### Ports
                elif accion == T('ports'):
                    redirect(URL('system', 'ports', vars=dict(ids= x.vars.records)))

    #### Cron tasks
                elif accion == T("update_packges"):
                    redirect(URL('system','update_packges', vars=dict(ids= x.vars.records)))
                
                elif accion == T("custom_task"):
                    redirect(URL('system','custom_task', vars=dict(ids= x.vars.records)))
                    
                elif accion == T("delete_task"):
                    redirect(URL('system','delete_task', vars=dict(ids= x.vars.records)))
    ### VNC
                elif accion == T('enable_vnc_ports'):
                    ids= x.vars.records
                    if type(ids) == str:  
                        redirect(URL('system', 'enable_vnc', vars=dict(ids= x.vars.records)))
                    else:
                        response.flash = T("For this task, please select just one machine")

                else:
                    pass
            else:
                response.flash = T('Please select at least one machine')
            #redirect ( URL(  'maquinas', 'configurar', vars=dict(accion=x.vars.accion, id= x.vars.records) ))
    #elif x.errors:
        #response.flash = T('Please select at leats one id')
    else:
        grid = None
    return locals()

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
    
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='vnc_config', variables_extra = variables)))
    return locals()
    
@auth.requires_login()
def install_vnc():
    
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=maquina_id, opcion='vnc_install')))
    return locals()

@auth.requires_login()
def copiar_archivos():
    #Recuperamos los ids
    ids = request.vars["ids"]
    #recuperamos el path para subir los archivos
    folder_user = "uploads/" + str(auth.user_id) + "/"
    ruta_basica = os.path.join(request.folder, folder_user)
    rows = db1(db1.port_machine.ip_machine==ids).select()
    for row in rows:
        HOSTNAME.append(row.hostname);
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



@auth.requires_login()
def copiar_archivos_subidos():
    #Recuperamos los ids
    ids = request.vars["ids"]
    #recuperamos el path para subir los archivos
    folder_user = "uploads/" + str(auth.user_id) + "/"
    ruta_basica = os.path.join(request.folder, folder_user)
    orig_name =  request.vars.archi
    rows = db1(db1.port_machine.ip_machine==ids).select()
    for row in rows:
        HOSTNAME.append(row.hostname);
    #url = URL('download')
    # https://groups.google.com/forum/#!topic/web2py/X5xmXyTCavY Checkbox Multiple
    form = SQLFORM.factory(  Field("archivo", "string", default = orig_name, writable= False), #widget=SQLFORM.widgets.upload.widget),
        Field("hostname", "list:string",
              default=HOSTNAME,widget=SQLFORM.widgets.checkboxes.widget,
              requires=[IS_IN_SET(HOSTNAME,multiple=True),IS_NOT_EMPTY()]))
    form.add_button(T('Back'), URL('mostrar#'))

    if form.accepts(request.vars, session):
        redirect(URL('ejecutar', vars= dict(ids=ids, opcion='copyFile', variables_extra=dict(origen=ruta_basica + orig_name,
                                                                                             somelist=request.vars.hostname))))
    return locals()

@auth.requires_login()
@auth.requires_membership('Administrador')
def lista_maquina_grupo():
    indentificador = auth.user_id

    mensaje = H1 (T("Please select a course"))
    restricciones = dict(
        #course_group = db1.course_group.id_teacher== indentificador
                         #, course = db1.course.id == 2
                        )
    grid = SQLFORM.smartgrid(db1.course,linked_tables=['course_group'], constraints = restricciones,
        #searchable=False,
        deletable=False, editable=True, details=True, csv= False, create= False
        #, links=[lambda row:A(T("Select"),_href=URL("maquinas","lista_maquina_clase",args=[row.id]))]
    )
    return locals()

@auth.requires_login()
@auth.requires_membership('Administrador')
def lista_maquina_materia():
    indentificador = auth.user_id

    mensaje = H1 (T("Please select a course"))
    restricciones = dict(
        #course_group = db1.course_group.id_teacher== indentificador
                         #, course = db1.course.id == 2
                        )
    grid = SQLFORM.smartgrid(db1.course,linked_tables=['machine'], constraints = restricciones,
        #searchable=False,
        deletable=True, editable=True, details=True, csv= False, create= False
        #, links=[lambda row:A(T("Select"),_href=URL("maquinas","lista_maquina_clase",args=[row.id]))]
    )
    return locals()

@auth.requires_login()
def ejecutar():
    #un diccionario con los nombres de los playbooks segun la opcion elegida
    playbooks= dict(restart='reiniciar.yml', user='usuarios2/linux_users.yml', copyFile='copiarArchivo.yml', paquete="paquete/paquete.yml", 
                    services="services/services.yml", ports="ports/ports.yml", limpiar = "limpiar.yml", first_time = "configurar/site.yml",
                    vnc_config = "vnc_config/site.yml", crontab="crontab/cron.yml")
     
    #los ids de las maquinas selccionadas y la opcion elegida
    ids = request.vars["ids"]
    ids = [ids] if type(ids)==str else ids
    opcion = request.vars['opcion']
    
    #para_evitar_errores ccon los playbook de servicios y puertos, que hacian un parseo para
    # mostrar la salida de un comando incluso cuando este no era para revisar el estado actual
    is_debug = True if request.vars["is_debug"] else False
    
    variables_extra = request.vars['variables_extra']
    #print str(ids)+ "opcion " + str(playbooks[opcion]) + str(variables_extra) 
    
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
        debug = ruta_basica + "debug/" + nombre,
        variables=variables_extra,
        is_debug= is_debug
    )
    
    #se pide al worker o proceso en segundo plano que ejcuta el playbook en maximo 10 minutos
    tarea = scheduler.queue_task(
        "playbook", pargs=ids, pvars=variables, stop_time = None, timeout = 600 ,repeats = 1
    )
    print "id ", str(tarea.id) #id de la tarea 
    #se inserta un registro de la tarea en la base de datos con la referencia al campo en la tabla scheduler_task,
    #dicha tabla maneja los estados de una tarea, registra los errores, guarda los argumentos(parametros en un arreglo)
    # y las variables(parametros en un diccionario)
    db1.job.insert(name = nombre, user_id = indentificador, task_id = tarea.id, action = opcion)
   
    #db1.commit()
    redirect(URL('tasks', 'resumen/'+nombre))
