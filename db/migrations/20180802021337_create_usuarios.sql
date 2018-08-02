-- migrate:up

CREATE TABLE usuarios(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  usuario VARCHAR(20) NOT NULL,
  contrasenia VARCHAR(30) NOT NULL,
  correo VARCHAR(30) NOT NULL,
  estado_usuario_id INTEGER,
  FOREIGN KEY (estado_usuario_id) REFERENCES estado_usuarios(id) ON DELETE CASCADE
)

-- migrate:down

DROP TABLE IF EXISTS usuarios;
