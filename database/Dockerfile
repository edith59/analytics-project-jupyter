FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database
ADD queries /docker-entrypoint-initdb.d
ADD ml_latest_small /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*