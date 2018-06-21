#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, HTTPResponse
from config.models import Usuario, VWUsuarioCorreoEstado
from sqlalchemy.sql import select
from config.middleware import enable_cors, headers, check_csrf
from config.database import engine, session_db
from config.constants import constants

usuario_view = Bottle()

@usuario_view.route('/listar', method='GET')
@enable_cors
@headers
@check_csrf
def listar():
  rpta = None
  status = 200
  try:
    conn = engine.connect()
    stmt = select([Usuario.id, Usuario.usuario, Usuario.correo])
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar los usuarios',
        str(e)
      ],
    }
    status = 500
  return HTTPResponse(status = status, body = json.dumps(rpta))

@usuario_view.route('/obtener_usuario_correo/<usuario_id>', method='GET')
@enable_cors
@headers
@check_csrf
def listar(usuario_id):
  rpta = None
  status = 200
  try:
    conn = engine.connect()
    stmt = select([VWUsuarioCorreoEstado]).where(VWUsuarioCorreoEstado.id == usuario_id)
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
    rpta = rpta[0]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en  obtener el usuario y correo',
        str(e)
      ],
    }
    status = 500
  return HTTPResponse(status = status, body = json.dumps(rpta))
