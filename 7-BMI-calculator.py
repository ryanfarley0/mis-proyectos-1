def finding_BMI (altura,peso):
    BMI= peso/altura**2
    return BMI
def general ():
    while True:
        try:
            altura= float(input("Ingrese si altura en metros: "))
            peso=float(input("Ingrese su peso en Kg: "))
            finding_BMI(altura,peso)
            BMI=finding_BMI(altura,peso)
            if BMI < 18.5 :
                print(f"Su masa corporal es baja")
            elif 18.5<=BMI<24.9:
                print("Su masa corporal es promedio")
            elif 25<=BMI<30:
                print("Su masa corporal es alta")
            else:
                print("Su masa corporal es muy alta")
            break
        except ValueError:
            print("ingrese valores validos")

general()

print ("Hello world")

