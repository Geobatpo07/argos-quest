# ./infrastructure/database/schema.py

SCHEMA = """

CREATE TABLE IF NOT EXISTS thesis(

    id UUID PRIMARY KEY,

    title TEXT,

    laboratory TEXT,

    organization TEXT,

    city TEXT,

    country TEXT,

    description TEXT,

    domain TEXT,

    funding TEXT,

    deadline DATE,

    url TEXT,

    score DOUBLE,

    created_at TIMESTAMP

);

"""