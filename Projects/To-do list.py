taskList = []
operation = 0

def show_tasks():
    taskIndex = 0
    for task in taskList:
        print(task, "-", taskIndex)
        taskIndex += 1

def add_task():
    task = input("Jakie zadanie chcesz wykonać? ")
    if task != "":
        taskList.append(task)
        print("Dodano zadanie!")
    else:
        print("Nic nie dodałeś!")

def delete_task():
    task = int(input("Podaj numer zadania które chcesz usunąć: "))
    if task >= 0 or task <= len(taskList) - 1:
        taskList.pop(task)
        print("Usunięto!")
    else:
        print("Nie ma takiego numeru!")

def save_task():
    file = open("nowy.txt", "w")
    for task in taskList:
        file.write(task + "\n")
    file.close()

def load_tasks():
    try:
        file = open("plik.txt")
        for line in file.readlines():
            taskList.append(line.lstrip())
    except FileNotFoundError:
        return

load_tasks()

while operation != 5:
    if operation == 1:
        show_tasks()
    if operation == 2:
        add_task()
    if operation == 3:
        delete_task()    
    if operation == 4:
        save_task()
    
    print()
    print("1. Wyświetl zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zadanie do pliku")
    print("5. Wyjdź z programu")

    operation = int(input("Podaj numer operacji którą chcesz wykonać: "))
