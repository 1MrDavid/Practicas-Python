#Variables
Calificacion = [] #Notes
Nombre = [] #Name
AuxNombre = "" #AuxiliaryName
AuxCalif = 0 #AuxiliaryNote
Posicion = int(input("Cuantos estudiantes desea registrar? ")) #Position ("How many students do you want to registry? ")
 
for n in range(Posicion):
    print("Ingrese los datos del estudiante ", n + 1) #("Write the student's information")
    AuxNombre = input("Nombre: ") #("Name")
    AuxCalif = input("Calificación: ") #("Notes")
    Nombre.append(AuxNombre)
    Calificacion.append(AuxCalif)

cont = len(Calificacion) #This stand for count or "contador"

for i in range(cont):
    for j in range(cont-i-1):
        if Calificacion[j] < Calificacion[j + 1]:
            Calificacion[j], Calificacion[j + 1] = Calificacion[j + 1], Calificacion[j]
            Nombre[j], Nombre[j + 1] = Nombre[j + 1], Nombre[j]
print(Nombre)
print(Calificacion)