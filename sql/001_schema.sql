CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE targets (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  host TEXT NOT NULL,
  kind TEXT NOT NULL CHECK (kind IN ('ping', 'speedtest')),

  UNIQUE (name)
);

CREATE TABLE measurements (
  time TIMESTAMPTZ NOT NULL,
  target_id INTEGER NOT NULL REFERENCES targets(id),
  metric TEXT NOT NULL,
  value DOUBLE PRECISION NOT NULL,

  UNIQUE (time, target_id, metric)
);

SELECT create_hypertable('measurements', 'time');