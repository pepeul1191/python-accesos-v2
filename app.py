#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
import json
from bottle import Bottle, run, HTTPResponse, static_file, redirect, error, template
from beaker.middleware import SessionMiddleware
from config.middleware import headers
from config.helpers import load_css, load_js
from config.session import session_opts
from config.constants import constants
from views.estacion import estacion_view
from views.accesos import accesos_view
from views.sistema import sistema_view
from views.modulo import modulo_view
from views.subtitulo import subtitulo_view
from views.item import item_view
from views.permiso import permiso_view
from views.rol import rol_view
from views.login import login_view
from helpers.error_helper import error_access_css, error_access_js

main_app = bottle.app()
app = SessionMiddleware(main_app, session_opts)

@main_app.route('/')
@headers
def index():
  return redirect("/accesos/")

@main_app.route('/test/conexion')
def test_conexion():
  return 'Ok'

@main_app.route('/accesos')
def test_conexion():
  return redirect("/accesos/")

@error(404)
def error404(error):
  helpers = {}
  helpers['css'] = load_css(error_access_css())
  helpers['js'] = load_js(error_access_js())
  locals = {
    'constants': constants,
    'title': 'Bienvenido',
    'mensaje': 'Archivo no encontrado',
    'numero': '404',
    'descripcion': 'La página que busca no se encuentra en el servidor',
  }
  boby_template = template('templates/error/access', locals = locals, helpers = helpers)
  return HTTPResponse(status = 404, body = boby_template)

@error(405)
def error405(error):
  rpta = {
    'tipo_mensaje' : 'error',
    'mensaje' : [
      'Recurso no disponible',
      'Error 404'
    ]
  }
  return HTTPResponse(status = 404, body = json.dumps(rpta))


@main_app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./static/')

if __name__ == '__main__':
  # login
  main_app.mount('/login', login_view)
  # accesos
  main_app.mount('/accesos/', accesos_view)
  # servicios REST
  main_app.mount('/estacion', estacion_view)
  main_app.mount('/sistema', sistema_view)
  main_app.mount('/modulo', modulo_view)
  main_app.mount('/subtitulo', subtitulo_view)
  main_app.mount('/item', item_view)
  main_app.mount('/permiso', permiso_view)
  main_app.mount('/rol', rol_view)
  #bottle.run(app = app, host='localhost', port=3025, debug=True, reloader=True)
  bottle.run(app = app, host='localhost', port=3025, debug=True)
