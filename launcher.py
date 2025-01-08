import os
import subprocess

# Ruta al directorio de OpenJDK
openjdk_path = r"C:\Users\Asesor\Downloads\CommonFiles\OpenJDKJRE\bin"

# Ruta al archivo .jar del cliente de Minecraft
minecraft_jar = r"C:\Users\Asesor\Downloads\mod\Install\versions\1.20.1.jar"

# Validación de rutas
if not os.path.exists(openjdk_path):
    print(f"Error: No se encontró el directorio de OpenJDK en '{openjdk_path}'")
    exit(1)

if not os.path.exists(minecraft_jar):
    print(f"Error: No se encontró el archivo .jar de Minecraft en '{minecraft_jar}'")
    exit(1)

# Ejecutar Minecraft
def launch_minecraft():
    java_exe = os.path.join(openjdk_path, "javaw.exe")
    if not os.path.exists(java_exe):
        print(f"Error: No se encontró 'javaw.exe' en '{java_exe}'")
        exit(1)

    # Comando para ejecutar Minecraft
    command = [java_exe, "-Xmx2G", "-Xms1G", "-jar", minecraft_jar]
    print("Ejecutando Minecraft...")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Minecraft: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    launch_minecraft()
