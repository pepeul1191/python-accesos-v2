-- migrate:down
DROP VIEW IF EXISTS vw_usuarios_roles;
-- migrate:up sqlite3
CREATE VIEW vw_usuarios_roles AS SELECT 
  R.id AS id, U.id AS usuario_id, U.usuario AS usuario, R.nombre AS nombre, 0 AS existe  
  FROM usuarios_roles UR 
  INNER JOIN usuarios U ON U.id = UR.usuario_id 
  INNER JOIN roles R ON R.id = UR.rol_id  
  LIMIT 2000;