-- Usuario utilizado por WEB01 para acceder a DB01
-- La contraseña real se configura localmente y NO se almacena en GitHub.

CREATE USER 'webapp'@'10.25.13.130'
IDENTIFIED BY '<PASSWORD_CONFIGURED_LOCALLY>';

GRANT SELECT, INSERT, UPDATE, DELETE
ON p1_lab.*
TO 'webapp'@'10.25.13.130';

FLUSH PRIVILEGES;
