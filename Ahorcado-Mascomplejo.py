import random

#Word
palabra = ["electroencefalografista", "adolescente", "individuo", "caballero", "espiritu", "enfermedad", "matrimonio", "hermano", "criatura", "naturaleza", "desierto", "caballo", "elefante", "langosta", "saltamontes", "marisco", "vegetal", "serpiente", "alimento", "cocodrilo", "almendra", "zanahoria", "naranja", "manzana", "patata", "segundo", "momento", "instante", "anochecer", "ambiente", "espacio", "superficie"]

#Hangman Game
def juego_ahorcado(palabra):
    print("\nBienvenido al juego del ahorcado!\nTendras que adivinar la palabra escribiendo las letras que creas que lo compone!\nTendras 5 intentos que se reinician cada vez que aciertas una letra. Suerte!") #("Welcome to the hangman game! You have to guess the word writing the letters you think it's made of! You have 5 tries that resets each time you guess a word. Good luck!")
    palabra_a_adivinar = [] #("word_to_guess")
    palabra_adivinada = [] #("Guessed_word")
    palabra_random = random.choice(palabra) #("random_word")
    intentos = 0 #("Tries")
    condicion_victoria = False #("Win condition")
    for i in palabra_random:
        palabra_a_adivinar.append(i)
        palabra_adivinada.append("_")
    while intentos < 5:
        letra = input("\n\nEscribe una letra:  ") #("Write a letter")
        #El codigo de posiciones revisa la lista que contiene las letras de la palabra a adivinar y lo compara con la letra ingresada para realizar una lista con las posiciones donde se encuentra esa letra. Si no se encuentra la letra la lista queda vacia
        #The position code checks the list containing the letters of the word to be guessed and compares it with the entered letter to create a list with the positions where that letter is found. If the letter is not found, the list remains empty.
        posiciones = [i for i in range(len(palabra_a_adivinar)) if palabra_a_adivinar[i] == letra]
        if letra in palabra_a_adivinar:
            print("\nLetra correcta") #("Correct word")
            intentos = 0
        else:
            print("Letra incorrecta") #("Incorrect word")
            intentos += 1
        for j in posiciones:
            palabra_adivinada[j] = letra
        for h in palabra_adivinada:
            print("  ", h, end=" ")
        if "_" not in palabra_adivinada:
            condicion_victoria = True
            break
    if condicion_victoria == False:
        print(f"\nQue pena :( no has sido capaz de adivinar la palabra //{palabra_random}//. Pero no te desanimes intenta otra vez!") #("How sad :( You coudn't guess the word //{random_word}//. But don't be discouraged. Try it again!")
    if condicion_victoria == True:
        print(f"\nFelicidades! Has adivinado exitosamente la palabra //{palabra_random}//. Sigue jugando para adivinar más!") #("CONGRATULATIONS! You've guessed successfully the word //{random_word}//. Keep playing to guess more!")

def mostar_menu_principal():
    while True:
        print("\n***BIENVENIDO AL PROGRAMA DE JUEGO DE AHORCADO***") #("WELCOME TO THE HANGMAN GAME PROGRAM")
        seleccion = input("Elige una opcion:\n1.-Jugar\n2.-Salir\n") #("Choose an option: 1.-Play 2.-Exit")
        seleccion = seleccion.lower()
        if seleccion == "1" or seleccion == "jugar":
            juego_ahorcado(palabra)
        if seleccion == "2" or seleccion == "salir":
            print("Cerrando programa\nGracias por jugar!") #("Closing program. Thanks for playing!")
            break

mostar_menu_principal()


