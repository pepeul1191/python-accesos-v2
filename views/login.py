#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from beaker.middleware import SessionMiddleware
from bottle import Bottle, request, template, HTTPResponse, redirect
from config.middleware import enable_cors, headers
from config.database import engine, session_db
from config.constants import constants
from config.session import session_opts
from config.helpers import load_css, load_js
from helpers.login_helper import login_index_css, login_index_js

login_view = Bottle()
SessionMiddleware(login_view, session_opts)

@login_view.route('/', method='GET')
@headers
def index():
  helpers = {}
  helpers['css'] = load_css(login_index_css())
  helpers['js'] = load_js(login_index_js())
  locals = {
    'constants': constants,
    'title': 'Bienvenido',
    'data': json.dumps({
      'modulo' : 'Accesos',
    }),
    'mensaje': '',
  }
  return template('templates/login/index', locals = locals, helpers = helpers)

@login_view.route('/acceder', method='POST')
@headers
def acceder():
  mensaje = ''
  continuar = True
  csrf_request = request.forms.get(constants['CSRF']['key'])
  if csrf_request == None:
    mensaje = 'Token CSRF no existe en POST request'
    continuar = False
  else:
    # validar csrf token
    if csrf_request != constants['CSRF']['secret']:
      mensaje = 'Token CSRF no existe en POST request'
      continuar = False
    # validar usuario y contraseña si csrf token es correcto
    if continuar == True:
      usuario_request = request.forms.get('usuario')
      contrasenia_request = request.forms.get('contrasenia')
      if (usuario_request != constants['login']['usuario']) or (contrasenia_request != constants['login']['contrasenia']):
        mensaje = 'Usuario y/o contraenia no coinciden'
        continuar = False
  if continuar == True:
    s = request.environ.get('beaker.session')
    s['activo'] = True
    print("1 ++++++++++++++++++++++++++++++++")
    print(s)
    print("2 ++++++++++++++++++++++++++++++++")
    print(s['activo'])
    print("3 ++++++++++++++++++++++++++++++++")
    return redirect("/accesos/")
  else:
    helpers = {}
    helpers['css'] = load_css(login_index_css())
    helpers['js'] = load_js(login_index_js())
    locals = {
      'constants': constants,
      'title': 'Bienvenido',
      'data': json.dumps({
        'modulo' : 'Accesos',
      }),
      'mensaje': mensaje,
    }
    boby_template = template('templates/login/index', locals = locals, helpers = helpers)
    return HTTPResponse(status = 500, body = boby_template)
