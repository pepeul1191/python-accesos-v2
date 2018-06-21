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
