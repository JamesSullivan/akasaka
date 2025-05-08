-- This script will be executed by the PostgreSQL container on its first startup.
-- It's located in the /docker-entrypoint-initdb.d/ directory inside the container.

-- Create a new database
-- The name 'mydatabase' should match what you expect to connect to.
-- If you uncommented POSTGRES_DB in docker-compose.yml, this CREATE DATABASE command might
-- not be strictly necessary, but it's good practice to include it.
CREATE DATABASE akasaka_db OWNER puser;
CREATE USER puser WITH PASSWORD '${AKASAKA_DB_PW}';
ALTER ROLE puser SET client_encoding TO 'utf8';
ALTER ROLE puser SET default_transaction_isolation TO 'read committed';
ALTER ROLE puser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE akasaka_db TO puser;

-- Connect to the newly created database
\c akasaka_db;

