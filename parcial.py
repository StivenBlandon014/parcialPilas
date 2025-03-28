class Dispositivo:
    def __init__(self, serial, marca, precio, nombre_usuario, disponibilidad):
        self.serial = serial
        self.marca = marca
        self.precio = precio
        self.nombre_usuario = nombre_usuario
        self.disponibilidad = disponibilidad

class PC(Dispositivo):
    def __init__(self, serial, marca, ram, disco_duro, precio, usuario, disponibilidad):
        super().__init__(serial, marca, precio, usuario, disponibilidad)
        self.ram = ram
        self.disco_duro = disco_duro

class Tablet(Dispositivo):
    def __init__(self, serial, tamaño, marca, precio, usuario, disponibilidad):
        super().__init__(serial, marca, precio, usuario, disponibilidad)
        self.tamaño = tamaño


inventario = []

def agregar_dispositivo_por_usuario():
    tipo = input("¿Qué tipo de dispositivo desea agregar (PC/Tablet)? ").strip().lower()
    serial = input("Serial: ").strip()
    marca = input("Marca: ").strip()
    precio = float(input("Precio: "))
    usuario = input("Nombre de usuario: ").strip()
    disponibilidad = input("¿Está disponible? (sí/no): ").strip().lower() == "sí"


    if tipo == "pc":
        ram = input("Memoria RAM: ").strip()
        disco_duro = input("Disco duro: ").strip()
        dispositivo = PC(serial, marca, ram, disco_duro, precio, usuario, disponibilidad)
    elif tipo == "tablet":
        tamaño = input("Tamaño: ").strip()
        dispositivo = Tablet(serial, tamaño, marca, precio, usuario, disponibilidad)
    else:
        print("Tipo de dispositivo no válido.")
        return inventario.append(dispositivo)
    print(f"Dispositivo {serial} agregado al inventario.")

def modificar_dispositivo_por_usuario():
    serial = input("Ingrese el serial del dispositivo que desea modificar: ").strip()
    for dispositivo in inventario:
        if dispositivo.serial == serial:
            atributo = input("¿Qué atributo desea modificar? ").strip().lower()
            nuevo_valor = input("Ingrese el nuevo valor: ").strip()
            if atributo == "precio":
                nuevo_valor = float(nuevo_valor)
            elif atributo == "disponibilidad":
                nuevo_valor = nuevo_valor.lower() == "sí"

            setattr(dispositivo, atributo, nuevo_valor)
            print(f"Dispositivo {serial} modificado con éxito.")
            return
    print("Dispositivo no encontrado.")

def mostrar_inventario():
    for dispositivo in inventario:
        print(vars(dispositivo))

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar dispositivo")
        print("2. Modificar dispositivo")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_dispositivo_por_usuario()
        elif opcion == "2":
            modificar_dispositivo_por_usuario()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Hasta luego")
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()


    

