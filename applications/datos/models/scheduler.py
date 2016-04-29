# -*- coding: utf-8 -*-
from gluon.scheduler import Scheduler

#para ejecutar los comandos remotos
import subprocess

# para partir los comandos, no sirvio muy bien
#import shlex 

#para construir la ruta a los archivos
import os

# para sacar los resultados en una sola linea 
import yaml
import json

# interpreta un string como codigo python, usado para obtener el diccionario de variables que se convierte a string automaticamente
import ast

# Para analizar expresiones
import re

'''
    Comprueba si existe un resultado para un trabajo(job),
    de no ser asi significa q la tarea no se ha ejecutado
    
    Retorna 'Yes' si existe un archivo con los resultados
            'No'  En caso contrario
'''
def buscar_tarea_resumen(nombre):
    ruta = os.path.join(request.folder, 'private/Ansible/resultados/') + nombre + ".txt"
    print ruta
    existe = T("Yes") if os.path.exists(ruta) else T("No")
    return existe

'''
    Retorna un arreglo de arrelgos, 
    cada linea corresponde a la direccion ip de un equipo y un diccionario con los resultados
    de la ejecucion de un trabajo (job)
'''
def abrir_resumen(nombre):
    ruta = os.path.join(request.folder, 'private/Ansible/resultados/') + nombre + ".txt"
    lineas = []
    with open(ruta) as archivo:
        lineas = archivo.readlines()
    lineas_separadas = []
    for linea in lineas:
        if linea != '' and linea != '*\n':
            datos = re.split(':|',linea)
            #print datos
            datos[1] = separar_resultados(datos[1])
            print datos
            lineas_separadas.append(datos)
        
    return lineas_separadas

'''
    Retorna un diccionario con una llave por cada posible dato que da ansible, 
    ok = tareas ejecutadas con exito
    
    changed = cambios en el host destino tras ejecutar las tareas
    
    unreachable = Los hosts a los q ansible no se pudo conectar, 
        bien sea q estan apagados o hay un error al conectarse por ssh
        
    failed: el numero de tareas que fallaron
'''
def separar_resultados(resultado):
    ok = re.split("ok=|", resultado )#["", "12 changed=123132 ..."]
    ok = re.split(" |", ok[1]) #[12, " changed=....]
    ok = ok[0] #12
    
    changed = re.split("changed=|", resultado) #["", "12 unreachable=123132 ..."]
    changed = re.split(" |", changed[1]) #[12, " unreachable=....]
    changed = changed[0] #12
    
    unreachable = re.split("unreachable=|", resultado) #["", "12 failed=123132 ..."]
    unreachable = re.split(" |", unreachable[1]) #[12, " failed=....]
    unreachable = unreachable[0] #12
    
    failed = re.split("failed=|", resultado) #["", "12  \n"]
    failed = re.split(" |", failed[1]) #[12, " changed=....]
    failed = failed[0] #12
    
    return dict(ok=ok, changed=changed,unreachable=unreachable, failed=failed)

'''
    Guarda el resumen de la ejecucion de un trabajo(job) en un archivo dentro de /private/Ansible/resultados/XXXX
    la ruta completa esta incluida en la variable nombre
'''
def guardar_resumen(nombre, texto):
    nombre_txt = nombre + ".txt"
    archivo = open(nombre_txt, "w+")
    registros = texto.split('\n')
    for registro in registros:
        print registro
        if registro != '':
            posible_error = re.split("to retry, |", registro) # Si existe algun error y ansible sugiere re intentar la tarea, esto no se le debe mostrar al usuario
            ignorar = True if len(posible_error)>1 else False
            if  not ignorar:
                archivo.write(registro + '\n')

'''
    Crea un archivo yml con las variables de la ejecucion de un playbook dentro /private/Ansible/variables/XXXXXX
    la ruta esta incluida en la variable ruta_nombre
'''
def escribir_variables_yml(ruta_nombre, variables):
    ruta_nombre += '.yml'
    diccionario = ast.literal_eval(variables)

    with open(ruta_nombre, 'w') as fp:
        yaml.dump(diccionario, fp, default_flow_style=False)
    return ruta_nombre
       
'''
    Crea un archivo json con las variables de la ejecucion de un playbook dentro /private/Ansible/variables/XXXXXX
    la ruta esta incluida en la variable ruta_nombre
'''
def escribir_variables_json(ruta_nombre, variables):
    ruta_nombre += '.json'
    diccionario = ast.literal_eval(variables)

    with open(ruta_nombre, 'w') as fp:
        json.dump(diccionario, fp)
    return ruta_nombre
        
'''
    Crea un archivo con una lista de hosts sobre los cuales se va a ejecutar una tarea
'''
def crear_inventario(ruta_nombre, ids):
    #recuperando las ips segun las ids recibidas
    filas =  db1(db1.machine).select(
        db1.machine.id, db1.machine.ip_machine
    )
    ips = []
    for identificador in ids:
        for fila in filas:
            if fila['id'] == int(identificador):
                ips.append( fila['ip_machine'] )
    
    #se crea un archivo con las direcciones ip de las maquinas seleccionadas (el archivo inventario)
    archivo = open(ruta_nombre, 'w')
    #print "IPS SON: ", ips
    for ip in ips:
        archivo.write(ip + "\n")

'''
    Ejecuta una tarea, los parametros son:
        args: Una lista de las ids de las maquinas sobre las que se va a ejecutar un trabajo,
              se utilizaran para obtener las direcciones IP de la BD
        vars: Un diccionario que incluye:
              - Nombre del archivo de resumen de tarea a ser creado
              - Ruta al archivo yml que contienen las tareas a ejecutar
              - Ruta al archivo en el q se guardaran las direcciones de destino
              - Las variables de ejecucion, son diferentes para cada trabajo
'''
def playbook(*args, **vars):
    #recuperando datos pasados en un diccionario
    #print "entro al playbook"
    nombre = vars['nombre']
    playbook = vars['playbook']
    hosts = vars['hosts']
    pid = -1 # no lo usamos para nada 
    salida = None
    variables = vars['variables']
    
    ids = args
    crear_inventario(hosts, ids)
    
    #creando una parte del comando que incluye como variables extra el archivo indicado
    extra_vars = ""
    if variables:
        ruta_variables =  vars['ruta_extra']
        ruta_variables = escribir_variables_yml(ruta_variables, variables)
        extra_vars = " --extra-vars @" + ruta_variables
    #print extra_vars
    comando = "ansible-playbook " + playbook + " -i " + hosts + extra_vars
    print comando
    
    #comando_listo = shlex.split(comando)
    #print comando_listo
    
    
    process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = process.pid
    #print "proceso es: ", pid
    
    output = process.communicate()
    salida = output[0]
    #str_salida = salida.split("PLAY RECAP *********************************************************************") #Camilo 
    str_salida = salida.split("PLAY RECAP *********************************************************************") #Carlos
    print output
    
   
    guardar_resumen(nombre, str_salida[1])
    
    return 1
    
scheduler = Scheduler(db1,
    dict( playbook=playbook
#                        demo2=demo2,
#                        demo3=demo3,
#                        demo4=demo4,
#                        foo=demo5
                        )
                      , migrate=mig)

db1.job.task_id._reference = 'db1.scheduler_task'
