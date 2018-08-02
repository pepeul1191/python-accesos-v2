-- migrate:up

INSERT INTO roles (nombre, sistema_id) VALUES (
  'Administrador',
  1
);

-- migrate:down
