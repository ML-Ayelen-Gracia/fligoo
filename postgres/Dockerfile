FROM postgres:13

# Copy the SQL script to the init script directory
COPY 01_create_db.sql /docker-entrypoint-initdb.d/01_create_db.sql
COPY 02_create_schema.sql /docker-entrypoint-initdb.d/02_create_schema.sql