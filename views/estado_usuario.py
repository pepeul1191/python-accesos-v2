#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, HTTPResponse
from config.models import EstadoUsuario
from sqlalchemy.sql import select
from config.database import engine
from config.middleware import enable_cors, headers, check_csrf

estado_usuario_view = Bottle()

@estado_usuario_view.route('/listar', method='GET')
@enable_cors
@headers
@check_csrf
def listar():
  rpta = None
  status = 200
  try:
    conn = engine.connect()
    stmt = select([EstadoUsuario])
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar los estados de usuario',
        str(e)
      ],
    }
    status = 500
  return HTTPResponse(status = status, body = json.dumps(rpta))
