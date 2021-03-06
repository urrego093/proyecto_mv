# -*- coding: utf-8 -*-
# intente algo como
#def index(): return dict(message="hello from usuarios.py")
import evaluar_expresion

@auth.requires_login()
def crear():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('user_name', label='User name', requires=IS_NOT_EMPTY()),
        Field('password', 'password', label='Password', requires=[IS_LENGTH(minsize=6)
                                                                 # , IS_STRONG(min=6,special=0, upper=1)
                                                                 ]
             ),
        Field('confirm_password', 'password', label='Confirm password', requires=[
                IS_STRONG(min=6, special=0, upper=1), 
                IS_EQUAL_TO(request.vars.password, error_message='passwords do not match')]),
        Field('admin', 'boolean', label='Admin')
    ).process()

    if form.accepted:
        name = request.vars.user_name
        name = evaluar_expresion.evaluar_expresion(name)
        registrar_host(ids, name)
        password = request.vars.password
        admin = 'yes' if request.vars.admin else 'no'

        variables_extra = dict( remote='all', username=name, password=password, admin=admin, action="create_user")
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='user', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario

    return dict(form=form)

@auth.requires_login()
def eliminar_usuario():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('user_name', label=T('User name'), requires=IS_NOT_EMPTY())
    ).process()

    if form.accepted:
        name = request.vars.user_name
        name = evaluar_expresion.evaluar_expresion(name)
        print 'NAME ES :' , name
        delete_host(ids,name)
        variables_extra = dict( remote='all', username=name, action='delete_user')
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion="user", variables_extra = variables_extra)))
    return dict(form= form)


@auth.requires_login()
def cambiar_pass():
    ids = request.vars["ids"]
    form = SQLFORM.factory(
        Field('user_name', label='User name', requires=IS_NOT_EMPTY()),
        Field('password', 'password', label='New password', requires=[IS_LENGTH(minsize=6)
                                                                  #, IS_STRONG(min=6,special=0, upper=1)
                                                                 ]),
        Field('confirm_password', 'password', label='Confirm new password', requires=[
                #IS_STRONG(min=6, special=0, upper=1), 
                IS_EQUAL_TO(request.vars.password, error_message='passwords do not match')])
    ).process()

    if form.accepted:
        name = request.vars.user_name
        name = evaluar_expresion.evaluar_expresion(name)

        password = request.vars.password

        variables_extra = dict( remote='all', username=name, password=password, action="change_pass")
        #redirect(URL('mostrar'))
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='user', variables_extra = variables_extra))) ## asi se pasan las variables ingresadas por el usuario
    return locals()

@auth.requires_login()
#@auth.requires_membership('Administrador')
def registrar_host(ids,hosts):
    ids = [ids] if type(ids)==str else ids
    list_to_last = []
    list_last = []
    for i in ids:
        last_port = db1(db1.port_machine.ip_machine==i).select().sort(lambda registro: registro.number_port).last()
        if last_port:
            list_to_last += range(5901,int(last_port.number_port)+1)
            list_busy_ports = []
            for row in db1(db1.port_machine.ip_machine==i).select(db1.port_machine.number_port):
                list_busy_ports.append(int(row.number_port))
            list2 = del_list(list_to_last,list_busy_ports)
            print "LISTA  RESTA ====================" , list2
            if len(list2) >= len(hosts):
                for n in range(len(hosts)):
                    nexts = list2[n]
                    db1.port_machine.insert(ip_machine=i, number_port=nexts, hostname=hosts[n])
                    db1.commit()
            elif len(list2) < len(hosts):
                dif = len(hosts) - len(list2)
                list_last += list2
                list_last += range(int(last_port.number_port)+1,int(last_port.number_port)+dif+1)
                for n in range(len(hosts)):
                    nexts = list_last[n]
                    db1.port_machine.insert(ip_machine=i, number_port=nexts, hostname=hosts[n])
                    db1.commit()
 
            print "LISTA ====================" , list_last
        else:
            nexts = 5900
            for n in hosts:
                nexts += 1
                db1.port_machine.insert(ip_machine=i, number_port=nexts, hostname=n)
                db1.commit()

@auth.requires_login()
#@auth.requires_membership('Administrador')
def delete_host(ids,hosts):
    ids = [ids] if type(ids)==str else ids
    l_ports = []
    for i in ids:
        ports = db1(db1.port_machine.ip_machine==i).select()
        for n in hosts:
            if db1(db1.port_machine.hostname==n).select() is None:
                 session.flash = T("This user(s) not found")
            else:
                db1(db1.port_machine.hostname==n).delete()

def del_list(lista1, lista2):
    #print "LISTA 1111111111111 ====================" , lista1
    #print "LISTA 2222222222222 ====================" , lista2
    for i in range(len(lista2)):
        print lista1.remove(lista2[i])
    return lista1
