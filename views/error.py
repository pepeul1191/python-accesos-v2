#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, HTTPResponse, template
from config.middleware import headers
from config.constants import constants
from config.helpers import load_css, load_js
from helpers.error_helper import error_access_css, error_access_js

error_view = Bottle()

@error_view.route('/access/<numero_error>', method='GET')
@headers
def access(numero_error):
  helpers = {}
  helpers['css'] = load_css(error_access_css())
  helpers['js'] = load_js(error_access_js())
  errores = {
    '404' : {
      'mensaje': 'Archivo no encontrado',
      'numero': '404',
      'descripcion': 'La página que busca no se encuentra en el servidor',
    },
    '505' : {
      'mensaje': 'Acceso restringido',
      'numero': '505',
      'descripcion': 'Necesita estar logueado',
    },
  }
  locals = {
    'constants': constants,
    'title': 'Error',
    'mensaje': errores[str(numero_error)]['mensaje'],
    'numero': errores[str(numero_error)]['numero'],
    'descripcion': errores[str(numero_error)]['descripcion'],
  }
  boby_template = template('templates/error/access', locals = locals, helpers = helpers)
  return HTTPResponse(status = 404, body = boby_template)
