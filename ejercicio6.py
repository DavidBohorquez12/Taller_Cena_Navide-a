class Dependencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.consumo_electricidad = 0
        self.kilometros_recorridos = 0

def registrar_dependencia(dependencias, nombre_dependencia):
    dependencia = Dependencia(nombre_dependencia)
    dependencias.append(dependencia)
    print(f"Dependencia {nombre_dependencia} registrada correctamente.")

def registrar_consumo(dependencias, nombre_dependencia):
    for dependencia in dependencias:
        if dependencia.nombre == nombre_dependencia:
            consumo_electricidad = float(input(f"Ingrese el consumo de electricidad en kWh para {nombre_dependencia}: "))
            dependencia.consumo_electricidad += consumo_electricidad

            kilometros_recorridos = float(input(f"Ingrese los kilómetros recorridos para {nombre_dependencia}: "))
            dependencia.kilometros_recorridos += kilometros_recorridos

            print("Consumo registrado correctamente.")
            return

    print("Dependencia no encontrada.")

def calcular_co2_producido(dependencias, factor_emision_electricidad, factor_emision_transporte):
    total_co2_producido = 0
    for dependencia in dependencias:
        co2_electricidad = dependencia.consumo_electricidad * factor_emision_electricidad
        co2_transporte = dependencia.kilometros_recorridos * factor_emision_transporte
        total_co2_producido += co2_electricidad + co2_transporte

    return total_co2_producido

def obtener_dependencia_mayor_co2(dependencias, factor_emision_electricidad, factor_emision_transporte):
    mayor_co2 = 0
    dependencia_mayor_co2 = None

    for dependencia in dependencias:
        co2_electricidad = dependencia.consumo_electricidad * factor_emision_electricidad
        co2_transporte = dependencia.kilometros_recorridos * factor_emision_transporte
        total_co2 = co2_electricidad + co2_transporte

        if total_co2 > mayor_co2:
            mayor_co2 = total_co2
            dependencia_mayor_co2 = dependencia.nombre

    return dependencia_mayor_co2

def main():
    dependencias = []
    factor_emision_electricidad = float(input("Ingrese el factor de emisión de electricidad en kg CO2/kWh: "))
    factor_emision_transporte = float(input("Ingrese el factor de emisión del transporte en kg CO2/km: "))

    while True:
        print("\n*** Menú Principal ***")
        print("1. Registrar Dependencia")
        print("2. Registrar Consumo por Dependencia")
        print("3. Ver CO2 Producido")
        print("4. Dependencia que Produce Mayor CO2")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
            registrar_dependencia(dependencias, nombre_dependencia)
        elif opcion == "2":
            nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
            registrar_consumo(dependencias, nombre_dependencia)
        elif opcion == "3":
            total_co2 = calcular_co2_producido(dependencias, factor_emision_electricidad, factor_emision_transporte)
            print(f"Total de CO2 producido en todas las dependencias: {total_co2} kg CO2")
        elif opcion == "4":
            dependencia_mayor_co2 = obtener_dependencia_mayor_co2(dependencias, factor_emision_electricidad, factor_emision_transporte)
            print(f"La dependencia que produce mayor CO2 es: {dependencia_mayor_co2}")
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
