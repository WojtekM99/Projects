import sys
import random
import string

password = []
start = 0

def updateCharactersLeft(numberCharacters):
    global charactersLeft
    if numberCharacters > charactersLeft or numberCharacters < 0:
        print("Too much characters used!")
        sys.exit(0)
    charactersLeft -= numberCharacters
    print("Pozostało znaków:",charactersLeft)

while start == 0:
    try: 
        passwordLengh = int(input("Jak długie ma być hasło? "))
    except:
        print("Podaj liczbę!\n")
        continue
    charactersLeft = passwordLengh
    if passwordLengh < 5:
        print("Hasło musi mieć minimum 5 znaków. Try again!")
        print()
        continue
    else:
        break

while start == 0:
    try:
        lowercaseLetters = int(input("Ile małych liter ma mieć hasło? "))
        updateCharactersLeft(lowercaseLetters)
    except:
        continue

    try:
        uppercaseLetters = int(input("Ile duych liter ma mieć hasło? "))
        updateCharactersLeft(uppercaseLetters)
    except:
        continue

    try:
        specialCharacters = int(input("Ile znaków specjalnych ma mieć hasło? "))
        updateCharactersLeft(specialCharacters)
    except:
        continue

    try:
        digits = int(input("Ile cyfr ma mieć hasło? "))
        updateCharactersLeft(digits)
    except:
        continue
    
    if charactersLeft > 0:
        lowercaseLetters += charactersLeft
        print("Pozostało nieywkorzystanych",charactersLeft,"znaków. Zostaną dodane do lowercaseLetters")

    print()
    print("Długość hasła:",passwordLengh)
    print("Małe litery:",lowercaseLetters)
    print("Due liter:",uppercaseLetters)
    print("Znaki specjalne:",specialCharacters)
    print("Cyfry:",digits)

    for _ in range(passwordLengh):
        if lowercaseLetters > 0:
            password.append(random.choice(string.ascii_lowercase))
            lowercaseLetters -= 1
        if uppercaseLetters > 0:
            password.append(random.choice(string.ascii_uppercase))
            uppercaseLetters -= 1
        if specialCharacters> 0:
            password.append(random.choice(string.punctuation))
            specialCharacters -= 1
        if digits > 0:
            password.append(random.choice(string.digits))
            digits -= 1
    
    random.shuffle(password)
    print("".join(password))
    break
    
