DROP DATABASE IF EXISTS stockTickers;
CREATE DATABASE IF NOT EXISTS stockTickers;
GRANT ALL PRIVILEGES ON stockTickers.users to 'user'@'localhost' 
identified by 'password';
USE stockTickers;

/* Set up initial user table structure */

CREATE TABLE users
(
  user_id INT(11) NOT NULL AUTO_INCREMENT,
  username VARCHAR(35) CHARACTER SET utf8 NOT NULL default '',
  password VARCHAR(256) NOT NULL default '',
  PRIMARY KEY (user_id)
);


CREATE TABLE stocks
(
  stock_id INT(11) NOT NULL AUTO_INCREMENT,
  symbol VARCHAR(6),
  name VARCHAR(35),
  price DECIMAL(8, 2),
  PRIMARY KEY (stock_id)
);

CREATE TABLE owners
(
  user_id INT(11) REFERENCES users (user_id),
  stock_id INT(11) REFERENCES stocks (stock_id),
  amount INT(11) NOT NULL default 1,
  PRIMARY KEY (user_id, stock_id)
); 

/* A new user */

INSERT INTO users VALUES (1, 'duffbuster', SHA2('password', 0));

INSERT INTO stocks VALUES (1, 'GOOG', 'Google Inc', 1197.16);

INSERT INTO owners VALUES (1, 1, 2);

/* I don't want to have to create a new table every time I get a new user... */

/* stocks table and a linker table? */
