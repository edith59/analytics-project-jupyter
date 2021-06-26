SET datestyle = 'iso,dmy';
COPY links FROM '/docker-entrypoint-initdb.d/links.csv' DELIMITER ',' CSV HEADER;
COPY movies FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;
COPY ratings FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
COPY tags FROM '/docker-entrypoint-initdb.d/tags.csv' DELIMITER ',' CSV HEADER;