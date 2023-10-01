print("""Bienvenido!
Este programa sirve para calcular el perímetro de un polígono regular.
El perímetro de un polígono regular es igual a la longitud de uno de sus lados por el número de lados.
Recuerde que un polígono regular tiene lados y ángulos iguales.""") #("Welcome! This program is used to calculate the perimeter of a regular polygon. The perimeter of a regular polygon is equal to the length of one of its sides multiplied by the number of sides. Remember, a regular polygon has equal sides and angles.")

#Asignación de variables y un verificador porque los lados de un polígono no puede ser negativo o cero
#Variable assigment. Added a verifier because a Regular polygon can't have a negative side
verificador = False #verifier
while verificador == False:
    Numero_Lados = int(input("Cuantos lados tiene el polígono? ")) #("How many sides has the polygon")
    Lados = int(input("Cuanto mide los lados del cuadrado? ")) #("How long are the sides of the square?")

    if Lados <= 0:
        print("Por favor ingrese un número mayor a 0") #("Please, write a number higher than 0")
    else:
        verificador = True

Perimetro = Numero_Lados * Lados #perimeter

print("El perímetro del polígono regular es: ", Perimetro) #("The perimeter of the regular polygon is")