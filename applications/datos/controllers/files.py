# -*- coding: utf-8 -*-
# intente algo como

@auth.requires_login()
def clean_machines(): 
    ids = request.vars["ids"]
    redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='limpiar')))
    return dict(message="hello from files.py")
