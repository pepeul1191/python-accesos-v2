#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config.constants import constants

def error_access_css():
  switcher = {
    'desarrollo': [
      'bower_components/bootstrap/dist/css/bootstrap.min',
      'bower_components/font-awesome/css/font-awesome.min',
      'bower_components/swp-backbone/assets/css/constants',
      'assets/css/constants',
      'assets/css/error',
    ],
    'produccion': ['dist/error.min'],
  }
  return switcher.get(constants['ambiente_static'])

def error_access_js():
  switcher = {
    'desarrollo': [],
    'produccion': [],
  }
  return switcher.get(constants['ambiente_static'])
