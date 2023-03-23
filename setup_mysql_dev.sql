-- Setup development
CREATE DATABASE IF NOT EXISTS hbnb_dev_bd;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_bd.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
