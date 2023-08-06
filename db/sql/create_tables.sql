CREATE TABLE users_with_hash_index (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL ,  
    INDEX IX_date_of_birth_hash (date_of_birth)  USING HASH
) ENGINE=InnoDB;

CREATE TABLE users_with_btree_index (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL ,  
    INDEX IX_date_of_birth_btree (date_of_birth)  USING BTREE
) ENGINE=InnoDB;