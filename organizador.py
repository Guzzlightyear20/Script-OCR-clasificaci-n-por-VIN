import os
import shutil
import cv2
from pyzbar.pyzbar import decode
from datetime import datetime # <--- NUEVO: Importamos la herramienta para la fecha

def organizar_fotos_por_vin(carpeta_origen):
    archivos = sorted([f for f in os.listdir(carpeta_origen) if f.lower().endswith(('.jpg', '.jpeg'))])
    
    lote_temporal = []
    vins_procesados = [] 
    
    print(f"Procesando {len(archivos)} fotos...")

    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_origen, archivo)
        lote_temporal.append(ruta_completa)
        
        imagen = cv2.imread(ruta_completa)
        
        if imagen is None:
            continue
            
        codigos = decode(imagen)
        
        if codigos:
            vin = codigos[0].data.decode('utf-8')
            vin = "".join(c for c in vin if c.isalnum()) 
            vin = vin[-8:] 
            
            print(f"\n¡VIN detectado!: {vin} en la foto {archivo}")
            
            carpeta_destino = os.path.join(carpeta_origen, vin)
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            for foto_lote in lote_temporal:
                nombre_archivo = os.path.basename(foto_lote)
                shutil.move(foto_lote, os.path.join(carpeta_destino, nombre_archivo))
            
            print(f"-> Se movieron {len(lote_temporal)} fotos a la carpeta '{vin}'.")
            
            vins_procesados.append(vin)
            lote_temporal = []

    if lote_temporal:
        print(f"\nOjo: Quedaron {len(lote_temporal)} fotos sueltas al final sin un VIN asignado.")

    # ---------------------------------------------------------
    # 6. CREAR EL REPORTE TXT CON FECHA
    # ---------------------------------------------------------
    if vins_procesados:
        # <--- NUEVO: Obtenemos la fecha de hoy (Día-Mes-Año)
        fecha_hoy = datetime.now().strftime("%d-%m-%Y")
        
        # Le ponemos la fecha al nombre del archivo
        nombre_reporte = f"Reporte_Stock_{fecha_hoy}.txt"
        ruta_reporte = os.path.join(carpeta_origen, nombre_reporte)
        
        with open(ruta_reporte, "w") as archivo_txt:
            archivo_txt.write(f"REPORTE DE STOCK - FECHA: {fecha_hoy}\n")
            archivo_txt.write("-" * 35 + "\n")
            archivo_txt.write("VIN (8 Digitos)\n")
            archivo_txt.write("-" * 35 + "\n")
            
            for v in vins_procesados:
                archivo_txt.write(f"{v}\n")
                
        print(f"\n¡Éxito! Se creó el archivo '{nombre_reporte}' con {len(vins_procesados)} vehículos procesados.")

# --- CÓMO USARLO ---
ruta_de_tus_fotos = r"E:\CARROS\4-15-26 Camiones" 
organizar_fotos_por_vin(ruta_de_tus_fotos)