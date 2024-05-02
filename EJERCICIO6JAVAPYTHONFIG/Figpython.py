import math

class HexagonoRegular:
    def __init__(self, lado, color):
        self.__lado = lado
        self.__color = color

    def get_area(self):
        return self.__area()

    def get_perimetro(self):
        return self.__perimetro()

    def get_color(self):
        return self.__color

    def __area(self):
        return (3 * math.sqrt(3) * self.__lado ** 2) / 2

    def __perimetro(self):
        return 6 * self.__lado


class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, color):
        self.__diagonal_mayor = diagonal_mayor
        self.__diagonal_menor = diagonal_menor
        self.__color = color

    def get_area(self):
        return self.__area()

    def get_perimetro(self):
        return self.__perimetro()

    def get_color(self):
        return self.__color

    def __area(self):
        return (self.__diagonal_mayor * self.__diagonal_menor) / 2

    def __perimetro(self):
        return 4 * math.sqrt((self.__diagonal_mayor / 2) ** 2 + (self.__diagonal_menor / 2) ** 2)


class Trapecio:
    def __init__(self, base_mayor, base_menor, lado1, lado2, altura, color):
        self.__base_mayor = base_mayor
        self.__base_menor = base_menor
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__altura = altura
        self.__color = color

    def get_area(self):
        return self.__area()

    def get_perimetro(self):
        return self.__perimetro()

    def get_color(self):
        return self.__color

    def __area(self):
        return ((self.__base_mayor + self.__base_menor) * self.__altura) / 2

    def __perimetro(self):
        return self.__base_mayor + self.__base_menor + self.__lado1 + self.__lado2


if __name__ == "__main__":
    hexagono = HexagonoRegular(5, "azul")
    print("Área del hexágono regular:", hexagono.get_area())
    print("Perímetro del hexágono regular:", hexagono.get_perimetro())
    print("Color del hexágono regular:", hexagono.get_color())

    rombo = Rombo(8, 6, "verde")
    print("Área del rombo:", rombo.get_area())
    print("Perímetro del rombo:", rombo.get_perimetro())
    print("Color del rombo:", rombo.get_color())

    trapecio = Trapecio(10, 6, 4, 8, 5, "rojo")
    print("Área del trapecio:", trapecio.get_area())
    print("Perímetro del trapecio:", trapecio.get_perimetro())
    print("Color del trapecio:", trapecio.get_color())
