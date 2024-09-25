def main():
    # Solicita al usuario que ingrese un texto largo
    print("\nBIENVENIDO AL SIMULADOR DE SISTEMAS DE ARCHIVOS FAT😎\n")
    texto = input("Ingrese el texto a almacenar🗂️: ")
    print("\n")

    # Define el tamaño máximo de caracteres por clúster
    tamano_cluster = 15

    # Divide el texto en partes de 15 caracteres
    clusters = [texto[i:i + tamano_cluster] for i in range(0, len(texto), tamano_cluster)]

    # Muestra el contenido de cada clúster
    for i, cluster in enumerate(clusters):
        print(f"Clúster {i + 1}: \"{cluster}\"")

    # Calcula y muestra el número de clústeres completos y parciales
    clusters_completos = len([c for c in clusters if len(c) == tamano_cluster])
    clusters_parciales = len(clusters) - clusters_completos
    tamano_total = len(texto)

    print(f"\n✅ Se utilizaron {clusters_completos} clústeres completos y {clusters_parciales} clúster parcial(es), \n✅ El tamaño total del archivo es de {tamano_total} caracteres. \n")

    print("\nGracias por utilizar la aplicacion en consola de ESTHER SOLOJ...💻\n")

if __name__ == "__main__":
    main()
