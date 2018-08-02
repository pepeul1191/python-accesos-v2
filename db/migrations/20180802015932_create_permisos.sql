-- migrate:up

CREATE TABLE permisos(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(30) NOT NULL,
	llave	VARCHAR(30),
  sistema_id INTEGER,
  FOREIGN KEY (sistema_id) REFERENCES sistemas(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS permisos;
