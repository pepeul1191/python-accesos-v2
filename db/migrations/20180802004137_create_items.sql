-- migrate:up

CREATE TABLE items(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(30) NOT NULL,
  url	VARCHAR(30) NOT NULL,
  subtitulo_id INTEGER,
  FOREIGN KEY (subtitulo_id) REFERENCES subtitulos(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS items;
