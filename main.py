from Logic.CRUD import adaugaCheltuiala
from Test.testAll import runAllTests
from UI.console import runMenu
from UI.command_line_console import run_console

def main():
    runAllTests()
    lista = []
    lista = adaugaCheltuiala("1", 2, 10, 10, "caldura", lista)
    lista = adaugaCheltuiala("2", 3, 12, 30, "apa", lista)
    while True:
        print(
            "Apasati 1 pentru primul tip de interfata (console), 2 pentru al doilea tip de interfata (command_line_console) si x pentru a iesi din program")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            run_console(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")


if __name__ == '__main__':
    main()
