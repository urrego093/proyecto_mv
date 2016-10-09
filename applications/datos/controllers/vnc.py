# -*- coding: utf-8 -*-
# essayez quelque chose comme
import evaluar_expresion

def index(): return dict(message="hello from vnc.py")



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
    
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=id_maquina, opcion='vnc_config', variables_extra = variables)))
    return locals()
    
@auth.requires_login()
def first_time():
    ids = request.vars["ids"]
    
    campo = db1(db1.machine.id == ids).select()

    ip = campo[0]["ip_machine"]
    os = campo[0]["operative_system"]
    
    variables_extra = dict(IP = ip, OS = os)
        
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='first_time', variables_extra=variables_extra))) 

        
    #redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='vnc_install')))
    return locals()
