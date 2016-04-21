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

def guardar_resumen(nombre, texto):
    nombre_txt = nombre + ".txt"
    archivo = open(nombre_txt, "w+")
    registros = texto.split('\n')
    for registro in registros:
        if registro != '':
            archivo.write(registro + '\n')

def escribir_variables_yml(ruta_nombre, variables):
    ruta_nombre += '.yml'
    diccionario = ast.literal_eval(variables)

    with open(ruta_nombre, 'w') as fp:
        yaml.dump(diccionario, fp, default_flow_style=False)
    return ruta_nombre
        
def escribir_variables_json(ruta_nombre, variables):
    ruta_nombre += '.json'
    diccionario = ast.literal_eval(variables)

    with open(ruta_nombre, 'w') as fp:
        json.dump(diccionario, fp)
    return ruta_nombre
        
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

def playbook(*args, **vars):
    #recuperando datos pasados en un diccionario
    print "entro al playbook"
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
    print extra_vars
    comando = "ansible-playbook " + playbook + " -i " + hosts + extra_vars
    
    #comando_listo = shlex.split(comando)
    #print comando_listo
    
    
    process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = process.pid
    #print "proceso es: ", pid
    
    output = process.communicate()
    salida = output[0]
    #str_salida = salida.split("PLAY RECAP *********************************************************************") #Camilo 
    str_salida = salida.split("PLAY RECAP ********************************************************************") #Carlos
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
