# -*- coding: utf-8 -*-
# intente algo como

def index():
    encabezado = T("These are your previous task")
    
    query_job = db1.job.user_id == auth.user_id
    
    campos_tarea = [db1.job.name, db1.job.action, db1.job.date] 
    
    grid = SQLFORM.grid(query_job, fields = campos_tarea, csv=False, editable=False, deletable=False, 
        searchable=False, # No no moverlo, la busqueda no va a servir debido a q user_signature esta desativado
        details=False, create=False, user_signature=False, # Si se deja activada como es por defecto resulta en un error extrano, solo en este formulario
        orderby=db1.job.date,
        links=[
            dict(  header=T('Finished'), body= lambda row:(buscar_tarea_resumen(row.name)) ),
            dict(  header=T('Summary'),  body= lambda row:A(T("Open"),_href=URL('tasks', 'resumen',args=(row.name))) )
        ]
    )
    return locals()

 

def resumen():
    job_name = request.args(0)
    trabajo = db1(db1.job.name == job_name).select()
    
    boton_volver = INPUT(_value = T('Back'),_type= "button", _class="btn btn-default", _onclick= "window.history.back();")
    boton_descargar = INPUT(_value = T('Download Resume'),_type= "button", _class="btn btn-primary",
                            #_href="/datos/private/Ansible/resultados/" + job_name + ".txt"
                           )
     
    texto_summary = T("Global Summary")
    #print "----------------- /////////////// ------------", trabajo[0]
    query_task = db1.scheduler_task.id == trabajo[0]["task_id"]
   
    campos_task = [db1.scheduler_task.status, db1.scheduler_task.start_time, db1.scheduler_task.next_run_time]
    grid = SQLFORM.grid(query_task, fields = campos_task, csv=False, editable=False, deletable=False, 
        searchable=False, # No no moverlo, la busqueda no va a servir debido a q user_signature esta desativado
        details=False, create=False, user_signature=False # Si se deja activada como es por defecto resulta en un error extrano, solo en este formulario
        #,links=[dict(  header='Hosts', body=lambda row:str([1,2])  )  ] # mejorar para mostra las ips ?
    )
    
    texto_summary_per_host = T("Summary per host")
    
    existe_resumen = buscar_tarea_resumen(job_name)
    resultados = []
    if existe_resumen == T('Yes'):
        resultados = abrir_resumen(job_name)
    else:
        resultados = T("Job not finished yet")
    #print lineas
    return locals()
