# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('VM-UD'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href=URL('default', 'index'),
                  _id="pmv_logo")

response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Carlos  <suarezsilvestre1@gmail.com> Camilo <urrego@outlook.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])]

response.menu = [
    (T('User manual'), False, URL('tutorial', 'index'), []),
     (T('About'), False, URL('about', 'index'), [])

]



#List of course for userid  (Ex: User_id 1, machines 192.168.1.114,192.168.1.115)
couxuser = []
for row in db1(db1.course_group.id_teacher==auth.user_id).select(db1.course_group.cod_course, distinct=True):
    couxuser.append((T(str(row.cod_course.name_course)), False, URL('academia', 'show_couxuser', args=(row.cod_course.id)))) #id_course


macxuser = []
for c_group in db1(db1.course_group.id_teacher==auth.user_id).select(db1.course_group.cod_course, distinct=True):
    for row in db1(db1.machine.code_course==c_group.cod_course.id).select(db1.machine.ip_machine, db1.machine.id, distinct=True):
        macxuser.append((row.ip_machine, False,URL('academia', 'mostrar_macxuser',args=(row.id, c_group.cod_course)))) #/id_machine/id_course

adminis = db1((db1.auth_membership.user_id == auth.user_id)).select()
for row in adminis:
    if row.group_id.role =="Administrador": #row.group_id == 1
        response.menu += [
            (T('Approval'), False, '#', [
                (T('Teacher'), False, URL('academia', 'agree_teacher'))
            ])
        ]
        
        response.menu += [     
            (T('To register'), False, '#', [
                    (T('Course'), False, URL('academia', 'register_course')),
                    (T('Machine'), False, URL('academia', 'register_machine')),
                    (T('Group'), False, URL('academia', 'register_group'))
            ])
        ]
        
        response.menu += [
            (T('Consult'), False, '#', [
                 (T('My Files'), False, URL('files', 'list_files')),
                 (T('My jobs'), False, URL('tasks', 'index')),
                 #(T('Running Services'), False, URL('maquinas','mostrar', vars=dict(accion= 'services'))),
                 #(T('Open ports'), False, URL('maquinas','mostrar', vars=dict(accion= 'ports'))),
            ])
        ]
        
        response.menu += [
            (T('Commands'), False, '#', [
                (T('Users'), False,  URL('commands','users')),
                (T('System'), False, URL('commands', 'system')),
                (T('Files'), False, URL('commands', 'files'))
            ])
        ]
        
        response.menu += [
            (T('DB'), False, "#", [
                (T('Courses and Groups'), False, URL('admin', 'courses_and_groups')),
                (T('Machines by course'), False, URL('admin', 'lista_maquina_materia')), 
                (T('Teachers'), False, URL('admin', 'teachers')),
            ])
        ]
        


        
        
    if row.group_id.role=="Docente":
        response.menu += [
            (T('Courses'), False,'#',couxuser),
            (T('Machines'), False,'#',macxuser),
            #(T('Commands'), False, URL('maquinas','mostrar')),
           ]
        
        response.menu += [
            (T('Commands'), False, '#', [
                (T('Users'), False,  URL('commands','users')),
                (T('System'), False, URL('commands', 'system')),
                (T('Files'), False, URL('commands', 'files')),
            ]),
            (T('Consult'), False, '#', [
                            (T('My Files'), False, URL('files', 'list_files')),
                            (T('My jobs'), False, URL('tasks', 'index')),
                            #(T('Running Services'), False, URL('maquinas','mostrar', vars=dict(accion= 'services'))),
                            #(T('Open ports'), False, URL('maquinas','mostrar', vars=dict(accion= 'ports')))
                    ]
             )
            #(T('Students'), False, '#', [
            #                (T('Register'), False, URL('default', 'register_student')),
            #                (T('List'), False, URL('tasks', 'index'))])
        ]
        
    else:
        response.menu += []


DEVELOPMENT_MENU = False

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
          (T('This App'), False, '#', [
              (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
              LI(_class="divider"),
              (T('Controller'), False,
               URL(
               'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
              (T('View'), False,
               URL(
               'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
              (T('DB Model'), False,
               URL(
               'admin', 'default', 'edit/%s/models/db.py' % app)),
              (T('Menu Model'), False,
               URL(
               'admin', 'default', 'edit/%s/models/menu.py' % app)),
              (T('Config.ini'), False,
               URL(
               'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
              (T('Layout'), False,
               URL(
               'admin', 'default', 'edit/%s/views/layout.html' % app)),
              (T('Stylesheet'), False,
               URL(
               'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
              (T('Database'), False, URL(app, 'appadmin', 'index')),
              (T('Errors'), False, URL(
               'admin', 'default', 'errors/' + app)),
              (T('About'), False, URL(
               'admin', 'default', 'about/' + app)),
              ]),
          ('web2py.com', False, '#', [
             (T('Download'), False,
              'http://www.web2py.com/examples/default/download'),
             (T('Support'), False,
              'http://www.web2py.com/examples/default/support'),
             (T('Demo'), False, 'http://web2py.com/demo_admin'),
             (T('Quick Examples'), False,
              'http://web2py.com/examples/default/examples'),
             (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
             (T('Videos'), False,
              'http://www.web2py.com/examples/default/videos/'),
             (T('Free Applications'),
              False, 'http://web2py.com/appliances'),
             (T('Plugins'), False, 'http://web2py.com/plugins'),
             (T('Recipes'), False, 'http://web2pyslices.com/'),
             ]),
          (T('Documentation'), False, '#', [
             (T('Online book'), False, 'http://www.web2py.com/book'),
             LI(_class="divider"),
             (T('Preface'), False,
              'http://www.web2py.com/book/default/chapter/00'),
             (T('Introduction'), False,
              'http://www.web2py.com/book/default/chapter/01'),
             (T('Python'), False,
              'http://www.web2py.com/book/default/chapter/02'),
             (T('Overview'), False,
              'http://www.web2py.com/book/default/chapter/03'),
             (T('The Core'), False,
              'http://www.web2py.com/book/default/chapter/04'),
             (T('The Views'), False,
              'http://www.web2py.com/book/default/chapter/05'),
             (T('Database'), False,
              'http://www.web2py.com/book/default/chapter/06'),
             (T('Forms and Validators'), False,
              'http://www.web2py.com/book/default/chapter/07'),
             (T('Email and SMS'), False,
              'http://www.web2py.com/book/default/chapter/08'),
             (T('Access Control'), False,
              'http://www.web2py.com/book/default/chapter/09'),
             (T('Services'), False,
              'http://www.web2py.com/book/default/chapter/10'),
             (T('Ajax Recipes'), False,
              'http://www.web2py.com/book/default/chapter/11'),
             (T('Components and Plugins'), False,
              'http://www.web2py.com/book/default/chapter/12'),
             (T('Deployment Recipes'), False,
              'http://www.web2py.com/book/default/chapter/13'),
             (T('Other Recipes'), False,
              'http://www.web2py.com/book/default/chapter/14'),
             (T('Helping web2py'), False,
              'http://www.web2py.com/book/default/chapter/15'),
             (T("Buy web2py's book"), False,
              'http://stores.lulu.com/web2py'),
             ]),
          (T('Community'), False, None, [
             (T('Groups'), False,
              'http://www.web2py.com/examples/default/usergroups'),
              (T('Twitter'), False, 'http://twitter.com/web2py'),
              (T('Live Chat'), False,
               'http://webchat.freenode.net/?channels=web2py'),
              ]),
        ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
