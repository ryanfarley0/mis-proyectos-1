def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def main():
    print("Conversor de Unidades:")
    print("1. Celsius a Fahrenheit")
    print("2. Kilómetros a Millas")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        resultado = celsius_to_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son {resultado:.2f} grados Fahrenheit.")
    elif opcion == '2':
        kilometers = float(input("Ingrese la distancia en kilómetros: "))
        resultado = kilometers_to_miles(kilometers)
        print(f"{kilometers} kilómetros son {resultado:.2f} millas.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()