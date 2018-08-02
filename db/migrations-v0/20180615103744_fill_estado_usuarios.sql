-- migrate:down
--TRUNCATE TABLE estado_usuarios;
-- migrate:up
INSERT INTO estado_usuarios (nombre) VALUES (
  'activo'
);
INSERT INTO estado_usuarios (nombre) VALUES (
  'bloqueado'
);
INSERT INTO estado_usuarios (nombre) VALUES (
  'eliminado'
);