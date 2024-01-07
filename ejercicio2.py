print("Bienvenido al centro de salud de campuslands")
print("Ingrese los siguientes datos")
nombre = str(input("Ingrese su nombre : "))
edad = int(input("Ingrese su edad : "))
peso = int(input("Peso actual (kg) : "))

altura = float(input("Altura actual (m2): "))
altura = int(altura*altura)

imc = int(peso / altura)
print("Su IMC es de : ",imc)
def categoria_imc(imc):
    if imc < 18.5:
        return("Bajo peso")
    elif 18.5 <= imc < 24.9:
        return("Peso normal")
    elif 25 <= imc < 29.9:
        return("Sobrepeso")
    elif 30 <= imc < 34.9:
        return("Obesidad I")
    elif 35 <= imc < 39.9:
        return("Obesidad II")
    else:
        return("Obesidad III")

    
categoria_imc=categoria_imc(imc)

print(f"Su categoria IMC es : {categoria_imc}")
