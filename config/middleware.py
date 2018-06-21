#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
import json
from bottle import response, redirect, request, HTTPResponse
from config.constants import constants

def headers(fn):
  def _headers(*args, **kwargs):
    response.headers['Server'] = 'Ubuntu;WSGIServer/0.2;CPython/3.5.2'
    return fn(*args, **kwargs)
  return _headers

def enable_cors(fn):
  def _enable_cors(*args, **kwargs):
    # set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    if bottle.request.method != 'OPTIONS':
      # actual request; reply with the actual response
      return fn(*args, **kwargs)
  return _enable_cors

def check_csrf(fn):
  def _check_csrf(*args, **kwargs):
    #si csrf en el header NO coincide
    if constants['ambiente_csrf'] == 'activo':
      continuar = True
      mensaje = []
      if request.get_header(constants['CSRF']['key']) != None:
        if request.get_header(constants['CSRF']['key']) != constants['CSRF']['secret']:
          continuar = False
          mensaje = [
            'No se puede acceder al recurso',
            'CSRF Token key error'
          ]
      else:
        continuar = False
        mensaje = [
          'No se puede acceder al recurso',
          'CSRF Token error'
        ]
      if continuar == True:
        return fn(*args, **kwargs)
      else:
        rpta = {
          'tipo_mensaje' : 'error',
          'mensaje' : mensaje
        }
        return HTTPResponse(status = 500, body = json.dumps(rpta))
    else:
      return fn(*args, **kwargs)
  return _check_csrf

def session_false(fn):
  def _session_false(*args, **kwargs):
    #si la session es activaa, vamos a '/accesos/'
    if constants['ambiente_session'] == 'activo':
      s = request.environ.get('beaker.session')
      if s != None:
        if s.has_key('activo') == True:
          if s['activo'] == True:
            return redirect("/accesos/")
      return fn(*args, **kwargs)
    #else: contnuar
    else:
      return fn(*args, **kwargs)
  return _session_false

def session_true(fn):
  def _session_true(*args, **kwargs):
    #si la session es activaa, vamos a '/accesos/'
    if constants['ambiente_session'] == 'activo':
      s = request.environ.get('beaker.session')
      if s != None:
        if s.has_key('activo') == True:
          if s['activo'] == False:
            return redirect("/error/access/505")
        else:
          return redirect("/error/access/505")
      else:
        return redirect("/error/access/505")
    return fn(*args, **kwargs)
  return _session_true
