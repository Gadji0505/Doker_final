CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');

