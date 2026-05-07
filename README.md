# 🚗 Organizador de Fotos por VIN (VIN Photo Organizer)

Este script en Python automatiza la organización de fotografías de vehículos mediante la detección de códigos de barras o QR. Es ideal para flujos de trabajo donde se capturan varias fotos de un mismo vehículo y se finaliza (o inicia) la sesión tomando una foto del número de identificación del vehículo (VIN).

Además de organizar los archivos, el script genera automáticamente un reporte de stock diario con los vehículos procesados.

## ✨ Características Principales

* **Agrupamiento Inteligente (Lotes):** Lee las fotos en orden alfabético y las acumula en un "lote temporal" hasta que detecta una foto con un código de barras.
* **Lectura de Código VIN:** Utiliza visión por computadora para decodificar el código, limpia los caracteres no alfanuméricos y extrae los **últimos 8 dígitos** del VIN para nombrar las carpetas.
* **Creación Automática de Directorios:** Crea una carpeta con los 8 dígitos del VIN y mueve allí todo el lote de fotos correspondiente a ese vehículo.
* **Reporte de Stock Automatizado:** Genera un archivo `.txt` (ej. `Reporte_Stock_DD-MM-YYYY.txt`) con un listado limpio de todos los VINs procesados en la sesión.

## ⚠️ Consideraciones
Fotos sueltas: Si al finalizar el escaneo quedan fotos en el lote temporal sin que el script haya detectado un código de barras de cierre, estas fotos no se moverán y el script notificará en la consola: "Ojo: Quedaron X fotos sueltas...".

Formato de imagen: Actualmente el script procesa archivos con extensión .jpg y .jpeg (sin distinguir mayúsculas de minúsculas).

## 🛠️ Requisitos Previos

Para ejecutar este script, necesitas tener instalado Python en tu sistema, junto con las siguientes librerías:

* `opencv-python` (cv2)
* `pyzbar`

Puedes instalarlas fácilmente usando pip:

```bash
pip install opencv-python pyzbar

```
<table style="width: 100%;">
  <tr>
    <td align="center"><img width="1690" height="829" alt="Captura de pantalla 2026-05-07 170128" src="https://github.com/user-attachments/assets/f130f420-bca7-43bc-b1d8-1321bd4d5467" width="100%"><br><b>Ejecutando el Script</b></td>
    <td align="center"><img width="1868" height="842" alt="Captura de pantalla 2026-05-07 170148" src="https://github.com/user-attachments/assets/0aeb2cb0-51de-4f5f-8536-a2f558fe5ed8" width="100%"><br><b>Script en Proceso</b></td>
  </tr>
  <tr>
    <td align="center"><img width="1704" height="892" alt="Captura de pantalla 2026-05-07 170205" src="https://github.com/user-attachments/assets/e420c911-eab9-483a-893d-a6e9c6a8524f"<img width="1402" height="914" alt="Captura de pantalla 2026-05-07 170223" src="https://github.com/user-attachments/assets/66f83880-dd89-42a2-969c-d2825d9b4dc4" />
 width="100%"><br><b>Finalizando</b></td>
    <td align="center"><img width="1402" height="914" alt="Captura de pantalla 2026-05-07 170223" src="https://github.com/user-attachments/assets/81867a6c-85df-4ea4-819e-47586fbb2a9e" width="100%"><br><b>Reporte de Vin</b></td>
  </tr>
</table>







