CREATE DATABASE IF NOT EXISTS stockTickers;
GRANT ALL PRIVILEGES ON stockTickers.users to 'user'@'localhost' 
identified by 'password';
USE stockTickers;

/* Set up initial user table structure */

CREATE TABLE users
(
  user_id NOT NULL AUTOINCREMENT,
  username VARCHAR(256),
  password VARCHAR(256),
  PRIMARY KEY (username)
);
