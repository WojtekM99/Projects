number = 0
result = None
reset = True
operation = None
calc_operations = ["+", "-"]

while True:
    if reset == True:
        number = int(input("Podaj pierwszą liczbę: "))
        reset = False
    
    operation = input("Wybierz znak: " + str(calc_operations) + "lub wybierz RESET bądź FINISH: ")

    if operation == "reset": 
        reset = True
        continue
    
    if operation == "finish": 
        break 
    
    number2 = int(input("Podaj drugą liczbę: "))

    if operation == "+":
        result = number + number2

    if operation == "-":
        result = number - number2

    print("Wynik: ", result)
    number = result
    

