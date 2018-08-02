-- migrate:down
DROP TABLE IF EXISTS usuarios_sistemas;
-- migrate:up
CREATE TABLE usuarios_sistemas(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  usuario_id INTEGER,
  sistema_id INTEGER,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
  FOREIGN KEY (sistema_id) REFERENCES sistemas(id) ON DELETE CASCADE
)