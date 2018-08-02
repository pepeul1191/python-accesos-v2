-- migrate:down
DROP TABLE IF EXISTS estado_usuarios;
-- migrate:up
CREATE TABLE estado_usuarios(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(20) NOT NULL
)