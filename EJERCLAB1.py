import random
import time

ARRAY_SIZE = 1000

# Funcion para generar un arreglo de numeros enteros aleatorios
def ga(size):
    return [random.randint(0, 999) for _ in range(size)]

# Funcion para imprimir el contenido de un arreglo
def ia(arreglo):
    print(" ".join(map(str, arreglo)))
    
# Funcion de busqueda secuencial
def bs(arreglo, ele):
    for i, num in enumerate(arreglo):
        if num == ele:
            return i
    return -1

# Funcion de ordenamiento: Metodo Burbuja
def oa(arreglo):
    return sorted(arreglo)

# Comienza main
if __name__ == "__main__":
    # Paso 1: Generar arreglo de numeros aleatorios
    inicio = time.time()
    arreglo = ga(ARRAY_SIZE)

    
    # Paso 2: Imprimir el arreglo generado
    print("Arreglo generado:")
    ia(arreglo)
    
    # Paso 3: Solicitar al usuario el numero a buscar
    elebus = int(input("\nIngrese el numero que desea buscar: "))
    
    # Paso 4: Busqueda secuencial del elemento ingresado por el usuario
    inicio = time.time()
    indenc = bs(arreglo, elebus)
    fin = time.time()
    tiempo = fin - inicio
    if indenc != -1:
        print(f"\nEl elemento {elebus} se encuentra en el indice {indenc}\n")
    else:
        print(f"\nEl elemento {elebus} no se encuentra en el arreglo\n")
    
    # Paso 5: Ordenar el arreglo
    inicio = time.time()
    ao = oa(arreglo)
    fin = time.time()
    tiempo = fin - inicio
    print("Arreglo ordenado:")
    ia(ao)
    
    # Paso 6: Buscar en el arreglo ordenado
    print("\nARREGLO ORDENADO")
    indenc = bs(ao, elebus)
    if indenc != -1:
        print(f"El elemento {elebus} se encuentra en el indice {indenc}\n")
    else:
        print(f"El elemento {elebus} no se encuentra en el arreglo\n")
        fin = time.time()
    print(f"Tiempo de generacion del arreglo: {tiempo} segundos")
