-- migrate:up

CREATE TABLE estado_usuarios(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(20) NOT NULL
)

-- migrate:down

DROP VIEW IF EXISTS estado_usuarios;
