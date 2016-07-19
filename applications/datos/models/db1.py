# -*- coding: utf-8 -*-
#Define DAL object, with max 10 connection

from gluon.contrib.appconfig import AppConfig

db1 = DAL(STR_DAL, pool_size=10, migrate=mig)
#db1 = DAL(STR_DAL, pool_size=10)

## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


#Auth
from gluon.tools import Auth, Service, PluginManager

auth = Auth(db1)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = True
auth.settings.reset_password_requires_verification = True


#Define tables of model 

db1.define_table('course',
                Field('code_course','integer', length=3, label = T('Course Code'),requires=IS_NOT_EMPTY()),
                Field('name_course','string', length=60, label = T('Course Name'), requires=IS_NOT_EMPTY()),
                Field('description_course','text',label = T('Course Description')),
                auth.signature)
db1.course.code_course.requires=IS_NOT_IN_DB(db1, db1.course.code_course)

db1.define_table('machine',
                Field('ip_machine', label=T('IPv4 Machine'), requires=IS_IPV4(minip='10.20.251.1', maxip='10.20.251.255')),
                Field('code_course','reference course', label=T('Code Course'), requires=IS_IN_DB(db1,db1.course.id, '%(name_course)s', zero=T('Choose One'))),
                Field('operative_system','string', label=T('Operative System'), requires=IS_IN_SET(OPERA_SYSTEM, zero=T('Select One'), error_message='You no choose one')),
                Field('memory','string',label=T('Memory RAM'), requires=IS_IN_SET(RAM_MEMORY, zero=T('Select One'), error_message='You no choose one')),
                Field('processor','string',label=T('Processor'), requires=IS_IN_SET(PROCESSOR, zero=T('Select One'), error_message='You no choose one')),
                Field('description_machine','text',label=T('Description'),requires=IS_NOT_EMPTY()),
                auth.signature)

db1.machine.ip_machine.requires=IS_NOT_IN_DB(db1, db1.machine.ip_machine)


db1.define_table('port_machine',
                Field('ip_machine','reference machine', label = T('IPv4 Machine'), requires=IS_IN_DB(db1,db1.machine.id, '%(ip_machine)s', zero = T('Select One'))),
                Field('number_port','string', label = T('Port'), requires=IS_IN_SET(P_HOST, zero = T('Select One'), error_message='You no choose one')),
                Field('hostname','string',label = T('Hostname'), requires=IS_IN_SET(HOSTNAME, zero = T('Select One'), error_message='You no choose one')),
                 auth.signature)

db1.port_machine.number_port.requires=IS_NOT_IN_DB(db1(db1.port_machine.ip_machine==request.vars.ip_machine),
    'port_machine.number_port')


db1.define_table('course_group',
               Field('cod_group', 'integer', label = T('Code Group'), requires=IS_NOT_EMPTY()),
               Field('id_teacher','reference auth_user', label = T('Teacher'), requires=IS_IN_DB(db1,db1.auth_user.id, '%(first_name)s', zero = T('Select One'))),
               Field('cod_course','reference course', label = T('Course'), requires=IS_IN_DB(db1,db1.course.id, '%(name_course)s', zero = T('Select One'))),
               Field('semester', 'string', label = T('Semester'), requires=IS_IN_SET(SEMESTER, zero = T('Select One'), error_message='You no choose one')),
                 auth.signature)

courses = db1(db1.course_group.cod_course==request.vars.cod_course)

db1.course_group.cod_group.requires=[IS_NOT_IN_DB(courses(db1.course_group.semester==request.vars.semester), 'course_group.cod_group')]



db1.define_table('student_x_machine',
               Field('ip_machine', 'reference port_machine', label = T('Id Machine:Port'), requires=IS_IN_DB(db1,db1.port_machine.id, '%(id)s', zero = T('Select One'))),
               Field('code_student','string', requires=IS_NOT_EMPTY()),
               Field('name_student','string', requires=IS_NOT_EMPTY()),
               Field('semester', 'string', label = T('Semester'), requires=IS_IN_SET(SEMESTER, zero = T('Select One'), error_message='You no choose one')),
               Field('course_group', 'string', label = T('Group'), requires=IS_IN_SET(GROUP, zero = T('Select One'), error_message='You no choose one')),
               auth.signature,migrate=False
)

db1.student_x_machine.ip_machine.requires=IS_NOT_IN_DB(db1(db1.student_x_machine.semester==request.vars.semester),
    'student_x_machine.ip_machine')

db1.define_table('job',
    Field('name', 'string', label=T('Job Name'), requires=IS_NOT_EMPTY()),
    Field('action', 'string', label=T('Action') ),
    Field('date', 'datetime', default=request.now),
    Field('user_id', 'reference auth_user', label=T('Teacher'), 
          requires=IS_IN_DB(db1, db1.auth_user.id)   ),
    Field('task_id' ,label=T('Task ID')), migrate=mig
                 #,
   # Field('state', label=T('State'), type='boolean', default=False) # lo maneja la tabla scheduler_task
)

db1.job.name.requires=IS_NOT_IN_DB(db1(db1.job.name==request.vars.name), 'job.name')
