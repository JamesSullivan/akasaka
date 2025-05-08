-- This script will be executed by the PostgreSQL container on its first startup.
-- It's located in the /docker-entrypoint-initdb.d/ directory inside the container.

-- Create a new database
-- The name 'mydatabase' should match what you expect to connect to.
-- If you uncommented POSTGRES_DB in docker-compose.yml, this CREATE DATABASE command might
-- not be strictly necessary, but it's good practice to include it.
CREATE DATABASE mydatabase OWNER puser;

-- Connect to the newly created database
\c mydatabase;

-- Create a simple table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- Insert some sample data into the table
INSERT INTO users (name, email) VALUES
('Alice Smith', 'alice.smith@example.com'),
('Bob Johnson', 'bob.johnson@example.com'),
('Charlie Brown', 'charlie.brown@example.com');

-- You can add more SQL commands here to set up your database schema,
-- create other tables, add more data, set up roles, etc.

