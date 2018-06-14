#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, HTTPResponse
from config.models import Sistema
from sqlalchemy.sql import select
from config.middleware import enable_cors, headers
from config.database import engine, session_db
from config.constants import constants

sistema_view = Bottle()

@sistema_view.route('/listar', method='GET')
@enable_cors
@headers
def listar():
  rpta = None
  status = 200
  try:
    conn = engine.connect()
    stmt = select([Sistema])
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en listar los sistemas',
        str(e)
      ],
    }
    status = 500
  return HTTPResponse(status = status, body = json.dumps(rpta))
