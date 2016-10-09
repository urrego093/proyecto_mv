# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def index():
    query_job = db1.job.user_id == auth.user_id
    grid = []
    
    campos_tarea = [db1.job.name, db1.job.action, db1.job.date] 
    
    grid = SQLFORM.grid(query_job, fields = campos_tarea, csv=False, editable=False, deletable=False, 
        searchable=False, # No no moverlo, la busqueda no va a servir debido a q user_signature esta desativado
        details=False, create=False, user_signature=False, # Si se deja activada como es por defecto resulta en un error extrano, solo en este formulario
        orderby=~db1.job.date,
        links=[
            dict(  header=T('Finished'), body= lambda row:(buscar_tarea_resumen(row.name)) ),
            dict(  header=T('Summary'),  body= lambda row:A(T("Open"),_href=URL('tasks', 'resumen',args=(row.name))) )
        ]
    )
    return locals()

 
@auth.requires_login()
def resumen():
    #Mensajes de la pagina
    job_name = request.args(0)
    
    fila_accion = db1(db1.job.name == job_name).select(db1.job.action)
    accion = fila_accion[0]['action']
    
    job_user_id = int(re.split("_", job_name)[0])
    user_id = int(auth.user_id)
    
    existe_resumen = T('No')
    
    #Tablas Nulas
    grid = T("You're not authorized to see this Job!")
    resultados = []
    variables = dict()
    debug = dict()
    cabezas = []
    datos = {}
    
    enlace_resumen = "http://127.0.0.1:8000/datos/appadmin/update/db1/scheduler_run/"
    
    if job_user_id == user_id:
        trabajo = db1(db1.job.name == job_name).select()

        #print "----------------- /////////////// ------------", trabajo[0]
        query_task = db1.scheduler_task.id == trabajo[0]["task_id"]
        
        '''
        borrar despues
        '''
        campos_ejecucion = db1(db1.scheduler_run.task_id == trabajo[0]["task_id"]).select()
        if campos_ejecucion:
            enlace_resumen += str(campos_ejecucion[0]["id"])

        campos_task = [db1.scheduler_task.status, db1.scheduler_task.start_time, db1.scheduler_task.next_run_time]
        grid = SQLFORM.grid(query_task, fields = campos_task, csv=False, editable=False, deletable=False, 
            searchable=False, # No no moverlo, la busqueda no va a servir debido a q user_signature esta desativado
            details=False, create=False, user_signature=False # Si se deja activada como es por defecto resulta en un error extrano, solo en este formulario
            #,links=[dict(  header='Hosts', body=lambda row:str([1,2])  )  ] # mejorar para mostra las ips ?
        )

        existe_resumen = buscar_tarea_resumen(job_name)
        
        if existe_resumen == T('Yes'):
            resultados = abrir_resumen(job_name)
            #variables = dict(ips=range(0,10), datos= "ajajajajjajaa", otros_datos="Otros datos")
            variables = cargar_variables(job_name)
            print " ------------- LAS VARIABLES SON  ---------"
            print variables
            #diccionario = dict(ips = T("IP Directions"), datos=T("Data"), otros_datos=T("Other data"))
        else:
            resultados = T("Job not finished yet")
            
        
        existe_debug = buscar_tarea_debug(job_name)

        
        if existe_debug == T('Yes'):
            if accion == "services":
                debug = leer_debug_servicios(job_name)
                
                cabezas = debug["cabezas"]
                datos = debug["datos"]
            elif accion == "ports":
                debug = leer_debug_puertos(job_name)
                
                cabezas = debug["cabezas"]
                datos = debug["datos"]
            else:
                pass
        else:
            pass
    #print lineas
    return locals()
