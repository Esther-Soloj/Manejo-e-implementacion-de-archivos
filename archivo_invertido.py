# ejercicio clase 20/9/2024 - archivo invertido 

# MARIA ESTHER TIGüILÁ SOLOJ

# Función para leer un documento y devolver una lista de palabras
def leer_documento(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return archivo.read().split()

# Crear archivos de prueba si no existen
try:
    documento1 = leer_documento("documento1.txt")
except FileNotFoundError:
    with open("documento1.txt", "w") as archivo:
        archivo.write("manzana banana cereza durazno")
    documento1 = leer_documento("documento1.txt")

try:
    documento2 = leer_documento("documento2.txt")
except FileNotFoundError:
    with open("documento2.txt", "w") as archivo:
        archivo.write("banana cereza kiwi limón")
    documento2 = leer_documento("documento2.txt")

# Pedir al usuario que ingrese una palabra para buscar
palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")

# Buscar la palabra en los documentos
coincidencias_documento1 = [palabra for palabra in documento1 if palabra == palabra_a_buscar]
coincidencias_documento2 = [palabra for palabra in documento2 if palabra == palabra_a_buscar]

# Crear un archivo con las coincidencias encontradas en los documentos
with open("coincidencias_palabra.txt", "w") as archivo:
    archivo.write(f"Coincidencias de la palabra '{palabra_a_buscar}'\n")
    archivo.write("===========================================\n")
    archivo.write(f"En documento1.txt: {len(coincidencias_documento1)} coincidencias\n")
    archivo.write(f"En documento2.txt: {len(coincidencias_documento2)} coincidencias\n")

print(f"Coincidencias encontradas y guardadas en 'coincidencias_palabra.txt'")
