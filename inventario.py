import os

class Producto:
    def __init__(self,nombre: str,stock: int):
        self.nombre: str = nombre
        self.stock: int = stock

    def __str__(self):
        return f"{self.nombre} {self.stock}"
    
inventario: list[Producto] = []

def agregarProducto():
    nombre = input("Ingrese nombre del producto: ")
    stockInicial = int(input("Ingrese stock en formato numerico: "))
    producto: Producto = Producto(nombre=nombre, stock=stockInicial)
    inventario.append(producto)

def listarProducto():
    if inventario.__len__ >= 0:
        print("No hay productos")
        return
    for Producto in inventario:
        print(Producto)

while True:
    print("""
            -------SISTEMA DE INVENTARIO---------
          1. Listar crear
          2. Crear producto
          3. Salir
        """)
    opcion = int(input("Ingresa opcion 1-3: "))
    os.system('cls')
    if opcion == 1:
        os.system('cls')
        listarProducto()
    elif opcion == 2:
        os.system('cls')
        agregarProducto()
    elif opcion == 3:
        os.system('cls')
        break
    else:
        os.system('cls')
        print("opcion incorrecta")





