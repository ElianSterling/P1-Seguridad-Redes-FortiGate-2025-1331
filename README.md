# P1 - Seguridad de Redes con FortiGate

**Matrícula:** 2025-1331

## 🎥 Video demostrativo

> El enlace del video será agregado aquí antes de la entrega final.

## Propósito del laboratorio

Implementar una arquitectura de red segmentada y protegida mediante FortiGate, aplicando controles de acceso, inspección profunda de tráfico, prevención de intrusiones, protección contra SQL Injection, filtrado de archivos, rate limiting y políticas de comunicación entre usuarios, servidor web y servidor de base de datos.

## Topología

El laboratorio estará compuesto por:

- 1 FortiGate.
- 1 switch Cisco.
- 1 cliente de usuarios.
- 1 servidor web HTTPS.
- 1 servidor de base de datos.
- VLAN independientes para Users, Web, Database y Management.

## Direccionamiento

Bloque principal basado en la matrícula 2025-1331:

`10.25.13.0/24`

| VLAN | Nombre | Red | Gateway |
|---|---|---|---|
| 10 | USERS | 10.25.13.0/25 | 10.25.13.1 |
| 20 | WEB | 10.25.13.128/28 | 10.25.13.129 |
| 30 | DB | 10.25.13.144/28 | 10.25.13.145 |
| 99 | MGMT | 10.25.13.160/28 | 10.25.13.161 |

## Documentación

La documentación detallada se encuentra en el directorio `docs/`.

## Evidencias

Las capturas de pantalla y pruebas se encuentran en `images/`.

## Configuraciones

Los running-configs y respaldos se encuentran en `configs/`.

## Scripts

Todos los scripts utilizados durante el laboratorio se encuentran en `scripts/`.
