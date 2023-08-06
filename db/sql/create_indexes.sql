CREATE INDEX ix_users_name_btree ON users (name)  USING BTREE; -- duration 2 min 25 sec
CREATE INDEX ix_users_name_HASH ON users (name)  USING HASH;

--to show DDL of table
SHOW CREATE TABLE users;