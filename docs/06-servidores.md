# 06 - Servidores y cliente

## WEB01

### Direccionamiento

```text
IP:      10.25.13.130/28
Gateway: 10.25.13.129
VLAN:    20
```

### Servicios

WEB01 utiliza:

- Debian 12.
- Nginx en TCP/443.
- Certificado TLS autofirmado para el laboratorio.
- Flask como aplicación.
- Gunicorn con 2 workers enlazado a `127.0.0.1:5000`.
- Variables de entorno en `/etc/p1-webapp.env`.

Nginx actúa como reverse proxy hacia Gunicorn.

Archivos publicados:

- [Configuración Nginx](../configs/web/nginx-https.conf)
- [Servicio systemd](../configs/web/p1-webapp.service)
- [Aplicación Flask](../scripts/web-server/app.py)

La clave privada TLS y el archivo `.env` no se almacenan en GitHub.

## Aplicación

La página principal consulta DB01 y presenta la tabla `productos`.

Se implementó también el endpoint:

```text
/buscar?id=<valor>
```

El endpoint contiene deliberadamente una consulta vulnerable para generar el tráfico SQLi autorizado del laboratorio. No debe utilizarse como patrón de desarrollo seguro en un entorno real.

## DB01

### Direccionamiento

```text
IP:      10.25.13.146/28
Gateway: 10.25.13.145
VLAN:    30
```

### MariaDB

DB01 ejecuta MariaDB 10.11.

El servicio fue ajustado para escuchar explícitamente en:

```text
10.25.13.146:3306
```

Configuración:

```text
bind-address = 10.25.13.146
```

Se deshabilitó `mariadb.socket` para evitar que systemd expusiera `*:3306` mediante socket activation. MariaDB quedó ejecutándose como servicio normal.

Archivo:

- [50-server.cnf](../configs/db/50-server.cnf)

### Base de datos

Base:

```text
p1_lab
```

Tabla:

```text
productos
```

El usuario de aplicación `webapp` se limita al origen `10.25.13.130` y dispone de permisos SELECT, INSERT, UPDATE y DELETE sobre `p1_lab.*`.

La contraseña real no está almacenada en el repositorio.

Archivos:

- [Dump de p1_lab](../scripts/db-server/p1_lab_dump.sql)
- [Ejemplo sanitizado de creación de usuario](../scripts/db-server/setup-user-example.sql)

## USER01

Cliente Windows en VLAN10-USERS.

```text
IP obtenida por DHCP: 10.25.13.10/25
Gateway: 10.25.13.1
```

Se utiliza para validar las políticas de acceso y ejecutar las pruebas de seguridad.

## Evidencia

![WEB01 consultando DB01](../images/web/01-web01-https-db-data.png)
