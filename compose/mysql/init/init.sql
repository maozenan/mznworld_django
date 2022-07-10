Alter user 'dbuser'@'%' IDENTIFIED WITH mysql_native_password BY 'mzn19961023';
GRANT ALL PRIVILEGES ON *.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;