# Evidencias organizadas — P1 Seguridad de Redes

Paquete organizado para `P1-Seguridad-Redes-FortiGate-2025-1331`.

## Capturas principales

### FortiGate
- `01-interfaces-vlans.png`
  - Interfaces VLAN del laboratorio.
- `02-interfaces-vlans-dhcp.png`
  - VLANs y DHCP de USERS.
- `03-firewall-policies.png`
  - Políticas principales de firewall.
- `04-ips-quarantine.png`
  - Cuarentena de `10.25.13.10` por IPS.
- `05-file-filter-exe-blocked.png`
  - Bloqueo de `P1-Test.exe` mediante `P1_BLOCK_EXE`.
- `06-dos-syn-flood-protection.png`
  - DoS Policy `P1_WEB_DOS_PROTECTION`, `tcp_syn_flood`, `Block`, threshold `100`.
- `07-ips-sqli-dropped-details.png`
  - Evidencia detallada del evento `P1.SQL.Injection.Test`.
  - Source `10.25.13.10`, destination `10.25.13.130`, HTTP/80, action `dropped`.
  - Incluye el payload `id=1 OR 1=1`, perfil `P1_SQLI_PROTECTION` y severidad High.
- `08-custom-deep-inspection.png`
  - Perfil `custom-deep-inspection` con Full SSL Inspection y CA `Fortinet_CA_SSL`.
  - HTTPS/443 habilitado para inspección.
- `09-users-to-web-https-security-profiles.png`
  - Policy `USERS_to_WEB_HTTPS` con IPS `P1_SQLI_PROTECTION`
    y SSL Inspection `custom-deep-inspection`.

### Switch
- `images/switch/01-switch-status-trunk.png`
  - Puertos de acceso, puertos no usados deshabilitados y trunk 802.1Q
    con VLAN 10,20,30,99.

### WEB01
- `images/web/01-web01-https-db-data.png`
  - Aplicación HTTPS de WEB01 consumiendo datos desde DB01 por TCP/3306.

## Capturas descartadas
- `images/descartadas/01-interfaces-incompleta.png`
  - Captura intermedia; no muestra todas las VLANs.
- `images/descartadas/02-firewall-policies-duplicada.png`
  - Duplicada de la captura principal de políticas.

## Notas de documentación
- Las capturas del 17 de septiembre muestran la WAN con `192.168.1.137`.
  Más adelante el FortiGate recibió `192.168.1.184` por DHCP.
  Deben usarse como evidencia de VLANs/interfaces, no de la IP WAN final.
- `custom-deep-inspection` quedó configurado correctamente, pero la VM Evaluation
  limitó la demostración completa de DPI sobre HTTPS. Debe documentarse como
  limitación de licencia, no como ausencia de configuración.

## Evidencias que todavía conviene añadir
- Prueba desde USER01 de `WEB01:443` permitida y `DB01:3306` bloqueada.
- Traffic Shaping Policy `P1_USERS_TO_WEB_RATE_LIMIT` con `P1_WEB_RATE_LIMIT`.
- Estado final de MariaDB escuchando en `10.25.13.146:3306`.
- Si existe, una captura final de `show vlan brief` y `show interfaces trunk`.


## Nuevas evidencias añadidas (21 de septiembre)

- `images/fortigate/10-per-ip-shaper-2048kbps.png`
  - Evidencia del `Per IP Shaper` llamado `P1_WEB_RATE_LIMIT`.
  - Maximum bandwidth configurado en `2048 kbps`.
  - Sirve como evidencia directa del requisito de rate limiting.

- `images/fortigate/11-forward-traffic-web-to-db-mysql.png`
  - Evidencia de tráfico permitido desde `WEB01 (10.25.13.130)` hacia `DB01 (10.25.13.146)`.
  - La fila visible corresponde a la policy `WEB_to_DB_MYSQL`.
  - Útil para demostrar que WEB01 puede acceder a DB01 por MySQL.
  - No sustituye la evidencia de que `USER01 -> DB01:3306` está bloqueado; para eso conviene una captura separada de la prueba final o del log de deny.


## Evidencia final de segmentación

- `images/pruebas/01-segmentacion-user-web-db.png`
  - Desde `USER01 (10.25.13.10)`, `DB01 (10.25.13.146):3306` devuelve `TcpTestSucceeded : False`.
  - Desde el mismo origen, `WEB01 (10.25.13.130):443` devuelve `TcpTestSucceeded : True`.
  - Demuestra simultáneamente que el acceso directo de USERS a MariaDB está bloqueado y que HTTPS hacia WEB01 está permitido.
