import java.lang.Math;

public class Punto3D {
    private double x;
    private double y;
    private double z;

    public Punto3D() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    public Punto3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Punto3D(Punto3D punto) {
        this.x = punto.getX();
        this.y = punto.getY();
        this.z = punto.getZ();
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void setZ(double z) {
        this.z = z;
    }

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public double getZ() {
        return this.z;
    }

    public double distancia(Punto3D otroPunto) {
        double dx = this.x - otroPunto.getX();
        double dy = this.y - otroPunto.getY();
        double dz = this.z - otroPunto.getZ();
        return Math.sqrt(dx*dx + dy*dy + dz*dz);
    }

    public static void main(String[] args) {
        Punto3D[] puntos = new Punto3D[10];

        // Inicializando los puntos con valores arbitrarios
        for (int i = 0; i < puntos.length; i++) {
            puntos[i] = new Punto3D(i, i + 1, i + 2);
        }

        // Mostrando las coordenadas de los puntos
        for (int i = 0; i < puntos.length; i++) {
            System.out.println("Coordenadas del punto " + (i+1) + ": (" + puntos[i].getX() + ", " + puntos[i].getY() + ", " + puntos[i].getZ() + ")");
        }

        // Calculando y mostrando la distancia entre todos los pares de puntos
        for (int i = 0; i < puntos.length; i++) {
            for (int j = i + 1; j < puntos.length; j++) {
                double distancia = puntos[i].distancia(puntos[j]);
                System.out.println("Distancia entre el punto " + (i+1) + " y el punto " + (j+1) + ": " + distancia);
            }
        }
    }
}


