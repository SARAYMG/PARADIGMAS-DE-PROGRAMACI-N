public class Main {
    public static void main(String[] args) {
    // Crear una instancia de Persona
    Persona persona = new Persona("Saray", 22, "Av.10 Col.Ignacio Zaragoza", "55-14-06-78-14", "saraymendogarcia29@gmail.com");
        
    // Imprimir los detalles de la persona
    System.out.println("Detalles de la persona:");
    System.out.println("Nombre: " + persona.getNombre());
    System.out.println("Edad: " + persona.getEdad());
    System.out.println("Dirección: " + persona.getDireccion());
    System.out.println("Teléfono: " + persona.getTelefono());
    System.out.println("Correo electrónico: " + persona.getCorreoElectronico());
    }
    }