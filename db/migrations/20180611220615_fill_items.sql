-- migrate:down
--TRUNCATE TABLE items;
-- migrate:up
INSERT INTO items (nombre, url, subtitulo_id) VALUES (
  'Gestión de Sistemas',
  '#/sistema',
  1
);
INSERT INTO items (nombre, url, subtitulo_id) VALUES (
  'Gestión de Usuarios',
  '#/usuario',
  1
);