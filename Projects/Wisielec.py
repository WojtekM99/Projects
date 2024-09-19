import random

start = 1
word_list = ["kamila", "ola", "karolina", "paulina"]
user_word = []
used_letters = []
word = random.choice(word_list)

def find_index(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", no_of_tries)
    print("Uyte litery:",used_letters)
    print()
    

for _ in word:
        user_word.append("_")

no_of_tries = int(input("Podaj liczbę prób: "))

while start == 1:
    letter = input("Podaj literę: ")
    
    if letter in used_letters:
        print("Ta litera juz została podana")
        continue
    try:
        a = "a" # wczytaj pierwszy znak
        b = "z" # wczytaj drugi znak
        x = ord(a) # wyznacz kod ASCII pierwszego znaku
        y = ord(b) # wyznacz kod ASCII drugiego znaku    
        z = ord(letter)
        if z in range (x, y):
            used_letters.append(letter)
        else:
            print("Zły znak! Podaj literę!")
            continue
    except TypeError:
        print("Podano więcej niz jedną literę!")
        continue
    
    found_letters = find_index(word, letter)

    if len(found_letters) == 0: #found_letters to fukncja która zwraca znalezione indexy (2 dla "a"), i jak dlugosc znalezionych bedzie 0 to znaczy ze nie znalezlismy zadnego czyli nie ma takiej litery w slowie
        print("Nie ma takiej litery")
        no_of_tries -= 1
        
    if no_of_tries == 0:
        print("Przegrałeś")
        ask = input("Wybierz wyłącz lub zacznij od nowa: ")
        if ask == "wyłącz":
            start = 0
            break
        if ask == "zacznij od nowa":
            start = 1
            no_of_tries = 5
            word = "kamila"
            user_word = []
            used_letters = []
            for _ in word:                    
                user_word.append("_")
    else:
        for index in found_letters:
            user_word[index] = letter
    
        if "".join(user_word) == word:          #tworzymy pusty string i łączym elementy listy zeby polączyło litery z listy
            print("Brawo!")
            ask = input("Wybierz wyłącz lub zacznij od nowa: ")
            if ask == "wyłącz":
                start = 0
                break
            if ask == "zacznij od nowa":
                start = 1
                no_of_tries = 5
                word = "kamila"
                user_word = []
                used_letters = []
                for _ in word:
                    user_word.append("_")

    show_state_of_game()