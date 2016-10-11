# -*- coding: utf-8 -*-
# intente algo como
import evaluar_expresion

@auth.requires_login()
def clean_machines(): 
    ids = request.vars["ids"]
    form = FORM(_method='post').confirm(T('Clean Machines'),{T('Back'):URL('maquinas','mostrar', vars=dict(accion= 'limpiar'))})
    form["_align"] = "center"

    if form.accepted:
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='limpiar')))
        #print tarea
    return dict(form=form)


@auth.requires_login()
def copiar_archivos():
    
    #Recuperamos los ids
    ids = request.vars["ids"]
    #recuperamos el path para subir los archivos
    folder_user = "uploads/" + str(auth.user_id) + "/"
    ruta_basica = os.path.join(request.folder, folder_user)
    
    rows = db1(db1.port_machine.ip_machine==ids).select()
    for row in rows:
        HOSTNAME.append(row.hostname);
    #url = URL('download')
    # https://groups.google.com/forum/#!topic/web2py/X5xmXyTCavY Checkbox Multiple
    form = SQLFORM.factory(  Field("archivo", "upload", label=T("Select file"), uploadfolder=ruta_basica, autodelete=True,requires=IS_NOT_EMPTY()), #widget=SQLFORM.widgets.upload.widget),
        Field("hostname", "list:string",
              default=HOSTNAME,widget=SQLFORM.widgets.checkboxes.widget,
              requires=[IS_IN_SET(HOSTNAME,multiple=True),IS_NOT_EMPTY()]))
    
    form.add_button(T('Back'), URL('maquinas','mostrar', vars=dict(accion= 'copy_files')) )

    #var_extra = dict(origen=request.vars.archivo, somelist=request.vars.hostname)
    var_extra = ""#"origen=" +str("") + "somelist=" + str(request.vars.hostname)

    x = form.process()
    #print "\n\n ********************************** \n\n"
    if x.accepted:
    #if form.accepts(request.vars, session):
        #http://stackoverflow.com/questions/8008213/web2py-upload-with-original-filename todo un día intentado hacer lo que este chico me soluciono :D
        coded_name = form.vars.archivo
        orig_name = request.vars.archivo.filename
        os.rename(ruta_basica + coded_name, ruta_basica + orig_name) 
        ## ^ ^ comentar si se desea encriptar archivos, se debe tener algun registro en la base de datos para que no salga feo
        redirect(URL('maquinas','ejecutar', vars= dict(ids=ids, opcion='copyFile', variables_extra=dict(origen=ruta_basica + orig_name,
                                                                                  somelist=request.vars.hostname))))
    return locals()



@auth.requires_login()
def copiar_archivos_subidos():
    #Recuperamos los ids
    ids = request.vars["ids"]
    #recuperamos el path para subir los archivos
    folder_user = "uploads/" + str(auth.user_id) + "/"
    ruta_basica = os.path.join(request.folder, folder_user)
    orig_name =  request.vars.archi
    rows = db1(db1.port_machine.ip_machine==ids).select()
    for row in rows:
        HOSTNAME.append(row.hostname);
    #url = URL('download')
    # https://groups.google.com/forum/#!topic/web2py/X5xmXyTCavY Checkbox Multiple
    form = SQLFORM.factory(  Field("archivo", "string", default = orig_name, writable= False), #widget=SQLFORM.widgets.upload.widget),
        Field("hostname", "list:string",
              default=HOSTNAME,widget=SQLFORM.widgets.checkboxes.widget,
              requires=[IS_IN_SET(HOSTNAME,multiple=True),IS_NOT_EMPTY()]))
    form.add_button(T('Back'), URL('maquinas','mostrar', vars=dict(accion='re_copy_files', archi= orig_name)))

    if form.accepts(request.vars, session):
        redirect(URL('maquinas','ejecutar', vars= dict(ids=ids, opcion='copyFile', variables_extra=dict(origen=ruta_basica + orig_name,
                                                                                             somelist=request.vars.hostname))))
    return locals()

@auth.requires_login()
def list_files():
    folder_user = "uploads/" + str(auth.user_id) + "/"
    ruta_basica = os.path.join(request.folder, folder_user)
    lstDir = os.walk(ruta_basica)
    #Lista vacia para incluir los ficheros
    lstFiles = []
    #Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            lstFiles.append(nombreFichero+extension)

    #res = response.stream(open(pathfilename,'rb'), chunk_size=10**6)

    return locals()






@auth.requires_login()
## Reference http://www.web2py.com/AlterEgo/default/show/36
def my_big_file_downloader():
    import os
    filename=request.args[0]
    folder_user = str(auth.user_id)
    pathfilename= os.path.join(request.folder,'uploads/'+folder_user, filename)
    return response.stream(open(pathfilename,'rb'), chunk_size=10**6)

    # the old way
# reference http://www.web2py.com/AlterEgo/default/show/36
@auth.requires_login()
def my_small_file_downloader():
    import os
    import gluon.contenttype
    filename=request.args[0]
    folder_user = str(auth.user_id)
    response.headers['Content-Type']=gluon.contenttype.contenttype(filename)
    pathfilename=os.path.join(request.folder,'uploads/'+folder_user, filename)
    return open('pathfilename', 'rb').read()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
