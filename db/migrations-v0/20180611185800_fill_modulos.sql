-- migrate:down
--TRUNCATE TABLE modulos;
--UP
INSERT INTO modulos (nombre, url, icono, sistema_id) VALUES (
  'Accesos',
  'accesos/',
  '',
  1
);
