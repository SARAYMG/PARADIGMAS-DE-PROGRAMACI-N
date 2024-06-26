abstract class Figure {
    protected String color;

    public Figure(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public abstract double perimeter();
    public abstract double area();
}

class Triangle extends Figure {
    private double a, b, c;

    public Triangle(String color, double a, double b, double c) {
        super(color);
        this.a = a;
        this.b = b;
        this.c = c;
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

class Circle extends Figure {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
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

class Rectangle extends Figure {
    private double width, height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
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

class Hexagon extends Figure {
    private double side;

    public Hexagon(String color, double side) {
        super(color);
        this.side = side;
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
