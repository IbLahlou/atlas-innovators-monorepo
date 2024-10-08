-- Create the abstract Person table
CREATE TABLE Person (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INTEGER
);

-- Create the Parent table
CREATE TABLE Parent (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INTEGER,
    child_id JSONB
) INHERITS (Person);

-- Create the Child table
CREATE TABLE Child (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INTEGER,
    score INTEGER,
    level INTEGER,
    parent_id JSONB
) INHERITS (Person);