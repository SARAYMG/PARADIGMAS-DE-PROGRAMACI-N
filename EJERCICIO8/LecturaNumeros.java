import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.IOException;

public class LecturaNumeros extends BufferedReader {

    // Constructor que usa System.in
    public LecturaNumeros() {
        super(new InputStreamReader(System.in));
    }

    // Constructor que usa un Reader proporcionado
    public LecturaNumeros(Reader r) {
        super(r);
    }

    // Método para leer un entero de la entrada
    public int readInt() throws IOException {
        return Integer.parseInt(readLine());
    }

    // Método para leer un entero de la entrada con un mensaje
    public int readInt(String mensaje) throws IOException {
        System.out.print(mensaje);
        return readInt();
    }

    // Método para leer un Integer de la entrada
    public Integer readInteger() throws IOException {
        return Integer.valueOf(readLine());
    }

    // Método para leer un Integer de la entrada con un mensaje
    public Integer readInteger(String mensaje) throws IOException {
        System.out.print(mensaje);
        return readInteger();
    }

    // Método para leer un double de la entrada
    public double readDouble() throws IOException {
        return Double.parseDouble(readLine());
    }

    // Método para leer un double de la entrada con un mensaje
    public double readDouble(String mensaje) throws IOException {
        System.out.print(mensaje);
        return readDouble();
    }
}
