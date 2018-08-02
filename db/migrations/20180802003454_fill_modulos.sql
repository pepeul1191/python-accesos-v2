-- migrate:up

INSERT INTO modulos (nombre, url, icono, sistema_id) VALUES (
  'Accesos',
  'accesos/',
  '',
  1
);

-- migrate:down
