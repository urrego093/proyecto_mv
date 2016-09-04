# -*- coding: utf-8 -*-
# intente algo como
import evaluar_expresion


def index(): return dict(message="hello from system.py")

@auth.requires_login()
def reiniciar():
    ids = request.vars["ids"]
    form = FORM(_method='post').confirm(T('Restart'),{T('Back'):URL('maquinas','mostrar', vars=dict(accion= 'reboot'))})
    form["_align"] = "center"

    if form.accepted:
        redirect(URL('maquinas', 'ejecutar', vars= dict(ids=ids, opcion='restart')))
        #print tarea
    return locals()
