-- migrate:down
DROP VIEW IF EXISTS vw_usuarios_sistemas;
-- migrate:up sqlite3
CREATE VIEW vw_usuarios_sistemas AS SELECT 
  S.id AS id, U.id AS usuario_id, U.usuario AS usuario, S.nombre AS nombre, 0 AS existe  
  FROM usuarios_sistemas US 
  INNER JOIN usuarios U ON U.id = US.usuario_id 
  INNER JOIN sistemas S ON S.id = US.sistema_id  
  LIMIT 2000;