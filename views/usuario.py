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

@usuario_view.route('/nombre_repetido', method='POST')
@enable_cors
@headers
@check_csrf
def nombre_repetido():
  rpta = None
  status = 200
  try:
    data = json.loads(request.forms.get('data'))
    usuario_id = data['id']
    nombre_usuario = data['usuario']
    if usuario_id == 'E':
      #SELECT COUNT"(*) AS cantidad FROM usuarios WHERE usuario = ?
      n = session_db().query(Usuario).filter_by(usuario = nombre_usuario).count()
      rpta = str(n)
    else:
      #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ? AND id = ?
      n = session_db().query(Usuario).filter_by(usuario = nombre_usuario, id = usuario_id).count()
      if n == 1:
        rpta = '0'
      else:
        #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ?
        n = session_db().query(Usuario).filter_by(usuario = nombre_usuario).count()
        rpta = str(n)
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en validar si el nombre es repetido',
        str(e)
      ],
    }
    status = 500
    rpta = json.dumps(rpta)
  return HTTPResponse(status = status, body = rpta)

@usuario_view.route('/correo_repetido', method='POST')
@enable_cors
@headers
@check_csrf
def correo_repetido():
  rpta = None
  status = 200
  try:
    data = json.loads(request.forms.get('data'))
    usuario_id = data['id']
    correo = data['correo']
    if usuario_id == 'E':
      #SELECT COUNT(*) AS cantidad FROM usuarios WHERE correo = ?
      n = session_db().query(Usuario).filter_by(correo = correo).count()
      rpta = str(n)
    else:
      #SELECT COUNT(*) AS cantidad FROM usuarios WHERE correo = ? AND id = ?
      n = session_db().query(Usuario).filter_by(correo = correo, id = usuario_id).count()
      if n == 1:
        rpta = '0'
      else:
        #SELECT COUNT(*) AS cantidad FROM usuarios WHERE correo = ?
        n = session_db().query(Usuario).filter_by(correo = correo).count()
        rpta = str(n)
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en validar si el correo es repetido',
        str(e)
      ],
    }
    status = 500
    rpta = json.dumps(rpta)
  return HTTPResponse(status = status, body = rpta)

@usuario_view.route('/contrasenia_repetida', method='POST')
@enable_cors
@headers
@check_csrf
def contrasenia_repetida():
  rpta = None
  status = 200
  try:
    data = json.loads(request.forms.get('data'))
    usuario_id = data['id']
    contrasenia = data['contrasenia']
    n = session_db().query(Usuario).filter_by(contrasenia = contrasenia, id = usuario_id).count()
    rpta = str(n)
  except Exception as e:
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en validar si la contraseña del usuario',
         str(e)
       ],
     }
    status = 500
    rpta = json.dumps(rpta)
  return HTTPResponse(status = status, body = rpta)
