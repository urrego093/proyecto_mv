# -*- coding: utf-8 -*-

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
   Abre un archivo yaml que guarda las variables usadas para ejecutar un playbook, 
   luego retorna un diccionario con dichas variables
'''
def cargar_variables(nombre):
    ruta = os.path.join(request.folder, 'private/Ansible/variables/') + nombre + ".yml"
    variables = dict()
    with open(ruta, 'r') as f:
        variables = yaml.load(f)
    return variables

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
    '''
    if type(ids) == str:
        for fila in filas:
            if fila['id'] == int(ids):
                ips.append( fila['ip_machine'] )
    '''
    for identificador in ids:
        for fila in filas:
            if fila['id'] == int(identificador):
                ips.append( fila['ip_machine'] )
    
    
    #se crea un archivo con las direcciones ip de las maquinas seleccionadas (el archivo inventario)
    archivo = open(ruta_nombre, 'w')
    #print "IPS SON: ", ips
    for ip in ips:
        archivo.write(ip + "\n")
