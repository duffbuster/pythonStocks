CREATE DATABASE IF NOT EXISTS stockTickers;
GRANT ALL PRIVILEGES ON stockTickers.* to 'user'@'localhost' 
identified by 'password';
USE stockTickers;

/* Set up initial user table structure */

CREATE TABLE users
(
  firstName VARCHAR(256),
  lastName VARCHAR(256),
  username VARCHAR(256),
  password VARCHAR(256),
  PRIMARY KEY (username)
);
