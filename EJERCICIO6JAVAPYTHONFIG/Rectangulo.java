public class Rectangulo {
    private double largo;
    private double ancho;
    private String color;

    public Rectangulo(double largo, double ancho, String color) {
        this.largo = largo;
        this.ancho = ancho;
        this.color = color;
    }

    public double getArea() {
        return area();
    }

    public double getPerimetro() {
        return perimetro();
    }

    public String getColor() {
        return color;
    }

    private double area() {
        return largo * ancho;
    }

    private double perimetro() {
        return 2 * (largo + ancho);
    }
}
