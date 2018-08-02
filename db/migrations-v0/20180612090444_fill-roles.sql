-- migrate:down
--TRUNCATE TABLE roles;
-- migrate:up
INSERT INTO roles (nombre, sistema_id) VALUES (
  'Administrador',
  1
);