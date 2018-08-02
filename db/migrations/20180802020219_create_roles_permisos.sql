-- migrate:up

CREATE TABLE roles_permisos(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  rol_id INTEGER,
  permiso_id INTEGER,
  FOREIGN KEY (rol_id) REFERENCES roles(id) ON DELETE CASCADE,
  FOREIGN KEY (permiso_id) REFERENCES permisos(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS roles_permisos;
