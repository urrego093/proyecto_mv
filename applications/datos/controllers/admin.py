# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from admin.py")

@auth.requires_login()
@auth.requires_membership('Administrador')
def teachers():
    teacher_group = db1(db1.auth_group.role == "Docente").select(db1.auth_group.id)
    id_teacher_group = teacher_group[0]['id']
    
    query= db1.auth_membership.group_id == id_teacher_group
    campos = [db1.auth_membership.user_id]
    form = SQLFORM.grid(query, campos,  deletable=False, csv=False, editable=False, details=False, create=False,
       links=[
            dict(  header=T('Details'),  body= lambda row: 
                 A(
                    SPAN(_class="icon magnifier icon-zoom-in glyphicon glyphicon-zoom-in") + SPAN(T("View"),_class="buttontext button"), 
                    _class="button btn btn-default", _title=T("View"), _href=URL('admin', 'teacher_details', args=[row.user_id]) 
                )
            )
        ]
    )
    return dict(form=form)

@auth.requires_login()
@auth.requires_membership('Administrador')
def teacher_details():
    teacher_id = request.args[0]
    query= db1.auth_user.id == teacher_id
    #campos = []
    form = SQLFORM.grid(query, deletable=False, csv=False, editable=False, details=False, user_signature=False, searchable=False, create=False)
    return dict(form=form)
