# PostGres Docker Container

This document explains how to use Docker Compose and a SQL initialization script to create a PostgreSQL container with a pre-loaded database that you can connect to locally.  
**Steps:**

 
1. Run the command `docker compose up -d`.  
   * docker compose up: This command reads the docker-compose.yml file, builds (if necessary) and starts the services defined in it.  
   * `-d`: This flag runs the containers in detached mode (in the background).  
   * Note as this is a single container, once created it can also be started by `docker start docker-db-1`
2. Docker will pull the postgres image (if you don't have it), create a network, a volume for persistent data, and start the PostgreSQL container. The init.sql script will run automatically on the first startup.  
3. To connect via shell `PGPASSWORD=$AKASAKA_DB_PW psql -h localhost -p 5432 -d postgres -U puser`
   `drop database fin_report;`
4. You should now be able to connect to your PostgreSQL database locally using a client (like psql, pgAdmin, DBeaver, etc.) with the following details:  
   * **Host:** localhost  
   * **Port:** 5432 (or the port you specified in docker-compose.yml)  
   * **Database:** mydatabase (or the database name you created in init.sql)  
   * **User:** myuser (or the user you specified in docker-compose.yml)  
   * **Password:** mypassword (or the password you specified in docker-compose.yml)

**To stop the container:**  
In the same directory, run `docker compose down`. This will stop and remove the container, the default network, and the volume (unless you specify not to remove volumes).  
**Important:** The pgdata volume is used to persist your database data. If you stop and restart the container using docker compose up, your data will still be there. If you remove the volume (e.g., using 'docker compose down -v'), the data will be lost, and the init.sql script will run again on the next docker compose up.


