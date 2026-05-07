# 🚗 Organizador de Fotos por VIN (VIN Photo Organizer)

Este script en Python automatiza la organización de fotografías de vehículos mediante la detección de códigos de barras o QR. Es ideal para flujos de trabajo donde se capturan varias fotos de un mismo vehículo y se finaliza (o inicia) la sesión tomando una foto del número de identificación del vehículo (VIN).

Además de organizar los archivos, el script genera automáticamente un reporte de stock diario con los vehículos procesados.

## ✨ Características Principales

* **Agrupamiento Inteligente (Lotes):** Lee las fotos en orden alfabético y las acumula en un "lote temporal" hasta que detecta una foto con un código de barras.
* **Lectura de Código VIN:** Utiliza visión por computadora para decodificar el código, limpia los caracteres no alfanuméricos y extrae los **últimos 8 dígitos** del VIN para nombrar las carpetas.
* **Creación Automática de Directorios:** Crea una carpeta con los 8 dígitos del VIN y mueve allí todo el lote de fotos correspondiente a ese vehículo.
* **Reporte de Stock Automatizado:** Genera un archivo `.txt` (ej. `Reporte_Stock_DD-MM-YYYY.txt`) con un listado limpio de todos los VINs procesados en la sesión.

## 🛠️ Requisitos Previos

Para ejecutar este script, necesitas tener instalado Python en tu sistema, junto con las siguientes librerías:

* `opencv-python` (cv2)
* `pyzbar`

Puedes instalarlas fácilmente usando pip:

```bash
pip install opencv-python pyzbar
