#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
from bottle import Bottle, run, HTTPResponse, static_file, redirect
from beaker.middleware import SessionMiddleware
from config.middleware import headers
from config.session import session_opts
from views.estacion import estacion_view
from views.accesos import accesos_view
from views.sistema import sistema_view
from views.modulo import modulo_view
from views.subtitulo import subtitulo_view
from views.item import item_view
from views.permiso import permiso_view
from views.rol import rol_view
from views.login import login_view

app = SessionMiddleware(bottle.app(), session_opts)

@bottle.route('/')
@headers
def index():
  the_body = 'Error : URI vacía'
  return HTTPResponse(status=404, body=the_body)

@bottle.route('/test/conexion')
def test_conexion():
  return 'Ok'

@bottle.route('/accesos')
def test_conexion():
  return redirect("/accesos/")

@bottle.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./static/')

if __name__ == '__main__':
  # login
  bottle.mount('/login', login_view)
  # accesos
  bottle.mount('/accesos/', accesos_view)
  # servicios REST
  bottle.mount('/estacion', estacion_view)
  bottle.mount('/sistema', sistema_view)
  bottle.mount('/modulo', modulo_view)
  bottle.mount('/subtitulo', subtitulo_view)
  bottle.mount('/item', item_view)
  bottle.mount('/permiso', permiso_view)
  bottle.mount('/rol', rol_view)
  bottle.run(app = app, host='localhost', port=3025, debug=True, reloader=True)
  #@bottle.run(host='localhost', port=3025, debug=True)
