
class TorneoTenisMesa:
    def __init__(self):
        self.categorias = {"Novato": [], "Intermedio": [], "Avanzado": []}

    def registrar_jugador(self, id_jugador, nombre, edad, categoria):
        jugador = {"Id": id_jugador, "Nombre": nombre, "Edad": edad, "Partidos Jugados": 0,
                   "Partidos Ganados": 0, "Partidos Perdidos": 0, "Puntos A Favor": 0, "Total Puntos": 0}
        
        if categoria in self.categorias and self.validar_edad(categoria, edad):
            self.categorias[categoria].append(jugador)
            print(f"Jugador {nombre} registrado en la categoría {categoria}.")

    def validar_edad(self, categoria, edad):
        if categoria == "Novato" and 15 <= edad <= 16:
            return True
        elif categoria == "Intermedio" and 17 <= edad <= 20:
            return True
        elif categoria == "Avanzado" and edad > 20:
            return True
        else:
            print("Edad no válida para la categoría.")
            return False

    def iniciar_torneo(self):
        for categoria, jugadores in self.categorias.items():
            if len(jugadores) >= 5:
                print(f"Iniciando torneo en la categoría {categoria}.")
                self.realizar_juegos(categoria)
            else:
                print(f"No hay suficientes inscritos en la categoría {categoria} para iniciar el torneo.")

    def realizar_juegos(self, categoria):
        for jugador in self.categorias[categoria]:
            print(f"\nPartidos de {jugador['Nombre']} en la categoría {categoria}:")
            partidos_ganados = int(input(f"Cantidad de partidos ganados por {jugador['Nombre']}: "))
            partidos_perdidos = int(input(f"Cantidad de partidos perdidos por {jugador['Nombre']}: "))
            jugador['Partidos Jugados'] += partidos_ganados + partidos_perdidos
            jugador['Partidos Ganados'] += partidos_ganados
            jugador['Partidos Perdidos'] += partidos_perdidos
            jugador['Puntos A Favor'] = (partidos_ganados * 2) + (partidos_perdidos * 0)
            jugador['Total Puntos'] = jugador['Puntos A Favor']

    def obtener_ganador_por_categoria(self):
        for categoria, jugadores in self.categorias.items():
            if jugadores:
                ganador = max(jugadores, key=lambda x: x['Puntos A Favor'])
                print(f"\nGanador de la categoría {categoria}: {ganador['Nombre']} con {ganador['Puntos A Favor']} puntos a favor.")



def main():
    torneo = TorneoTenisMesa()

    while True:
        print("\n*** Menú ***")
        print("1. Registrar Jugador")
        print("2. Iniciar Torneo")
        print("3. Obtener Ganador por Categoría")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_jugador = input("Ingrese el ID del jugador: ")
            nombre = input("Ingrese el nombre del jugador: ")
            edad = int(input("Ingrese la edad del jugador: "))
            categoria = input("Ingrese la categoría del jugador (Novato/Intermedio/Avanzado): ")
            torneo.registrar_jugador(id_jugador, nombre, edad, categoria)
        elif opcion == "2":
            torneo.iniciar_torneo()
        elif opcion == "3":
            torneo.obtener_ganador_por_categoria()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
