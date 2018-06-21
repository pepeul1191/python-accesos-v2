#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request, template
from config.middleware import enable_cors, headers
from config.database import engine, session_db
from config.constants import constants
from config.helpers import load_css, load_js
from helpers.login_helper import login_index_css, login_index_js

login_view = Bottle()

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
