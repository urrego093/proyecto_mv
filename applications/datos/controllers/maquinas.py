# -*- coding: utf-8 -*-
# intente algo como
import os
import ast
import evaluar_expresion

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
                        redirect(URL('files','copiar_archivos',vars=dict(ids = ids)))
                    else:
                        response.flash = T("For this task, please select just one machine")

                elif accion == T("re_copy_files"):
                    ids= x.vars.records
                    if type(ids) == str:  
                        redirect(URL('files','copiar_archivos_subidos',vars=dict(ids= ids, archi = request.vars.archi), ))
                    else:
                        response.flash = T("For this task, please select just one machine")

                elif accion == T("limpiar"):
                    redirect(URL('files','clean_machines',vars=dict(ids= x.vars.records)))

    #### Packages and repositories
                elif accion == T("install_package"):
                    redirect(URL('packages_and_repos', 'install_packages', vars=dict(ids= x.vars.records)))

                elif accion == T("remove_packages"):
                    redirect(URL('packages_and_repos', 'remove_packages', vars=dict(ids= x.vars.records)))

                elif accion == T("add_repo"):
                    redirect(URL('packages_and_repos', 'add_repositories', vars=dict(ids= x.vars.records)))

                elif accion == T("remove_repo"):
                    redirect(URL('packages_and_repos', 'remove_repositories', vars=dict(ids= x.vars.records)))

    #### Servicios
                elif accion == T("services"):
                    redirect(URL('services', 'services', vars=dict(ids= x.vars.records)))

                elif accion == T("start_services"):
                    redirect(URL('services', 'start_services', vars=dict(ids= x.vars.records)))

                elif accion == T("stop_services"):
                    redirect(URL('services', 'stop_services', vars=dict(ids= x.vars.records)))

                elif accion == T("restart_services"):
                    redirect(URL('services', 'restart_services', vars=dict(ids= x.vars.records)))

                elif accion == T("reload_services"):
                    redirect(URL('services', 'reload_services', vars=dict(ids= x.vars.records)))

    #### Ports
                elif accion == T('ports'):
                    redirect(URL('ports', 'ports', vars=dict(ids= x.vars.records)))
                
                elif accion == T('open_ports'):
                    redirect(URL('ports', 'open_ports', vars=dict(ids= x.vars.records)))
                    
                elif accion == T('close_ports'):
                    redirect(URL('ports', 'close_ports', vars=dict(ids= x.vars.records)))

    #### Cron tasks
                elif accion == T("update_packges"):
                    redirect(URL('crontab','update_packges', vars=dict(ids= x.vars.records)))
                
                elif accion == T("custom_task"):
                    redirect(URL('crontab','custom_task', vars=dict(ids= x.vars.records)))
                    
                elif accion == T("delete_task"):
                    redirect(URL('crontab','delete_task', vars=dict(ids= x.vars.records)))
    ### VNC
                elif accion == T('enable_vnc_ports'):
                    ids= x.vars.records
                    if type(ids) == str:  
                        redirect(URL('vnc', 'enable_vnc', vars=dict(ids= x.vars.records)))
                    else:
                        response.flash = T("For this task, please select just one machine")

                elif accion == T("first_time"):
                    ids = x.vars.records
                    if type(ids) == str:  
                        redirect(URL('vnc','first_time', vars=dict(ids=ids)))
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
