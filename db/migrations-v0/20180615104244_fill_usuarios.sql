-- migrate:down
--TRUNCATE TABLE usuarios;
-- migrate:up
INSERT INTO usuarios (usuario, contrasenia, correo, estado_usuario_id) VALUES (
  'pepe', 'kiki123', 'jvaldivia@softweb.pe', 1
);
INSERT INTO usuarios (usuario, contrasenia, correo, estado_usuario_id) VALUES (
  'yacky', 'koki123', 'yramirez@softweb.pe', 1
);