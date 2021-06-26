SET datestyle = 'iso,dmy';
SET standard_conforming_strings = 0;
CREATE TABLE IF NOT EXISTS links (movieId INT, imdbId INT,tmdbId INT);
CREATE TABLE IF NOT EXISTS movies (movieId INT, title VARCHAR, genres VARCHAR);
CREATE TABLE IF NOT EXISTS ratings (userId INT, movieId INT, rating float, timestamp BIGINT );
CREATE TABLE IF NOT EXISTS tags (userId INT, movieId INT, tag varchar, timestamp BIGINT);