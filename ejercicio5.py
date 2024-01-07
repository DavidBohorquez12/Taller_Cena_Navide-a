# Módulo para el registro de sismos
class RegistroSismos:
    def __init__(self):
        self.ciudades = []

    def registrar_ciudad(self, nombre_ciudad, cantidad_sismos):
        ciudad = {"Nombre": nombre_ciudad, "Sismos": []}
        for _ in range(cantidad_sismos):
            magnitud_sismo = float(input(f"Ingrese la magnitud del sismo en {nombre_ciudad}: "))
            ciudad["Sismos"].append(magnitud_sismo)
        self.ciudades.append(ciudad)
        print(f"Ciudad {nombre_ciudad} registrada correctamente con {cantidad_sismos} sismos.")

    def buscar_sismos_por_ciudad(self, nombre_ciudad):
        for ciudad in self.ciudades:
            if ciudad["Nombre"] == nombre_ciudad:
                print(f"Sismos registrados en {nombre_ciudad}: {ciudad['Sismos']}")
                return
        print("Ciudad no encontrada.")

    def informe_riesgo(self):
        for ciudad in self.ciudades:
            promedio = sum(ciudad["Sismos"]) / len(ciudad["Sismos"])
            if promedio < 2.5:
                print(f"Ciudad {ciudad['Nombre']}: Amarillo (Sin riesgo)")
            elif 2.6 <= promedio <= 4.5:
                print(f"Ciudad {ciudad['Nombre']}: Naranja (Riesgo medio)")
            else:
                print(f"Ciudad {ciudad['Nombre']}: Rojo (Riesgo alto)")

# Módulo principal para la interacción con el usuario
def main():
    registro_sismos = RegistroSismos()

    while True:
        print("\n*** Menú ***")
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar Sismos por Ciudad")
        print("4. Informe de Riesgo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            cantidad_sismos = int(input("Ingrese la cantidad de sismos a registrar por ciudad: "))
            registro_sismos.registrar_ciudad(nombre_ciudad, cantidad_sismos)
        elif opcion == "2":
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            registro_sismos.buscar_sismos_por_ciudad(nombre_ciudad)
        elif opcion == "3":
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            registro_sismos.buscar_sismos_por_ciudad(nombre_ciudad)
        elif opcion == "4":
            registro_sismos.informe_riesgo()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
