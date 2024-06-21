import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int port = 5000; // Puerto en el que el servidor escuchará
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Servidor iniciado, escuchando en el puerto: " + port);

            // El servidor necesita correr indefinidamente
            while (true) {
                try {
                    Socket clientSocket = serverSocket.accept(); // Aceptar una conexión de un cliente
                    System.out.println("Cliente conectado");

                    // Abrir streams para leer y escribir datos
                    BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                    PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                    // Leer el mensaje enviado por el cliente
                    String clientMessage = in.readLine();
                    System.out.println("Mensaje del Cliente: " + clientMessage);

                    // Enviar una respuesta al cliente
                    String response = "Mensaje recibido, cliente!";
                    out.println(response);
                    System.out.println("Respuesta enviada al Cliente: " + response);

                    // Cerrar la conexión con el cliente
                    clientSocket.close();
                } catch (IOException e) {
                    System.out.println("Exception caught when trying to listen on port " + port + " or listening for a connection");
                    System.out.println(e.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println("Exception caught when trying to listen on port " + port);
            System.out.println(e.getMessage());
        }
    }
}
