-- migrate:up

CREATE VIEW vw_usuario_correo_estado AS SELECT
U.id, U.usuario, U.correo, EU.id AS estado_usuario_id, EU.nombre AS estado_usuario_nombre FROM
usuarios U
INNER JOIN estado_usuarios EU ON EU.id = U.estado_usuario_id
LIMIT 2000;

-- migrate:down

DROP VIEW IF EXISTS vw_usuario_correo_estado;
