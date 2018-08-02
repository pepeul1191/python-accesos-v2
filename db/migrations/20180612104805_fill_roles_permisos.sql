-- migrate:down
--TRUNCATE TABLE roles_permisos;
-- migrate:up
INSERT INTO roles_permisos (rol_id, permiso_id) VALUES (
  1,1
);
INSERT INTO roles_permisos (rol_id, permiso_id) VALUES (
  1,2
);