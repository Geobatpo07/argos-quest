CREATE TABLE IF NOT EXISTS schema_version
(
    version VARCHAR PRIMARY KEY,
    applied_at TIMESTAMP NOT NULL
);