print("""Bienvenido!
Este programa sirve para calcular el perímetro de un rectangulo.
El perímetro es igual a la suma de los cuatro lados del rectangulo. 
Recuerde que los lados verticales (izquierda y derecha) valen lo mismo y los lados horizontales (arriba y abajo) valen lo mismo.""") #("Welcome! This program is used to calculate the perimeter of a rectangle. The perimeter is equal to the sum of the four sides of the rectangle. Remember that the vertical sides (left and right) are equal, and the horizontal sides (top and bottom) are equal.")

#Asignación de variables con un verificador para que no se admiten números negativos o 0
#Variable assigment with a verifier that prevent negative numbers or 0
verificador = False #verifier
while verificador == False:
    Lados_verticales = int(input("Cuanto mide los lados verticales del rectangulo? ")) #Vertical_sides ("How long are the vertical sides of the rectangle?")
    Lados_horizontales = int(input("Cuanto mide los lados horizontales del rectangulo? ")) #Horizontal_sides ("How long are the horizontal sides of the rectangle?")
    if Lados_verticales <= 0 or Lados_horizontales <= 0:
        print("Por favor ingrese un número mayor a 0") #("Please, write a number higher than 0")
    else:
        verificador = True

#El perimetro de un rectangulo es igual a dos veces la suma de ambos lados.
#A rectangle perimeter is equal two time the sum of both sides
#Existen otras formulas para el perimetro pero todas son iguales
#Exist other formulas but they're all the same
Perimetro = 2 * (Lados_verticales + Lados_horizontales) #perimeter
print("El perimetro del rectangulo es: ", Perimetro) #("The rectangle perimeter is equal to")