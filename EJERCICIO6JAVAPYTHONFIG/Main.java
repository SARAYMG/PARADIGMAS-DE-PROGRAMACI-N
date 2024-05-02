public class Main {
    public static void main(String[] args) {
        // Ejemplo de uso de las clases
        Circulo circulo = new Circulo(5.0, "rojo");
        System.out.println("Círculo:");
        System.out.println("Área: " + circulo.getArea());
        System.out.println("Perímetro: " + circulo.getPerimetro());
        System.out.println("Color: " + circulo.getColor());

        Rectangulo rectangulo = new Rectangulo(4.0, 3.0, "verde");
        System.out.println("\nRectángulo:");
        System.out.println("Área: " + rectangulo.getArea());
        System.out.println("Perímetro: " + rectangulo.getPerimetro());
        System.out.println("Color: " + rectangulo.getColor());

        Cuadrado cuadrado = new Cuadrado(5.0, "azul");
        System.out.println("\nCuadrado:");
        System.out.println("Área: " + cuadrado.getArea());
        System.out.println("Perímetro: " + cuadrado.getPerimetro());
        System.out.println("Color: " + cuadrado.getColor());

        Triangulo triangulo = new Triangulo(3.0, 4.0, 5.0, "amarillo");
        System.out.println("\nTriángulo:");
        System.out.println("Área: " + triangulo.getArea());
        System.out.println("Perímetro: " + triangulo.getPerimetro());
        System.out.println("Color: " + triangulo.getColor());
    }
}
