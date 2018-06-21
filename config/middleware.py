#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
from bottle import response, redirect, request

def headers(fn):
  def _headers(*args, **kwargs):
    response.headers['Server'] = 'Ubuntu;WSGIServer/0.2;CPython/3.5.2'
    return fn(*args, **kwargs)
  return _headers

def enable_cors(fn):
  def _enable_cors(*args, **kwargs):
    # set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    if bottle.request.method != 'OPTIONS':
      # actual request; reply with the actual response
      return fn(*args, **kwargs)
  return _enable_cors

def session_false(fn):
  def _session_false(*args, **kwargs):
    #si la session es activaa, vamos a '/accesos/'
    s = request.environ.get('beaker.session')
    if s != None:
      if s.has_key('activo') == True:
        if s['activo'] == True:
          return redirect("/accesos/")
    #else: contnuar
    return fn(*args, **kwargs)
  return _session_false

def session_true(fn):
  def _session_true(*args, **kwargs):
    #si la session es activaa, vamos a '/accesos/'
    s = request.environ.get('beaker.session')
    if s != None:
      if s.has_key('activo') == True:
        if s['activo'] == False:
          return redirect("/error/access/505")
      else:
        return redirect("/error/access/505")
    else:
      return redirect("/error/access/505")
    return fn(*args, **kwargs)
  return _session_true
