# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from admin.py")

@auth.requires_login()
@auth.requires_membership('Administrador')
def teachers():
    teacher_group = db1(db1.auth_group.role == "Docente").select()
    id_teacher_group =  teacher_group[0]['id'] 
    
    arreglo_ids_docentes = []
    ids_docentes = db1(db1.auth_membership.group_id == id_teacher_group).select(db1.auth_membership.user_id)
    for fila in ids_docentes:
        arreglo_ids_docentes.append(fila["user_id"])
    
    usuarios_docentes = db1(db1.auth_user.id.belongs(arreglo_ids_docentes))#http://web2py.com/books/default/chapter/29/6#belongs

    form = SQLFORM.grid(usuarios_docentes,  deletable=True, csv=True, editable=True, details=True, create=False  )
    #form['_align'] = "center"
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Administrador')
def courses_and_groups():
    indentificador = auth.user_id

    mensaje = H1 (T("Please select a course"))
    restricciones = dict(
        #course_group = db1.course_group.id_teacher== indentificador
                         #, course = db1.course.id == 2
                        )
    grid = SQLFORM.smartgrid(db1.course,linked_tables=['course_group'], constraints = restricciones,
        #searchable=False,
        deletable=True, editable=True, details=True, csv= True, create= False
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
    grid = SQLFORM.smartgrid(db1.course,linked_tables=['machine'],
        #searchable=False,
        deletable=True, editable=True, details=True, csv= True, create= False
        #, links=[lambda row:A(T("Select"),_href=URL("maquinas","lista_maquina_clase",args=[row.id]))]
    )
    return locals()
