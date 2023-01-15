FROM postgres:11.3-alpine

ENV POSTGRES_INITDB_ARGS --locale=fi_FI

COPY init-database.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init-database.sh