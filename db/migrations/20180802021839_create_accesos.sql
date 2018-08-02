-- migrate:up

CREATE TABLE accesos(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  momento DATETIME NOT NULL,
  usuario_id INTEGER,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS accesos;
