-- migrate:up

CREATE TABLE subtitulos(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(30) NOT NULL,
  modulo_id INTEGER,
  FOREIGN KEY (modulo_id) REFERENCES modulos(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS subtitulos;
