#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, HTTPResponse
from config.models import Permiso
from sqlalchemy.sql import select
from config.middleware import enable_cors, headers, check_csrf
from config.database import engine, session_db
from config.constants import constants

permiso_view = Bottle()

@permiso_view.route('/listar/<sistema_id>', method='GET')
@enable_cors
@headers
@check_csrf
def listar(sistema_id):
  rpta = None
  status = 200
  try:
    conn = engine.connect()
    stmt = select([Permiso]).where(Permiso.sistema_id == sistema_id)
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar los permisos del sistema',
        str(e)
      ],
    }
    status = 500
  return HTTPResponse(status = status, body = json.dumps(rpta))

@permiso_view.route('/guardar', method='POST')
@enable_cors
@headers
@check_csrf
def guardar():
  status = 200
  data = json.loads(request.forms.get('data'))
  nuevos = data['nuevos']
  editados = data['editados']
  eliminados = data['eliminados']
  sistema_id = data['extra']['sistema_id']
  array_nuevos = []
  rpta = None
  session = session_db()
  try:
    if len(nuevos) != 0:
      for nuevo in nuevos:
        temp_id = nuevo['id']
        s = Permiso(
          nombre = nuevo['nombre'],
          llave = nuevo['llave'],
          sistema_id = sistema_id,
        )
        session.add(s)
        session.flush()
        temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
        array_nuevos.append(temp)
    if len(editados) != 0:
      for editado in editados:
        session.query(Permiso).filter_by(id = editado['id']).update({
          'nombre': editado['nombre'],
          'llave': editado['llave'],
        })
    if len(eliminados) != 0:
      for id in eliminados:
        session.query(Permiso).filter_by(id = id).delete()
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado los cambios en los permisos del sistema',
        array_nuevos
      ]
    }
  except Exception as e:
    status = 500
    session.rollback()
    rpta = {
      'tipo_mensaje' : 'error',
      'mensaje' : [
        'Se ha producido un error en guardar los permisos del sistema',
        str(e)
      ]
    }
  return HTTPResponse(status = status, body = json.dumps(rpta))
