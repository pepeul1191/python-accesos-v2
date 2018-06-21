#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, HTTPResponse
from config.models import Usuario, VWUsuarioCorreoEstado, UsuarioSistema, UsuarioRol, UsuarioPermiso
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

@usuario_view.route('/guardar_usuario_correo', method='POST')
@enable_cors
@headers
@check_csrf
def guardar_usuario_correo():
  rpta = None
  status = 200
  try:
    data = json.loads(request.forms.get('usuario'))
    usuario_id = data['id']
    correo = data['correo']
    nombre_usuario = data['usuario']
    estado_usuario_id = data['estado_usuario_id']
    session = session_db()
    session.query(Usuario).filter_by(id = usuario_id).update({
      'usuario': nombre_usuario,
      'correo': correo,
      'estado_usuario_id': estado_usuario_id
    })
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado los cambios en los datos generales del usuario',
      ]
    }
  except Exception as e:
    print(e)
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

@usuario_view.route('/guardar_contrasenia', method='POST')
@enable_cors
@headers
@check_csrf
def guardar_contrasenia():
  rpta = None
  status = 200
  try:
    data = json.loads(request.forms.get('contrasenia'))
    usuario_id = data['id']
    contrasenia = data['contrasenia']
    session = session_db()
    session.query(Usuario).filter_by(id = usuario_id).update({
      'contrasenia': contrasenia,
    })
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha el cambio de contraseña del usuario',
      ]
    }
  except Exception as e:
    print(e)
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en actualizar la contraseña del usaurio',
         str(e)
       ],
     }
    status = 500
  rpta = json.dumps(rpta)
  return HTTPResponse(status = status, body = rpta)

@usuario_view.route('/sistema/<usuario_id>', method='GET')
@enable_cors
@headers
@check_csrf
def sistema(usuario_id):
  rpta = None
  status = 200
  try:
    session = session_db()
    rs = session.execute('''
      SELECT T.id AS id, T.nombre AS nombre, (CASE WHEN (P.existe = 1) THEN 1 ELSE 0 END) AS existe FROM
      (
        SELECT id, nombre, 0 AS existe FROM sistemas
      ) T
      LEFT JOIN
      (
        SELECT S.id, S.nombre, 1 AS existe FROM sistemas S
        INNER JOIN usuarios_sistemas US ON US.sistema_id = S.id
        WHERE US.usuario_id = :usuario_id
      ) P
      ON T.id = P.id'''
      , {'usuario_id': usuario_id})
    rpta = [dict(r) for r in rs]
    session.commit()
  except Exception as e:
    print(e)
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error en  listar los sistema del usuario',
         str(e)
       ],
     }
    status = 500
  rpta = json.dumps(rpta)
  return HTTPResponse(status = status, body = rpta)

@usuario_view.route('/sistema/guardar', method='POST')
@enable_cors
@headers
def guardar():
  status = 200
  data = json.loads(request.forms.get('data'))
  editados = data['editados']
  usuario_id = data['extra']['usuario_id']
  array_nuevos = []
  rpta = None
  session = session_db()
  try:
    if len(editados) != 0:
      for editado in editados:
        sistema_id = editado['id']
        existe = editado['existe']
        e = session.query(UsuarioSistema).filter_by(sistema_id = sistema_id, usuario_id = usuario_id).first()
        if existe == 0: #borrar si existe
          if e != None:
            session.query(UsuarioSistema).filter_by(sistema_id = sistema_id, usuario_id = usuario_id).delete()
        elif existe == 1:#crear si no existe
          if e == None:
            s = UsuarioSistema(
              sistema_id = sistema_id,
              usuario_id = usuario_id,
            )
            session.add(s)
            session.flush()
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado la asociación de sistemas al usuario',
        array_nuevos
      ]
    }
  except Exception as e:
    status = 500
    session.rollback()
    rpta = {
      'tipo_mensaje' : 'error',
      'mensaje' : [
        'Se ha producido un error en asociar los sistemas al usuario',
        str(e)
      ]
    }
  return HTTPResponse(status = status, body = json.dumps(rpta))

@usuario_view.route('/rol/<sistema_id>/<usuario_id>', method='GET')
@enable_cors
@headers
@check_csrf
def rol(sistema_id, usuario_id):
  rpta = None
  status = 200
  try:
    session = session_db()
    rs = session.execute('''
      SELECT T.id AS id, T.nombre AS nombre, (CASE WHEN (P.existe = 1) THEN 1 ELSE 0 END) AS existe FROM
	  (
		SELECT id, nombre, 0 AS existe FROM roles WHERE sistema_id = :sistema_id
	  ) T
	  LEFT JOIN
	  (
		SELECT R.id, R.nombre, 1 AS existe  FROM roles R
		INNER JOIN usuarios_roles UR ON R.id = UR.rol_id
		WHERE UR.usuario_id = :usuario_id
	  ) P
	  ON T.id = P.id'''
      , {'usuario_id': usuario_id, 'sistema_id': sistema_id})
    rpta = [dict(r) for r in rs]
    session.commit()
  except Exception as e:
    print(e)
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error error en listar los roles del usuario',
         str(e)
       ],
     }
    status = 500
  rpta = json.dumps(rpta)
  return HTTPResponse(status = status, body = rpta)

@usuario_view.route('/rol/guardar', method='POST')
@enable_cors
@headers
def guardar():
  status = 200
  data = json.loads(request.forms.get('data'))
  editados = data['editados']
  usuario_id = data['extra']['usuario_id']
  array_nuevos = []
  rpta = None
  session = session_db()
  try:
    if len(editados) != 0:
      for editado in editados:
        rol_id = editado['id']
        existe = editado['existe']
        e = session.query(UsuarioRol).filter_by(rol_id = rol_id, usuario_id = usuario_id).first()
        if existe == 0: #borrar si existe
          if e != None:
            session.query(UsuarioRol).filter_by(rol_id = rol_id, usuario_id = usuario_id).delete()
        elif existe == 1:#crear si no existe
          if e == None:
            s = UsuarioRol(
              rol_id = rol_id,
              usuario_id = usuario_id,
            )
            session.add(s)
            session.flush()
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado la asociación de roles al usuario',
        array_nuevos
      ]
    }
  except Exception as e:
    status = 500
    session.rollback()
    rpta = {
      'tipo_mensaje' : 'error',
      'mensaje' : [
        'Se ha producido un error en asociar los roles al usuario',
        str(e)
      ]
    }
  return HTTPResponse(status = status, body = json.dumps(rpta))

@usuario_view.route('/permiso/<sistema_id>/<usuario_id>', method='GET')
@enable_cors
@headers
@check_csrf
def permiso(sistema_id, usuario_id):
  rpta = None
  status = 200
  try:
    session = session_db()
    rs = session.execute('''
      SELECT T.id AS id, T.nombre AS nombre, (CASE WHEN (P.existe = 1) THEN 1 ELSE 0 END) AS existe, T.llave AS llave FROM
	  (
		SELECT id, nombre, llave, 0 AS existe FROM permisos WHERE sistema_id = :sistema_id
	  ) T
	  LEFT JOIN
	  (
		SELECT P.id, P.nombre,  P.llave, 1 AS existe  FROM permisos P
		INNER JOIN usuarios_permisos UP ON P.id = UP.permiso_id
		WHERE UP.usuario_id = :usuario_id
	  ) P
	ON T.id = P.id'''
      , {'usuario_id': usuario_id, 'sistema_id': sistema_id})
    rpta = [dict(r) for r in rs]
    session.commit()
  except Exception as e:
    print(e)
    rpta = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Se ha producido un error error en listar los permisos del usuario',
         str(e)
       ],
     }
    status = 500
  rpta = json.dumps(rpta)
  return HTTPResponse(status = status, body = rpta)

@usuario_view.route('/permiso/guardar', method='POST')
@enable_cors
@headers
def guardar():
  status = 200
  data = json.loads(request.forms.get('data'))
  editados = data['editados']
  usuario_id = data['extra']['usuario_id']
  array_nuevos = []
  rpta = None
  session = session_db()
  try:
    if len(editados) != 0:
      for editado in editados:
        permiso_id = editado['id']
        existe = editado['existe']
        e = session.query(UsuarioPermiso).filter_by(permiso_id = permiso_id, usuario_id = usuario_id).first()
        if existe == 0: #borrar si existe
          if e != None:
            session.query(UsuarioPermiso).filter_by(permiso_id = permiso_id, usuario_id = usuario_id).delete()
        elif existe == 1:#crear si no existe
          if e == None:
            s = UsuarioPermiso(
              permiso_id = permiso_id,
              usuario_id = usuario_id,
            )
            session.add(s)
            session.flush()
    session.commit()
    rpta = {
      'tipo_mensaje' : 'success',
      'mensaje' : [
        'Se ha registrado la asociación de permisos al usuario',
        array_nuevos
      ]
    }
  except Exception as e:
    status = 500
    session.rollback()
    rpta = {
      'tipo_mensaje' : 'error',
      'mensaje' : [
        'Se ha producido un error en asociar los permisos al usuario',
        str(e)
      ]
    }
  return HTTPResponse(status = status, body = json.dumps(rpta))
