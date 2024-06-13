// Definición de la interfaz Figure
interface Figure {
    String getColor();
    double perimeter();
    double area();
}

// Implementación de la clase Triangle
class Triangle implements Figure {
    private String color;
    private double a, b, c;

    public Triangle(String color, double a, double b, double c) {
        this.color = color;
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return a + b + c;
    }

    @Override
    public double area() {
        double s = perimeter() / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}

// Implementación de la clase Circle
class Circle implements Figure {
    private String color;
    private double radius;

    public Circle(String color, double radius) {
        this.color = color;
        this.radius = radius;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

// Implementación de la clase Rectangle
class Rectangle implements Figure {
    private String color;
    private double width, height;

    public Rectangle(String color, double width, double height) {
        this.color = color;
        this.width = width;
        this.height = height;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return 2 * (width + height);
    }

    @Override
    public double area() {
        return width * height;
    }
}

// Implementación de la clase Hexagon
class Hexagon implements Figure {
    private String color;
    private double side;

    public Hexagon(String color, double side) {
        this.color = color;
        this.side = side;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return 6 * side;
    }

    @Override
    public double area() {
        return (3 * Math.sqrt(3) * side * side) / 2;
    }
}

// Clase principal para demostrar el uso de la interfaz y sus implementaciones
public class Main {
    public static void main(String[] args) {
        Figure[] figures = {
            new Triangle("Rojo", 3, 4, 5),
            new Circle("Azul", 2.5),
            new Rectangle("Verde", 4, 6),
            new Hexagon("Amarillo", 2)
        };

        for (Figure figure : figures) {
            System.out.println("Color: " + figure.getColor());
            System.out.println("Perimetro: " + figure.perimeter());
            System.out.println("Area: " + figure.area());
            System.out.println();
        }
    }
}
