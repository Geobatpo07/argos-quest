CREATE TABLE IF NOT EXISTS schema_version
(
    version VARCHAR PRIMARY KEY,
    applied_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS thesis
(
    id UUID PRIMARY KEY,

    title TEXT NOT NULL,

    reference TEXT,

    source TEXT NOT NULL,

    organization TEXT NOT NULL,

    laboratory TEXT NOT NULL,

    team TEXT,

    city TEXT,

    country TEXT,

    domain TEXT,

    funding TEXT,

    deadline DATE,

    summary TEXT,

    description TEXT,

    url TEXT NOT NULL,

    score DOUBLE DEFAULT 0,

    is_active BOOLEAN DEFAULT TRUE,

    scraped_at TIMESTAMP NOT NULL,

    created_at TIMESTAMP NOT NULL
);