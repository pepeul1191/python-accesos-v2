-- migrate:up

CREATE TABLE sistemas (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(30) NOT NULL,
	version	VARCHAR(6),
	repositorio	VARCHAR(200)
);

-- migrate:down

DROP TABLE IF EXISTS sistemas;
