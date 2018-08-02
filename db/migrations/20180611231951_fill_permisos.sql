-- migrate:down
--TRUNCATE TABLE permisos;
-- migrate:up
INSERT INTO permisos (nombre, llave, sistema_id) VALUES (
  'Listar Sistemas',
  'sistema_listar',
  1
);
INSERT INTO permisos (nombre, llave, sistema_id) VALUES (
  'Listar Módulos de Sistema',
  'sistema_modulo_listar',
  1
);