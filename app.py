#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, HTTPResponse, static_file, redirect
from config.middleware import headers
from views.estacion import estacion_view
from views.accesos import accesos_view
from views.sistema import sistema_view
from views.modulo import modulo_view
from views.subtitulo import subtitulo_view
from views.item import item_view
from views.permiso import permiso_view
from views.rol import rol_view
from views.login import login_view

app = Bottle()

@app.route('/')
@headers
def index():
  the_body = 'Error : URI vacía'
  return HTTPResponse(status=404, body=the_body)

@app.route('/test/conexion')
def test_conexion():
  return 'Ok'

@app.route('/accesos')
def test_conexion():
  return redirect("/accesos/")

@app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./static/')

if __name__ == '__main__':
  # login
  app.mount('/login', login_view)
  # accesos
  app.mount('/accesos/', accesos_view)
  # servicios REST
  app.mount('/estacion', estacion_view)
  app.mount('/sistema', sistema_view)
  app.mount('/modulo', modulo_view)
  app.mount('/subtitulo', subtitulo_view)
  app.mount('/item', item_view)
  app.mount('/permiso', permiso_view)
  app.mount('/rol', rol_view)
  #app.run(host='localhost', port=3025, debug=True, reloader=True)
  app.run(host='localhost', port=3025, debug=True)
