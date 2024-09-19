number = 0
listOperations = ["+", "-", "*", "/", "**"]
start = True

while True:
    if start == True:
        firstNumber = float(input("Podaj pierwszą liczbę: "))
        start = False

    operation = input("Podaj działanie matematyczne z dostępnych lub wpisz koniec/reset: " + str(listOperations))

    if operation == "zakoncz":
        break
    if operation == "reset":
        start = True
        continue
    if not operation in listOperations:
        print("Wprowadzono błędną operację!")
        continue

    number = float(input("Podaj liczbę: "))
    
    if operation == "+":
        sum = firstNumber + number
        print(sum)
    
    if operation == "-":
        sum = firstNumber - number
        print(sum)
    
    if operation == "*":
        sum = firstNumber * number
        print(sum)
    
    if operation == "/":
        sum = firstNumber / number
        print(sum)

    if operation == "**":
        sum = firstNumber ** number
        print(sum)
    
    firstNumber = sum
    print("Wynik: ", sum)
    