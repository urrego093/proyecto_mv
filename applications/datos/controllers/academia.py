# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
@auth.requires_membership('Administrador')
def register_course():
    form = SQLFORM(db1.course).process()
    if form.accepted:
        session.flash = T("Course Created!")
        redirect(URL('default','index'))
    return locals()

@auth.requires_login()
def create_hostvars_yml(idmachine, systemOpe):
    datos = dict()
    if systemOpe == "Ubuntu":
        datos = dict(ansible_become_pass="reverse", ansible_user="ubuntu")
        #datos = dict(ansible_become_pass="osboxes.org", ansible_user="osboxes")
    elif systemOpe == "CentOS":
        datos = dict(ansible_become_pass="Centosbase123", ansible_user="root")                
        #datos = dict(ansible_become_pass="osboxes.org", ansible_user="root")
    elif systemOpe == "Fedora":
        datos = dict(ansible_become_pass="Centosbase123", ansible_user="root")
        #datos = dict(ansible_become_pass="osboxes.org", ansible_user="root")

        
    #datos = dict (ansible_become_pass="reverse", ansible_user="root")
    
    ruta_basica = os.path.join(request.folder, 'private/Ansible/host_vars/')
    file_path = ruta_basica + idmachine
    escribir_host_yml(file_path,datos)
        
@auth.requires_login()
@auth.requires_membership('Administrador')
def register_machine():
    form = SQLFORM(db1.machine).process()
    if form.accepted:
        
        ip = str(form.vars.ip_machine)
        sistema_operativo = str(form.vars.operative_system)
        maquina_id = form.vars.id
        
        create_hostvars_yml(ip, sistema_operativo)
        session.flash = T(" Machine Created!")

        '''
            Al crear una maquina en el sistema, de manera automática se instala la llave local en la maquina
            para conectar por ssh sin contraseña y se instala el paqeuet vnc
        '''
        variables_extra = dict(IP = ip, OS = sistema_operativo)
        
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=maquina_id, opcion='first_time', variables_extra=variables_extra))) 

        #redirect(URL('default','index'))
    return locals()

@auth.requires_membership('Administrador')
def register_group():
    form = SQLFORM(db1.course_group).process()
    if form.accepted:
        session.flash = T("Group Created!")
        redirect(URL('default','index'))
    return locals()

def del_copy(lista1):
    if lista1==[]:
        return lista1
    else:
        lista2 = []
        for key in lista1:
            if key not in lista2:
                lista2.append(key)
        return lista2

@auth.requires_login()
def r_est():
    semes = request.args(0)
    course = db1.course(request.args(2, cast=int))
    machine = db1.machine(request.args(1, cast=int) or redirect(URL('default','index')))
    num_group = request.args(3) or redirect(URL('default','index'))
    port_m = db1(db1.port_machine.ip_machine==machine.id).select()
    list_port_usados = []
    list_all_port = []

    for row_mac in port_m:
        list_all_port.append(row_mac.id)
        for r_usados in db1((db1.student_x_machine.ip_machine==row_mac.id)).select():
            if r_usados.semester==semes:
                list_port_usados.append(r_usados.ip_machine)

    list_port_usados = del_copy(list_port_usados)
    for i in list_port_usados:
        list_all_port.remove(i)

    db_machine= db1(db1.port_machine.id.belongs(list_all_port))
    campos = [db1.port_machine.id, db1.port_machine.ip_machine, db1.port_machine.number_port, db1.port_machine.hostname]

    gs = SQLFORM.grid(db_machine, fields = campos,
                          csv=False, editable=False, deletable=False, searchable=False,
                          details=False,create=False, user_signature=False,
                          links=[lambda row:A(T("Select"),_href=URL('regis_student', args=(semes, machine.id, course.id, num_group, row.id)))],
                          links_placement = 'left'#,
                          #selectable = lambda ids:redirect(URL('maquinas', 'configurar', vars=dict(ids=ids)))
    )

    return locals()


@auth.requires_login()
def regis_student():
    semes = request.args(0)
    course = db1.course(request.args(2, cast=int))
    machine = db1.machine(request.args(1, cast=int) or redirect(URL('default','index')))
    num_group = request.args(3) or redirect(URL('default','index'))
    id_port_mach = db1.port_machine(request.args(4) or redirect(URL('default','index')))
    db1.student_x_machine.ip_machine.default = id_port_mach.id
    db1.student_x_machine.ip_machine.writable = False
    db1.student_x_machine.ip_machine.reable = False
    db1.student_x_machine.semester.default = semes
    db1.student_x_machine.semester.writable = False
    db1.student_x_machine.semester.reable = False
    db1.student_x_machine.course_group.default = num_group
    db1.student_x_machine.course_group.writable = False
    db1.student_x_machine.course_group.reable = False
    form = SQLFORM(db1.student_x_machine).process()
    if form.accepted:
        response.flash = T("Student Registered")
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return locals()


@auth.requires_login()
@auth.requires_membership('Administrador')
def agree_teacher():
    rows = db1(db1.auth_user.registration_key=='pending').select()
    return locals()

@auth.requires_login()
def show_teacher():
    user = db1.auth_user(request.args(0, cast=int))
    user.update(registration_key='')
    db1.auth_user.first_name.writable = False
    db1.auth_user.first_name.reable = False
    db1.auth_user.last_name.writable = False
    db1.auth_user.last_name.reable = False
    form = SQLFORM(db1.auth_user, user, deletable=False, showid=False)
    form.add_button(T('Back'), URL('academia','agree_teacher') )

    if form.process(next=URL('update_group_teacher', args=user.id)).accepted:
        #response.flash = T ('Teacher accepted')
        pass
    elif form.errors:
        pass
        #response.flash = T ('Teacher No Update')



    return locals()

@auth.requires_login()
def update_group_teacher():
    member = db1.auth_membership(request.args(0, cast=int) or redirect(URL('index')))
    if member:
        ruta_basica = os.path.join(request.folder, 'uploads/')
        ruta_basica = ruta_basica + str(member.user_id)
        try:
            os.makedirs(ruta_basica)
        except OSError:
            pass
        # si no podemos crear la ruta dejamos que pase
        # si la operación resulto con éxito nos cambiamos al directorio
        os.chdir(ruta_basica)
        linea = db1(db1.auth_group.role == "Docente").select(db1.auth_group.id)

        if linea:
            member.update(group_id=linea[0]["id"])
            session.flash = T('Teacher Accepted')
        else:
            session.flash  = T("Couldn't add the teacher to the group")
            
    redirect(URL('academia', 'agree_teacher') )

@auth.requires_login()
def deny_teacher():
    user_id = request.args(0, cast=int)
    user = db1.auth_user(user_id)
    
    #user_id = request.args(0, cast=int)
    #user = db1(db1.auth_user.id == user_id)
    #print user

    db1.auth_user.first_name.writable = False
    db1.auth_user.first_name.reable = False
    db1.auth_user.last_name.writable = False
    db1.auth_user.last_name.reable = False
    
    form = SQLFORM(db1.auth_user, user, deletable=False, showid=False)
    form.add_button(T('Back'), URL('academia','agree_teacher') )

    if form.process().accepted:
        db1(db1.auth_user.id == request.args(0, cast=int)).delete()
        session.flash = T ('User rejected')
        redirect(URL('academia','agree_teacher'))
    elif form.errors:
        session.flash = T ('Error in the form')


    return locals()


@auth.requires_login()
def mostrar_macxuser():
    course = db1.course(request.args(1, cast=int) or redirect(URL('index')))
    machine = db1.machine(request.args(0, cast=int) or redirect(URL('index')))
    #c_group = db1((db1.course_group.cod_course==course.id)& (db1.course_group.id_teacher==auth.user_id)).select()

    groups_text = T("Groups of ")
    query_grupos = ((db1.course_group.cod_course==course.id)& (db1.course_group.id_teacher==auth.user_id)) # eliminar la segunda condicion para q muestre todos los grupos de la materia
    campos_grupo = [db1.course_group.cod_group, db1.course_group.semester]
    groups = SQLFORM.grid(query_grupos, fields = campos_grupo,
                          csv=False, editable=False, deletable=False, searchable=False,
                          details=False,create=False, user_signature=False,
                          links=[lambda row:A(T("Select"),_href=URL('show_ports', args=(row.semester, machine.id, course.id, row.cod_group)))],
                          links_placement = 'left'
    )
    return locals()

@auth.requires_login()
@auth.requires_membership('Docente')
def show_couxuser():
    course = db1.course(request.args(0, cast=int) or redirect(URL('default','index')))
    #c_machine= db1((db1.machine.code_course==course.id)).select()


    query_maquinas = db1.machine.code_course==course.id
    campos_maquina = [db1.machine.ip_machine, db1.machine.operative_system, db1.machine.memory, db1.machine.processor]
    maquinas = SQLFORM.grid(query_maquinas, fields = campos_maquina, csv=False, editable=False, deletable=False,
        searchable=False, # No no moverlo, la busqueda no va a servir debido a q user_signature esta desativado
        details=False, create=False,
        user_signature=False # Si se deja activada como es por defecto resulta en un error extrano, solo en este formulario
        ,links=[lambda row:A(T("Select"),_href=URL('mostrar_macxuser',args=(row.id, course.id)))],
        links_placement = 'left'
    )

    #groups_text = T("Groups of ")
    #query_grupos = db1.course_group.cod_course==course.id and db1.course_group.id_teacher == auth.user_id # eliminar la segunda condicion para q muestre todos los grupos de la materia
    #campos_grupo = [db1.course_group.cod_group, db1.course_group.semester]
    #groups = SQLFORM.grid(query_grupos, fields = campos_grupo ,
     #   csv=False, editable=False, deletable=False, searchable=False, details=False,
      #  create=False, user_signature=False
    #)
    return locals()

@auth.requires_login()
def show_ports():
    semes = request.args(0)
    course = db1.course(request.args(2, cast=int) or redirect(URL('default','index')))
    machine = db1.machine(request.args(1, cast=int) or redirect(URL('default','index')))
    num_group = request.args(3) or redirect(URL('default','index'))
    port_mac = db1(db1.port_machine.ip_machine==machine.id).select()
    response.flash = num_group
    list_port = []

    for port_m in port_mac:
        list_est = db1((db1.student_x_machine.ip_machine==port_m.id) &
                       (db1.student_x_machine.semester==semes) & (db1.student_x_machine.course_group==num_group)).select( db1.student_x_machine.name_student, db1.student_x_machine.code_student, db1.student_x_machine.course_group)
        for l_est in list_est:
            list_port.append((port_m.number_port, port_m.hostname, l_est.code_student, l_est.name_student, l_est.course_group))
    if not list_port:
        response.flash = T ("Currently there are no students")

    return locals()




#def register_student():
#    form = SQLFORM(db1.student_x_machine).process()
#    if form.accepted:
#        session.flash = T("Student Register")
#        #redirect(URL('index'))
#    return locals()
