import os
import hashlib
from collections import defaultdict
import send2trash  # Este módulo se utiliza para enviar archivos a la papelera, instálalo con "pip install Send2Trash"

def buscar_duplicados(directorio):
    hash_archivos = defaultdict(list)

    for carpeta_actual, _, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta_actual, archivo)

            # Calcula el hash MD5 del archivo
            with open(ruta_completa, 'rb') as f:
                hash_archivo = hashlib.md5(f.read()).hexdigest()

            # Agrega la ruta al diccionario de hash_archivos
            hash_archivos[hash_archivo].append(ruta_completa)

    return {hash_: rutas for hash_, rutas in hash_archivos.items() if len(rutas) > 1}

def eliminar_duplicados(duplicados):
    for rutas in duplicados.values():
        for ruta in rutas[1:]:
            print(f"Eliminando duplicado: {ruta}")
            send2trash.send2trash(ruta)

def main():
    directorio = input("Ingrese la ruta del directorio a escanear: ")

    if not os.path.exists(directorio):
        print("La ruta especificada no existe.")
        return

    duplicados = buscar_duplicados(directorio)

    if duplicados:
        print("\nArchivos duplicados encontrados:")
        for hash_, rutas in duplicados.items():
            print(f"Hash: {hash_}")
            for ruta in rutas:
                print(f"  - {ruta}")

        eliminar = input("\n¿Desea eliminar los archivos duplicados? (S/N): ").strip().lower()
        if eliminar == 's':
            eliminar_duplicados(duplicados)
            print("Archivos duplicados eliminados.")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontraron archivos duplicados en el directorio.")

if __name__ == "__main__":
    main()
