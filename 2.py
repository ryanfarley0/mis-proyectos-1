import secrets
import string
while True:
    try:
        longitud_deseada= int(input("Ingrese la longitud deseada (12 por defecto)") or 12)
        caracteres= string.ascii_letters + string.digits #+ string.punctuation
        contraseña_generada= "".join(secrets.choice(caracteres) for _ in range(longitud_deseada))
        print(f"Contraseña generada:{contraseña_generada} ")
        break
    except ValueError:
        print("Por favor, ingrese valores numéricos")