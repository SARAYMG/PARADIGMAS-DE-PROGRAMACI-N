class Persona:
    def __init__(self, nombre='', edad=0, direccion='', telefono='', correo_electronico=''):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Correo electrónico: {self.correo_electronico}"

def main():
    # Crear una instancia de Persona
    persona = Persona("Saray", 22, "Av.10 Col.Ignacio Zaragoza", "55-14-06-78-14", "saraymendogarcia29@gmail.com")
    
    # Imprimir los detalles de la persona
    print("Detalles de la persona:")
    print(persona)

if __name__ == "__main__":
    main()
