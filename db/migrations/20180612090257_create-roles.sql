-- migrate:down
DROP TABLE IF EXISTS roles;
-- migrate:up
CREATE TABLE roles(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre	VARCHAR(30) NOT NULL,
  sistema_id INTEGER,
  FOREIGN KEY (sistema_id) REFERENCES sistemas(id) ON DELETE CASCADE
)