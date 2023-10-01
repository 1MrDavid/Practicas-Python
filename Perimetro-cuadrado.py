print("""Bienvenido!
Este programa sirve para calcular el perímetro de un cuadrado.
El perímetro es igual a la suma de los cuatro lados del cuadrado. 
Recuerde que todos los lados miden lo mismo.""") #("Welcome! This program is used to calculate the perimeter of a square. The perimeter is equal to the sum of all four sides of the square. Remember, all sides are of the same length.")

#Asignación de variables y un verificador porque los lados de un cuadrado no puede ser negativo o cero
#Variable assigment. Added a verifier because a square can't have a negative side
verificador = False #verifier
while verificador == False:
    Lados = int(input("Cuanto mide los lados del cuadrado? ")) #sides ("How long are the sides of the square?")

    if Lados <= 0:
        print("Por favor ingrese un número mayor a 0") #("Please, write a number higher than 0")
    else:
        verificador = True

#Como todos los lados del cuadrado valen lo mismo entonces solo hace falta tomar una variable y multiplicarlo por cuatro
#All the sides of a square are equal so the perimeter is equal to 4 times the side
Perimetro = Lados * 4
print("El perímetro del cuadrado es igual a: ", Perimetro)