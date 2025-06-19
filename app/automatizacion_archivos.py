import os
from datetime import datetime

def crear_reporte():
    carpeta = "reportes"
    os.makedirs(carpeta, exist_ok=True)

    fecha = datetime.now().strftime("%Y%m%d")
    archivo_reporte = os.path.join(carpeta, f"reporte_{fecha}.txt")
    archivos_txt = [f for f in os.listdir(carpeta) if f.endswith('.txt')]
    with open(archivo_reporte, "w") as f:
        if not archivos_txt:
            f.write("No se encontraron archivos de texto")
        else:
            for archivo in archivos_txt:
                if "reporte"  not in archivo:
                    ruta='reportes/'+archivo
                    with open(ruta, 'r') as a:
                        lineas = a.readlines()
                    f.write(f"{archivo} - {len(lineas)} lineas \n")
            f.write(f"\n  Total de archivos procesados: {len(archivos_txt)}\n")

if __name__ == "__main__":
    crear_reporte()
