-- migrate:down
DROP TABLE IF EXISTS modulos;
-- migrate:up
CREATE TABLE modulos(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(30) NOT NULL,
	url	VARCHAR(20) NOT NULL,
	icono	VARCHAR(14),
  sistema_id INTEGER,
  FOREIGN KEY (sistema_id) REFERENCES sistemas(id) ON DELETE CASCADE
)