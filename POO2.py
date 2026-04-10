class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} es menor de edad")

# Programa principal
nombre = str(input("Ingrese el nombre de la persona: "))
edad = int(input("Ingrese la edad de la persona: "))

persona = Persona(nombre, edad)
persona.mostrar()
persona.es_mayor_de_edad()
