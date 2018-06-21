#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, template
from sqlalchemy.sql import select
from config.middleware import session_true, headers
from config.database import engine, session_db
from config.constants import constants
from config.helpers import load_css, load_js
from helpers.accesos_helper import accesos_index_css, accesos_index_js

accesos_view = Bottle()

@accesos_view.route('/', method='GET')
@headers
@session_true
def index():
  helpers = {}
  helpers['css'] = load_css(accesos_index_css())
  helpers['js'] = load_js(accesos_index_js())
  locals = {
    'constants': constants,
    'title': 'Gestión de Accesos',
    'data': json.dumps({
      'modulo' : 'Accesos',
    }),
    'menu': json.dumps([
      {
        'url' : 'accesos/',
        'nombre' : 'Accesos'
      },
    ]),
    'items': json.dumps([
      {
        'subtitulo':'Opciones',
        'items':
		  [
		    {
              'item':'Gestión de Sistemas',
              'url':'accesos/#/sistema'
            },
            {
              'item':'Gestión de Usuarios',
              'url':'accesos/#/usuario'
            },
		  ]
	  },
    ]),
  }
  return template('templates/accesos/index', locals = locals, helpers = helpers)
