# Definición de funciones para operaciones matemáticas

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: no se puede calcular la raíz cuadrada de un número negativo"

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def logaritmo(a, b):
    import math
    if a > 0 and b > 0 and b != 1:
        return math.log(a, b)
    else:
        return "Error: argumentos inválidos para logaritmo"

def menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Factorial")
    print("8. Logaritmo")
    print("9. Salir")

def main():
    while True:
        menu()
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == "9":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4", "5", "8"]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Por favor ingrese números válidos.")
                continue
        elif opcion in ["6", "7"]:
            try:
                num = float(input("Ingrese el número: "))
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
                continue

        if opcion == "1":
            print("El resultado de la suma es:", suma(num1, num2))
        elif opcion == "2":
            print("El resultado de la resta es:", resta(num1, num2))
        elif opcion == "3":
            print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
        elif opcion == "4":
            print("El resultado de la división es:", division(num1, num2))
        elif opcion == "5":
            print("El resultado de la potencia es:", potencia(num1, num2))
        elif opcion == "6":
            print("La raíz cuadrada es:", raiz_cuadrada(num))
        elif opcion == "7":
            print("El factorial es:", factorial(int(num)))
        elif opcion == "8":
            base = float(input("Ingrese la base del logaritmo: "))
            if base <= 0 or base == 1:
                print("Error: la base del logaritmo debe ser un número mayor que 0 y diferente de 1.")
                continue
            print("El resultado del logaritmo es:", logaritmo(num1, base))
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 9.")

if __name__ == "__main__":
    main()
