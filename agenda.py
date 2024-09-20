import json

# Nombre del archivo donde se guardarán los contactos
archivo_agenda = 'agenda.json'

# Función para cargar los contactos desde el archivo
def cargar_contactos():
    try:
        with open(archivo_agenda, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Función para guardar los contactos en el archivo
def guardar_contactos(contactos):
    with open(archivo_agenda, 'w') as archivo:
        json.dump(contactos, archivo, indent=4)

# Función para agregar un nuevo contacto
def agregar_contacto(nombre, telefono):
    contactos = cargar_contactos()
    contactos[nombre] = telefono
    guardar_contactos(contactos)
    print(f'Contacto {nombre} agregado.')

# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    contactos = cargar_contactos()
    if nombre in contactos:
        print(f'{nombre}: {contactos[nombre]}')
    else:
        print(f'Contacto {nombre} no encontrado.❌')

# Función para modificar el número de teléfono de un contacto
def modificar_contacto(nombre, nuevo_telefono):
    contactos = cargar_contactos()
    if nombre in contactos:
        contactos[nombre] = nuevo_telefono
        guardar_contactos(contactos)
        print(f'Número de {nombre} actualizado.')
    else:
        print(f'Contacto {nombre} no encontrado.')

# Función para eliminar un contacto
def eliminar_contacto(nombre):
    contactos = cargar_contactos()
    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
        print(f'Contacto {nombre} eliminado.')
    else:
        print(f'Contacto {nombre} no encontrado.')

# Función para listar todos los contactos
def listar_contactos():
    contactos = cargar_contactos()
    if contactos:
        for nombre, telefono in contactos.items():
            print(f'{nombre}: {telefono}')
    else:
        print('No hay contactos en la agenda.')

# menu de uso
if __name__ == '__main__':
    while True:
        print("\n BIENVENIDO AL GESTOR DE AGENDA TELEFONICA 📚 ")
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Modificar contacto")
        print("4. Eliminar contacto")
        print("5. Listar contactos")
        print("6. Salir")
        
        opcion = input("Selecciona una opción:✅ ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agregar_contacto(nombre, telefono)
        elif opcion == '2':
            nombre = input("Nombre: ")
            buscar_contacto(nombre)
        elif opcion == '3':
            nombre = input("Nombre: ")
            nuevo_telefono = input("Nuevo Teléfono: ")
            modificar_contacto(nombre, nuevo_telefono)
        elif opcion == '4':
            nombre = input("Nombre: ")
            eliminar_contacto(nombre)
        elif opcion == '5':
            listar_contactos()
        elif opcion == '6':
            break
        else:
            print("❌  Opción no válida, intenta de nuevo.")