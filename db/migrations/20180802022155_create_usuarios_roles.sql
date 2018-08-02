-- migrate:up

CREATE TABLE usuarios_roles(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  usuario_id INTEGER,
  rol_id INTEGER,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
  FOREIGN KEY (rol_id) REFERENCES roles(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS usuarios_roles;
