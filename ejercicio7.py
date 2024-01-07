class Producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor
        self.stock_actual = 0

def registrar_producto(productos):
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = float(input("Ingrese el valor de compra del producto: "))
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    stock_minimo = int(input("Ingrese el stock mínimo permitido: "))
    stock_maximo = int(input("Ingrese el stock máximo permitido: "))
    proveedor = input("Ingrese el nombre del proveedor del producto: ")

    nuevo_producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
    productos.append(nuevo_producto)
    print(f"Producto {nombre} registrado correctamente.")

def visualizar_productos(productos):
    print("\nLista de Productos:")
    for producto in productos:
        print(f"\nCódigo: {producto.codigo}")
        print(f"Nombre: {producto.nombre}")
        print(f"Valor de Compra: {producto.valor_compra}")
        print(f"Valor de Venta: {producto.valor_venta}")
        print(f"Stock Mínimo: {producto.stock_minimo}")
        print(f"Stock Máximo: {producto.stock_maximo}")
        print(f"Proveedor: {producto.proveedor}")
        print(f"Stock Actual: {producto.stock_actual}")

def actualizar_stock(productos):
    codigo = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a agregar o restar al stock (use valores negativos para restar): "))

    for producto in productos:
        if producto.codigo == codigo:
            producto.stock_actual += cantidad
            print(f"Stock actualizado correctamente para el producto {producto.nombre}. Nuevo stock: {producto.stock_actual}")
            return

    print("Producto no encontrado.")

def informe_productos_criticos(productos):
    print("\nProductos Críticos (Stock por debajo del límite mínimo):")
    for producto in productos:
        if producto.stock_actual < producto.stock_minimo:
            print(f"\nCódigo: {producto.codigo}")
            print(f"Nombre: {producto.nombre}")
            print(f"Stock Actual: {producto.stock_actual}")

def calcular_ganancia_potencial(productos):
    ganancia_potencial_total = 0
    for producto in productos:
        ganancia_potencial_total += (producto.valor_venta - producto.valor_compra) * producto.stock_actual
    return ganancia_potencial_total

def main():
    productos = []

    while True:
        print("\n*** Menú Principal ***")
        print("1. Registrar Producto")
        print("2. Visualizar Productos")
        print("3. Actualizar Stock")
        print("4. Informe de Productos Críticos")
        print("5. Cálculo de Ganancia Potencial")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            visualizar_productos(productos)
        elif opcion == "3":
            actualizar_stock(productos)
        elif opcion == "4":
            informe_productos_criticos(productos)
        elif opcion == "5":
            ganancia_potencial = calcular_ganancia_potencial(productos)
            print(f"\nGanancia Potencial Total: {ganancia_potencial}")
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
