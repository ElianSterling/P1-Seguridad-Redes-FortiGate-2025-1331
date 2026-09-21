# 09 - Índice de evidencias

## FortiGate

| Archivo | Evidencia |
|---|---|
| `01-interfaces-vlans.png` | Interfaces y direccionamiento VLAN |
| `02-interfaces-vlans-dhcp.png` | VLANs y rango DHCP de USERS |
| `03-firewall-policies.png` | Políticas principales de firewall |
| `04-ips-quarantine.png` | Cuarentena IPS de 10.25.13.10 |
| `05-file-filter-exe-blocked.png` | Bloqueo de archivo .exe |
| `06-dos-syn-flood-protection.png` | Protección tcp_syn_flood |
| `07-ips-sqli-dropped-details.png` | SQL Injection detectado y dropped |
| `08-custom-deep-inspection.png` | Perfil Full SSL Inspection |
| `09-users-to-web-https-security-profiles.png` | Policy HTTPS con IPS + SSL Inspection |
| `10-per-ip-shaper-2048kbps.png` | Per-IP rate limiting a 2048 Kbps |
| `11-forward-traffic-web-to-db-mysql.png` | WEB01 → DB01 MySQL permitido |

Ruta: `images/fortigate/`

## Switch

`images/switch/01-switch-status-trunk.png`

Demuestra puertos de acceso, trunk 802.1Q y puertos no utilizados deshabilitados.

La salida textual de `show vlan brief` y `show interfaces trunk` se encuentra en:

`configs/switch/SW1-verification.txt`

## WEB01

`images/web/01-web01-https-db-data.png`

Demuestra que WEB01 funciona sobre HTTPS y obtiene datos desde DB01 mediante TCP/3306.

## Pruebas

`images/pruebas/01-segmentacion-user-web-db.png`

En una sola captura demuestra:

- USER01 → DB01:3306 = `False`.
- USER01 → WEB01:443 = `True`.

## Capturas descartadas

El directorio `images/descartadas/` conserva capturas intermedias o duplicadas y no debe utilizarse como evidencia principal.

## Nota sobre la WAN

Las capturas iniciales de interfaces muestran la WAN con `192.168.1.137`. Posteriormente el FortiGate obtuvo `192.168.1.184` mediante DHCP. Estas capturas se utilizan para documentar VLANs y direccionamiento interno, no como referencia del lease WAN final.

## Nota sobre DPI

El perfil `custom-deep-inspection` y su aplicación a `USERS_to_WEB_HTTPS` están documentados visualmente. La VM Evaluation utilizada limitó la demostración completa del descifrado e inspección HTTPS.
