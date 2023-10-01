print("""Bienvenido!
Este programa sirve para calcular el perímetro de un triangulo.
El perímetro consta de la suma de los tres lasdos del triangulo""") #("Welcome! This program is used to calculate the perimeter of a triangle. The perimeter is the sum of the three sides of the triangle.")

#Asignación de variables. Agrego un verificador porque un triangulo no puede tener un lado con un valor negativo
#Variable assigment. Added a verifier because a triangle can't have a negative side
verificador = False #verifier
while verificador == False:
    Lado1 = int(input("Cuanto mide el primer lado del triangulo? ")) #side1 ("How long is the first side of the triangle?")
    Lado2 = int(input("Cuanto mide el segundo lado del triangulo? ")) #side2 ("How long is the second side of the triangle?")
    Lado3 = int(input("Cuanto mide el tercer lado del triangulo? ")) #side3 ("How long is the third side of the triangle?")

    if Lado1 <= 0 or Lado2 <= 0 or Lado3 <= 0:
        print("Por favor ingrese un número mayor a 0") #("Please, write a number higher than 0")
    else:
        verificador = True

#El perimetro de un triangulo es la suma de sus lados
#A triangle's perimeter is the sum of all it sides
#Dependiendo del tipo se pueden hacer formulas más cortas pero sigue siendo igual que sumar los tres lados
#Depending the type of the triangle we can do shorter formulas but they're all the sum of the three sides
Perimetro = Lado1 + Lado2 + Lado3 #perimeter

#Especificar que tipo de triangulo para agregar más al código
#Specify which type of triangle is for adding more lines to the code
if Lado1 != Lado2 and Lado2 != Lado3 and Lado1 != Lado3:
    print("Su tipo de triangulo es escaleno y su perimetro es de: ", Perimetro) #("Its type of triangle is scalene, and its perimeter is:")
if Lado1 == Lado2 != Lado3 or Lado1 == Lado3 != Lado2 or Lado2 == Lado3 != Lado1:
    print("Su tipo de triangulo es isósceles y su perimetro es de: ", Perimetro) #("Its type of triangle is  isosceles, and its perimeter is:")
if Lado1 == Lado2 == Lado3:
    print("Su tipo de triangulo es equilatero y su perimetro es de: ", Perimetro) #("Its type of triangle is equilateral, and its perimeter is:")
           
