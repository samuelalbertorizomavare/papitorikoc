import os
import requests
import subprocess

# Configuración
MINECRAFT_VERSION = "1.20.1"  # Cambia esto a la versión de Minecraft que desees
MEMORY = "8G"                # Memoria asignada al servidor
SERVER_DIR = os.path.expanduser("~/minecraft-server")
PAPER_API = f"https://api.papermc.io/v2/projects/paper/versions/{MINECRAFT_VERSION}"

# Crear el directorio del servidor
os.makedirs(SERVER_DIR, exist_ok=True)
os.chdir(SERVER_DIR)

# Descargar la última versión de PaperMC
def download_papermc():
    response = requests.get(PAPER_API)
    if response.status_code == 200:
        data = response.json()
        latest_build = data['builds'][-1]
        download_url = f"{PAPER_API}/builds/{latest_build}/downloads/paper-{MINECRAFT_VERSION}-{latest_build}.jar"
        print(f"Descargando PaperMC Build {latest_build} para Minecraft {MINECRAFT_VERSION}...")
        jar_path = os.path.join(SERVER_DIR, "paper.jar")
        with requests.get(download_url, stream=True) as r:
            with open(jar_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Descarga completada.")
    else:
        print("Error al obtener la información de PaperMC.")
        exit(1)

# Aceptar el EULA automáticamente
def accept_eula():
    with open("eula.txt", "w") as f:
        f.write("eula=true\n")
    print("EULA aceptado.")

# Crear un archivo de inicio para el servidor
def create_start_script():
    start_script = f"""#!/bin/bash
java -Xms{MEMORY} -Xmx{MEMORY} -jar paper.jar --nogui
"""
    with open("start.sh", "w") as f:
        f.write(start_script)
    os.chmod("start.sh", 0o755)
    print("Archivo de inicio creado.")

# Ejecutar el servidor por primera vez
def start_server():
    print("Iniciando el servidor por primera vez...")
    subprocess.run(["bash", "start.sh"], check=True)

if __name__ == "__main__":
    print("Configurando el servidor de Minecraft...")
    download_papermc()
    accept_eula()
    create_start_script()
    start_server()
