def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def determinar_categoria(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad I"
    elif 35 <= imc < 39.9:
        return "Obesidad II"
    else:
        return "Obesidad III"


peso_ideal_count = 0
obesidad_I_count = 0
obesidad_II_count = 0
obesidad_III_count = 0
sobrepeso_count = 0


for _ in range(20):
    print("\nIngrese los datos del estudiante:")
    nombre = str(input("Nombre: "))
    edad = int(input("Edad: "))
    peso = float(input("Peso actual (kg): "))
    altura = float(input("Altura actual (m): "))

    imc = calcular_imc(peso, altura)
    categoria_imc = determinar_categoria(imc)

    print(f"IMC de {nombre}: {imc:.2f} - Categoría: {categoria_imc}")


    if categoria_imc == "Peso normal":
        peso_ideal_count += 1
    elif categoria_imc == "Obesidad I":
        obesidad_I_count += 1
    elif categoria_imc == "Obesidad II":
        obesidad_II_count += 1
    elif categoria_imc == "Obesidad III":
        obesidad_III_count += 1
    elif categoria_imc == "Sobrepeso":
        sobrepeso_count += 1


print("\nInforme:")
print(f"a. Estudiantes en peso ideal: {peso_ideal_count}")
print(f"b. Estudiantes en obesidad grado I: {obesidad_I_count}")
print(f"c. Estudiantes en obesidad grado II: {obesidad_II_count}")
print(f"d. Estudiantes en obesidad grado III: {obesidad_III_count}")
print(f"e. Estudiantes en Sobrepeso: {sobrepeso_count}")
