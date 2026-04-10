class Alumno:
    def datos (self,nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def mostrar (self):
        if (self.notas) >=6:
         print("El Alumno/a:", self.nombre,"tiene de nota:", self.notas,"Aprobado")
        else:
         print("El Alumno/a:", self.nombre,"tiene de nota:", self.notas,"Desaprobado")

nom = str(input("Ingrese el nombre del alumno/a: "))
calificaciones = int(input("Ingrese la nota del alumno/a: "))

alumno = Alumno()
alumno.datos(nom,calificaciones)
alumno.mostrar()
