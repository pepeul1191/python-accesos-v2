<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{locals['title']}}</title>
  {{!helpers['css']}}
  <script type="text/javascript">
    var BASE_URL = '{{locals['constants']['BASE_URL']}}';
    var STATICS_URL  = '{{locals['constants']['STATIC_URL']}}';
    var MODULOS_JSON = JSON.parse('{{!locals['menu']}}');
    var ITEMS_JSON = JSON.parse('{{!locals['items']}}');
    var DATA = JSON.parse('{{!locals['data']}}');
    var CSRF = '{{locals['constants']['CSRF']['secret']}}';
    var CSRF_KEY = '{{locals['constants']['CSRF']['key']}}';;
  </script>
</head>
<body>
  <label id="defaultTargetMensajes"></label>
  <!-- Inicio modal -->
  <button type="button" class="btn btn-primary btn-lg oculto" data-toggle="modal" data-target="#modal-container" id="btnModal">Launch demo modal</button>
  <div class="modal fade" id="modal-container" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          ...
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Fin modal -->
  <div id="app"></div>
  <!-- Handlebars Templates -->
  <script id="template" type="text/x-handlebars-template">
    {{!"{{> header}}"}}
    {{!"{{> breadcrumb}}"}}
    {{!"{{> contenido}}"}}
    {{!"{{> footer}}"}}
  </script>
  <script id="header-template" type="text/x-handlebars-template">
    <header>
      <a href="{{"{{BASE_URL}}"}}">Inicio</a>
      <a href="{{"{{BASE_URL}}"}}ayuda">Ayuda</a>
      <a href="{{"{{BASE_URL}}"}}login/ver" class="pull-right">Pepe Valdivia</a>
      <a href="{{"{{BASE_URL}}"}}login/cerrar" class="pull-right">Cerrar Sesión</a>
    </header>
  </nav>
  <!-- Fin Header -->
  </script>
  <script id="breadcrumb-template" type="text/x-handlebars-template">
    <nav>
      <h1><i class="fa fa-universal-access h1" aria-hidden="true"></i>Gestión de Accesos</h1>
      {{"{{{menuModulos}}}"}}
    </nav>
  </script>
  <script id="contenido-template" type="text/x-handlebars-template">
    <div id="body-app" class="row">
      <aside class="col-md-2">
        {{"{{{menuSubModulos}}}"}}
      </aside>
      <section class="col-md-10" id="workspace">
        <!-- Inicio Yield-->
        {{!"{{> yield}}"}}
        <!-- Fin Yield-->
      </section>
    </div>
  </script>
