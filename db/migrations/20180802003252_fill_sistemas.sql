-- migrate:up

INSERT INTO sistemas (nombre, version, repositorio) VALUES (
  'java-spark-accesos',
  '0.0.1',
  'https://github.com/pepeul1191/java-spark-accesos'
);
INSERT INTO sistemas (nombre, version, repositorio) VALUES (
  'swp-backbone-js-plugins',
  '0.1.1',
  'https://github.com/pepeul1191/swp-backbone-js-plugins'
);

-- migrate:down
