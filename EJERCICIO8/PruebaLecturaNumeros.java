import java.io.IOException;

public class PruebaLecturaNumeros {
    public static void main(String[] args) {
        // Utilizamos try-with-resources para asegurarnos de que el recurso se cierre automáticamente
        try (LecturaNumeros ln = new LecturaNumeros()) {
            
            // Leer 2 enteros
            int num1 = ln.readInt("Introduce el primer número entero: ");
            int num2 = ln.readInt("Introduce el segundo número entero: ");
            
            // Leer 1 Integer
            Integer num3 = ln.readInteger("Introduce un número entero (Integer): ");
            
            // Leer 1 double
            double num4 = ln.readDouble("Introduce un número de punto flotante (double): ");
            
            // Leer 1 Double
            Double num5 = Double.valueOf(ln.readDouble("Introduce otro número de punto flotante (Double): "));
            
            // Mostrar los números leídos
            System.out.println("Números leídos:");
            System.out.println("int1: " + num1);
            System.out.println("int2: " + num2);
            System.out.println("Integer: " + num3);
            System.out.println("double: " + num4);
            System.out.println("Double: " + num5);
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}



