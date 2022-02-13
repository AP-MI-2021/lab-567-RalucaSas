
from Domain.Cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Logic.functionalitate import  sumaPerApartament, ordonareDupaSuma, cheltuieliTip


def printMenu():
    print("1. Adaugare apartament")
    print("2. Stergere apartament")
    print("3. Modificare apartament")
    print("4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială")
    print("5. Ordonarea cheltuielilor descrescător după sumă.")
    print("6. Ordonarea vanzarilor crescator dupa pret")
    print("7. Afișarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare apartamente")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        nr_apartament = input("Dati nr_apartament: ")
        suma = float(input('Dati suma: '))
        data = input("Dati data: ")
        tip = int(input("Dati tipul :"))
        rezultat = adaugaCheltuiala(id, nr_apartament, suma, data, tip, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeCheltuiala(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul apartamentului de sters: ")
        rezultat = stergeCheltuiala(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaCheltuiala(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul apartamentului de modificat: ")
        nr_apartament = input("Dati noul nr_apartament: ")
        suma = float(input('Dati noua suma: '))
        data = input("Dati noua data: ")
        tip =input("Dati noul tip de reducere: ")
        rezultat = modificaCheltuiala(id, nr_apartament, suma, data, tip, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiOrdonareDupaSuma(lista, undo_list, redo_list):
    rezultat = ordonareDupaSuma(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def uiSumaPerApartament(lista):
    rezultat = sumaPerApartament(lista)
    for nr_apartament in rezultat:
        print("Apartamentul {} are suma preturilor {}".format(nr_apartament, rezultat[nr_apartament]))

def cheltuieliTip(lista):
    rezultat = cheltuieliTip(lista)
    for tip in rezultat:
        print("Tipul {} are cea mai mica cheltuiala {}".format(tip, rezultat[tip]))

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def runMenu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista, undo_list, redo_list)
        elif optiune == "4":
            uiSumaPerApartament(lista)
        elif optiune == "5":
            lista = uiOrdonareDupaSuma(lista, undo_list, redo_list)
        elif optiune == "6":
            cheltuieliTip(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
