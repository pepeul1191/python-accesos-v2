#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config.constants import constants

def login_index_css():
  switcher = {
    'desarrollo': [
      'bower_components/bootstrap/dist/css/bootstrap.min',
      'bower_components/font-awesome/css/font-awesome.min',
      'bower_components/swp-backbone/assets/css/constants',
      'bower_components/swp-backbone/assets/css/login',
      'assets/css/constants',
      'assets/css/login',
    ],
    'produccion': ['dist/login.min'],
  }
  return switcher.get(constants['ambiente_static'])

def login_index_js():
  switcher = {
    'desarrollo': [],
    'produccion': [],
  }
  return switcher.get(constants['ambiente_static'])
