# 01 - Propósito del laboratorio

## Objetivo general

Diseñar, implementar y validar una arquitectura de red segmentada utilizando FortiGate como dispositivo de seguridad perimetral y de control inter-VLAN. El laboratorio busca demostrar la aplicación práctica de controles de acceso, inspección, prevención de intrusiones y protección de servicios internos.

## Objetivos específicos

1. Separar usuarios, servidor web, base de datos y administración mediante VLAN independientes.
2. Proporcionar direccionamiento IP basado en el bloque `10.25.13.0/24`.
3. Permitir acceso de usuarios a WEB01 únicamente mediante HTTPS/443.
4. Impedir el acceso directo de usuarios al servicio MariaDB de DB01.
5. Permitir exclusivamente TCP/3306 desde WEB01 hacia DB01.
6. Configurar IPS para detectar y bloquear una prueba controlada de SQL Injection.
7. Configurar cuarentena temporal del origen detectado por IPS.
8. Bloquear descargas web de archivos `.exe`.
9. Aplicar rate limiting hacia WEB01.
10. Configurar protección ante SYN Flood.
11. Configurar un perfil de Deep SSL Inspection en FortiGate.
12. Documentar configuraciones, scripts, evidencias y resultados de pruebas.

## Alcance

La práctica se ejecuta en un entorno de laboratorio virtualizado y autorizado. La aplicación web incluye deliberadamente un endpoint vulnerable a SQL Injection con el único propósito de generar tráfico detectable por el IPS.

El laboratorio no expone credenciales reales ni material criptográfico privado en este repositorio.

## Criterios de seguridad utilizados

- **Segmentación:** cada tipo de activo se ubica en una VLAN distinta.
- **Mínimo privilegio de red:** solo se permiten los protocolos estrictamente necesarios.
- **Defensa en profundidad:** firewall, IPS, File Filter, Traffic Shaping y DoS Policy.
- **Registro y evidencia:** las políticas relevantes registran sesiones y eventos de seguridad.
- **Separación de secretos:** las contraseñas y claves privadas permanecen fuera de GitHub.

## Resultado

La arquitectura final permite el flujo legítimo USERS → WEB01 por HTTPS y WEB01 → DB01 por MySQL, mientras bloquea el acceso directo USERS → DB01. También se demostraron detección/bloqueo de SQL Injection, cuarentena, bloqueo de ejecutables, rate limiting y protección SYN Flood.
