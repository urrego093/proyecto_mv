# -*- coding: utf-8 -*-
from gluon.scheduler import Scheduler

#para ejecutar los comandos remotos
import subprocess

# para partir los comandos, no sirvio muy bien
#import shlex 

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
    debug = vars['debug']
    playbook = vars['playbook']
    hosts = vars['hosts']
    pid = -1 # no lo usamos para nada 
    salida = None
    variables = vars['variables']
    is_debug = vars["is_debug"]
    
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
    print "- - - - - -- COMANDO ES ------ "
    print comando
    
    #comando_listo = shlex.split(comando)
    #print comando_listo
    
    process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = process.pid
    #print "proceso es: ", pid
    
    output = process.communicate()
    
    salida = output[0]
    print "- - - - - - - -  SALIDA ES - - - - - - - "
    print salida
    
    errores = output[1]
    print "-----------------LOS ERRORES SON ------------"
    print errores
    
    #str_salida = salida.split("PLAY RECAP *********************************************************************") #Camilo 
    str_salida = salida.split("PLAY RECAP *********************************************************************") #Carlos
    guardar_resumen(nombre, str_salida[1])
    #print " ----------------------------------------  la salida es ------------------------------"
    #print str_salida
    #print output
    if is_debug:
        debug_feo = salida.split("TASK [check : debug] ***********************************************************")
        #print "--------------- DEBUG FEOOOOO -------------"
        #print debug_feo
        if len(debug_feo) > 1:
            debug_bonito = debug_feo[1].split("PLAY RECAP")
            #print "------------------ DEBBUG BONITO ------------------"
            #print debug_bonito
            guardar_resumen(debug, debug_bonito[0])

    return 1
    
scheduler = Scheduler(db1,
    dict( playbook=playbook ) , migrate=mig
)

db1.job.task_id._reference = 'db1.scheduler_task'
