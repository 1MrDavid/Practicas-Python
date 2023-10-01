import random

#Lista de palabras a adivinar
#List of words
lista_palabras = ["abrazo", "aburrido", "academia", "actor", "acero", "aguja", "ahorrar", "araña", "boxeo", "boda", "base", "caballo", "campana", "caracol", "chorizo", "cine", "cielo", "cocodrilo", "contacto", "cortina", "costilla", "deseo", "detective"]

#Juego tipo ahorcado
#Hangman game
def jugar_adivinanza(lista_palabras):
    print("En este juego se asignará una palabra la cual tiene que adivinar letra por letra\nTendras 10 intentos por cada letra y cuando adivinas una vuelves a tener los 10 intentos para adivinar la siguiente\nGanas al adivinar la palabra y pierdes al gastar 10 intentos intentando adivinar una letra.\n") 
    # ("In this game you'll have a word to guess word by word. You'll have 10 tries for each word and when you guess a word you have 10 tries again to guess the rest. You win if you guess the word and lose if you use 10 tries trying to guess a word")
    palabra_random = random.choice(lista_palabras) #random_word
    intentos = 0 #tries
    letras_palabra_adivinada = [] #letters_word_guessed
    letra_palabra = 0 #letter_word
    condicion_victoria = False #win condition
    for i in palabra_random:
                letras_palabra_adivinada.append("_")
    while intentos < 10:
        for j in range(len(letras_palabra_adivinada)):
            print(letras_palabra_adivinada[j], end=" ")
        adivinanza_palabra = input(f"\n¿Que letra corresponde a la posición {letra_palabra + 1}?\n") #guess_word ("Wich letter correspond to the position..")
        if adivinanza_palabra != palabra_random[letra_palabra]:
            print("Letra incorrecta") #("Incorrect word")
            intentos += 1
        if adivinanza_palabra == palabra_random[letra_palabra]:
            print("\nLetra correcta") #("Correct word")
            letras_palabra_adivinada[letra_palabra] = adivinanza_palabra
            letra_palabra += 1
            intentos = 0
        if "_" not in letras_palabra_adivinada:
            condicion_victoria = True
            break
    if condicion_victoria == True:
        print(f"FELICIDADES! Has adivinado exitosamente la palabra {palabra_random}! Sigue jugando para adivinar mas!") #("CONGRATULATIONS! You've guessed successfully the word  {random_word}! Keep playing to guess more!")
    if condicion_victoria == False:
        print(f"Que pena :( No has sido capaz de adivinar la palabra {palabra_random}. Pero no te desanimes. Intenta otra vez!") #("How sad :( You coudn't guess the word {random_word}. But don't be discouraged. Try it again!")
            
#Main
def mostar_menu_principal():
    while True:
        print("***BIENVENIDO AL PROGRAMA DE JUEGO DE ADIVINANZA DE PALABRAS***") #("WELCOME TO THE WORD GUESSING GAME")
        seleccion = input("Elige una opcion:\n1.-Jugar\n2.-Salir\n") #("Choose an option. 1.-Play 2.-Exit")
        seleccion = seleccion.lower()
        if seleccion == "1" or seleccion == "jugar":
            jugar_adivinanza(lista_palabras)
        if seleccion == "2" or seleccion == "salir":
            print("Finalizando programa") #("Ending program")
            break

mostar_menu_principal()