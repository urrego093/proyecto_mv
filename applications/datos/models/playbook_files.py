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
    Comprueba si existe un archivo con informacion que debe mostrarse al usuario para un trabajo(job),
    de no ser asi significa q la tarea no se ha ejecutado o que ésta no deberia mostrar información al usuario
    más allá del resumen general
    
    Retorna 'Yes' si existe un archivo con los resultados
            'No'  En caso contrario
'''
def buscar_tarea_debug(nombre):
    ruta = os.path.join(request.folder, 'private/Ansible/debug/') + nombre + ".txt"
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
    if os.path.exists(ruta):
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
        #print registro
        if registro != '':
            posible_error = re.split("to retry, |", registro) # Si existe algun error y ansible sugiere re intentar la tarea, esto no se le debe mostrar al usuario
            ignorar = True if len(posible_error)>1 else False
            if  not ignorar:
                archivo.write(registro + '\n')


'''
    Guarda la salida en pantalla dentro de la seccion "DEBUG" de la ejecucion de un trabajo(job) en un archivo dentro de /private/Ansible/debug/XXXX
    la ruta completa esta incluida en la variable nombre
'''
def guardar_debug(nombre, texto):
    nombre_txt = nombre + ".txt"
    archivo = open(nombre_txt, "w+")
    registros = texto.split('\n')
    for registro in registros:
        #print registro
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
    print ruta_nombre
    print " ----------- VARIABLES SON ----------"
    print variables
    diccionario = ast.literal_eval(variables)
    print "diccionario", diccionario
    
    with open(ruta_nombre, 'w') as fp:
        yaml.dump(diccionario, fp, default_flow_style=False)
    return ruta_nombre

'''
    Crea un archivo yml con las variables de los host de las maquinas dentro /private/Ansible/host_vars/XXXXXXX
    la ruta esta incluida en la variable ruta_nombre
'''
def escribir_host_yml(ruta_nombre, variables):
    ruta_nombre += '.yml'
    diccionario = variables
    
    with open(ruta_nombre, 'w') as fp:
        yaml.dump(diccionario, fp, default_flow_style=False)
    


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
        
def leer_debug_servicios(nombre):
    cabezas = [] ########### Guarda los encabezados
    datos = {} ############# Guarda una serie de datos ip : servicios activos
    ruta = os.path.join(request.folder, 'private/Ansible/debug/') + nombre + ".txt"
    if os.path.isfile(ruta) :
        archivo = open(ruta, "r")

        lineas = archivo.readlines()
        archivo.close()

        texto = "".join(lineas)

        coincidencias = re.findall('ok: (.*?)}', texto, re.DOTALL)
        #print "------------------ PARTIDO ------------------"
        for coincidencia in coincidencias:

            # separa la coincidencia en un arreglo con la ip y los servicios
            linea_partida = coincidencia.split("=>") 
            #saca la ip de los corchetes`
            ip = re.search('\[(.*?)\]', linea_partida[0] ).group(1) 

            # saca la lista de servicios activos en una maquina
            servicios = linea_partida[1].split('"msg": ') 

            #remueve unas lineas al final que son la interpretacion de la tabla
            sin_leyenda = re.split('"LOAD   = Reflects whether the unit',servicios[1])
            sin_leyenda[0] += '""]'
            #print sin_leyenda[0]    

            ##evalua el texto como una expresion de python con un arreglo de lineas
            #lista = ast.literal_eval(servicios[1])
            lista = ast.literal_eval(sin_leyenda[0])
            #print lista

            ## Saca los encabezados, primero elimina los espacios multiples
            ## remplazandolos por sencillos y luego hace un split por espacio sencillo
            espacio_sencillo = re.sub(' +',' ',lista[0])
            encabezados = re.split(" ",espacio_sencillo)
            #if (cabezas == [])
            cabezas = encabezados
            #print encabezados, "\n"

            lista.pop(0)

            #elimina lineas nulas
            lista2 = []
            for x in lista:
                if x != "":
                    lista2.append(x)
            #print lista2

            lista_espacios_sencillos = [re.sub(' +',' ',x) for x in lista2]
            #print lista_espacios_sencillos

            lista_de_listas = []
            for linea in lista_espacios_sencillos:
                arreglo = []

                partida_exited = re.split("exited", linea)
                partida_running = re.split("running", linea)

                if len(partida_exited) > 1:
                    inicio_datos =  re.split(" ", partida_exited[0] )
                    for dato in inicio_datos:
                        if dato != '':
                            arreglo.append(dato)
                    arreglo.append("exited")
                    arreglo.append( partida_exited[1] )

                if len(partida_running) > 1:
                    inicio_datos =  re.split( " +", partida_running[0] )
                    for dato in inicio_datos:
                        if dato != '':
                            arreglo.append(dato)
                    arreglo.append("running")
                    arreglo.append( partida_running[1] )
                    lista_de_listas.append(arreglo)

            #print arreglo

            datos.update({ip:lista_de_listas})
            #print "----------------- Datos ---------------"
            #print "Encabezados son:" , cabezas
            #print "Datos son:"
            #print datos
        
    return dict(cabezas=cabezas, datos=datos)










def leer_debug_puertos(nombre):
    cabezas = [] ########### Guarda los encabezados
    datos = {} ############# Guarda una serie de datos ip : puertos activos
    ruta = os.path.join(request.folder, 'private/Ansible/debug/') + nombre + ".txt"
    if os.path.isfile(ruta) :
        archivo = open(ruta, "r")

        lineas = archivo.readlines()
        archivo.close()

        texto = "".join(lineas)

        coincidencias = re.findall('ok: (.*?)}', texto, re.DOTALL)
        #print "------------------ PARTIDO ------------------"
        for coincidencia in coincidencias:

            # separa la coincidencia en un arreglo con la ip y los puertos
            linea_partida = coincidencia.split("=>") 
            #saca la ip de los corchetes
            ip = re.search('\[(.*?)\]', linea_partida[0] ).group(1) 

            # saca la lista de puertos activos en una maquina
            puertos = linea_partida[1].split('"msg": ') 

            #remueve unas lineas al final que son la interpretacion de la tabla
            sin_lineas_al_final = re.split('Active UNIX domain',puertos[1])
            if len(sin_lineas_al_final) ==1:
                sin_lineas_al_final = re.split('Sockets du domaine UNIX',puertos[1])
            sin_lineas_al_final[0] += '"]'
            #print sin_lineas_al_final[0]    

            ##evalua el texto como una expresion de python con un arreglo de lineas
            lista = ast.literal_eval(sin_lineas_al_final[0])
            #print lista

            #elimina la primera linea que es informacion que resulta irrelevante
            lista = lista[1:]
            
            ## Saca los encabezados, primero elimina los espacios sencillos en un solo encabezado
            ## remplazandolos por un guien, luego remplaza espacios multiples por sencillos 
            ## para terminar, hace un split por espacio sencillo
            
            if cabezas == []:
                espacio_address = re.sub(" Address", "-Address", lista[0])
                espacio_name = re.sub(" name", "-name", espacio_address)
                espacio_sencillo = re.sub(' +',' ', espacio_name )

                encabezados = re.split(" ",espacio_sencillo)
                
                cabezas2 = encabezados
                for x in cabezas2:
                    if x != "":
                        cabezas.append(x)
                #print encabezados, "\n"

            lista.pop(0) #elimina la linea de encabezados

            #elimina lineas nulas
            lista2 = []
            for x in lista:
                if x != "":
                    lista2.append(x)
            #print lista2

            lista_espacios_sencillos = [re.sub(' +',' ',x) for x in lista2]
            #print lista_espacios_sencillos

            lista_de_listas = []
            for linea in lista_espacios_sencillos:
                arreglo = []
                arreglo = re.split(" +", linea)
                arreglo.pop()
                if len(arreglo) == 6:
                    arreglo.append("-")

                print len(arreglo), ":", arreglo, "\n"
                lista_de_listas.append(arreglo)

            #print lista_de_listas
            datos.update({ip:lista_de_listas})
            #print "----------------- Datos ---------------"
            #print "Encabezados son:" , cabezas
            #print "Datos son:"
            #print datos
            
    return dict(cabezas=cabezas, datos=datos)
