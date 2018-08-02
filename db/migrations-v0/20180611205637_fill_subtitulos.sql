-- migrate:down
--TRUNCATE TABLE subtitulos;
-- migrate:up
INSERT INTO subtitulos (nombre, modulo_id) VALUES (
  'Opciones',
  1
);