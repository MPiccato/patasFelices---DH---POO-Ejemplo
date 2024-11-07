# Funciones para la interfaz de consola

from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Gato, Perro
from clases.producto import Producto
from clases.ventas import Venta


def registrar_mascota():
    tipo = input('Ingrese tipo de mascota (perro/gato): ').strip().lower()
    nombre = input('Nombre de la mascota: ').strip().lower()
    edad = int(input('Ingrese su edad: '))
    salud = input('Estado de salud de la mascota: ')
    precio = float(input('Precio de la mascota: '))

    if tipo == 'perro':
        raza = input('Ingrese la raza del perro: ')
        nivel_de_energia = input('Nivel de energía del perro: ')
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)

    elif tipo == 'gato':
        raza = input('Ingrese la raza del perro: ')
        independencia = input('Nivel de independencia: ')
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print('No se reconoce el tipo de mascota')
        return 
    return mascota

def registrar_cliente():
    nombre = input('Nombre del cliente: ')
    direccion = input('Dirección del cliente: ')
    telefono = input('Teléfono del cliente: ')
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre = input('Nombre del producto: ')
    categoria = input('Categoria del producto:')
    precio = input('Precio del producto:')
    cantidad = int(input('Cantidad de productos:'))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

def registrar_venta(clientes, inventario):
    nombre_cliente = input('Nombre del cliente: ')
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)

    if not cliente:
        print('Cliente no encontrado')

        return
    
    productos = []

    while True:
        nombre_producto = input('Ingrese nombre del producto o apriete enter para terminar: ')
        if not nombre_producto:
            break

        producto = next((p for p in inventario.lista_productos if p.nombre == nombre_producto))
        if producto:
            productos.append(producto)
        else:
            print('Producto no encontrado')
            
    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print('La venta se registra correctamente')
    else:
        print('No se ha registrado producto para la venta')
    
def mostrar_menu():
    print('\n ---- Menú de Gestión de Patas Felices ----')
    print('1. Registrar Mascota')
    print('2. Registrar Cliente')
    print('3. Registrar Producto')
    print('4. Registrar Venta')
    print('5. Mostrar inforamción acerca de Mascotas')
    print('6. Mostrar inforamción acerca de Clientes')
    print('7. Mostrar inforamción acerca de Productos')
    print('8. Generar alerta de inventario')
    print('9. Salir')


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        op = int(input('Elija la opción requerida: '))

        if op == 1:
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print('Mascota registrada con éxito')
        
        elif op == 2:
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print('Cliente registrado con éxito')
        
        elif op == 3:
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print('Producto agregado al inventario')

        elif op == 4:
            registrar_venta(cliente, inventario)
        
        elif op == 5:
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.caracteristicas())
        elif op == 6:
            for cliente in clientes:
                print(cliente.mostrar_informacion())
        elif op == 7:
            for producto in inventario.lista_productos:
                print(producto.mostrar_informacion())
        elif op == 8:
            umbral_minimo = int(input('Ingrese el umbral mínimo del inventario'))
            print(inventario.generar_alerta(umbral_minimo))
        elif op == 9:
            print('Hasta luego')
            break
        else:
            print('Opción inválida, intente nuevamente')


if __name__ == '__main__':
    main()

                    