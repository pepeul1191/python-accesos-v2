-- migrate:up

INSERT INTO usuarios_sistemas (usuario_id, sistema_id) VALUES (
  1,1
);

-- migrate:down
