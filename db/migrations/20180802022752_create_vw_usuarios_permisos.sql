-- migrate:up

CREATE VIEW vw_usuarios_permisos AS SELECT
  P.id AS id, P.llave AS llave, U.id AS usuario_id, U.usuario AS usuario, P.nombre AS nombre, 0 AS existe
  FROM usuarios_permisos UP
  INNER JOIN usuarios U ON U.id = UP.usuario_id
  INNER JOIN permisos P ON P.id = UP.permiso_id
  LIMIT 2000;

-- migrate:down

DROP VIEW IF EXISTS vw_usuarios_permisos;
