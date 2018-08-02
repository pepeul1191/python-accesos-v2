-- migrate:up

CREATE TABLE usuarios_permisos(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  usuario_id INTEGER,
  permiso_id INTEGER,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
  FOREIGN KEY (permiso_id) REFERENCES permisos(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS usuarios_permisos;
