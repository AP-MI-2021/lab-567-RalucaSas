from Domain.Cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, getById, stergeCheltuiala

#id, nr_apartament, suma, data, tip
def print_help():
    print("Comenzi disponibile: ")
    print("Ajutor: ")
    print("Adauga vanzare: adauga, id, nr_apartament, suma, data, tip ")
    print("Sterge vanzare: sterge, id ")
    print("Afisare: showall ")
    print("Stop ")
    print("Parametrii trebuie separati prin virgula. ")
    print("Comenzile trebuie separate prin ; ")

def adauga(lista, parametrii):
    try:
        if len(parametrii) < 6:
            print("Parametrii insuficienti")
            return lista
        if len(parametrii) > 6:
            print("Prea multi parametrii")
            return lista
        id = str(parametrii[1])
        nr_apartament = str(parametrii[2])
        suma = float(parametrii[3])
        data = str(parametrii[4])
        tip = str(parametrii[5])
        lista = adaugaCheltuiala(id, nr_apartament, suma, data, tip, lista)
        print("Adaugare efectuata")
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def sterge(lista, parametrii):
    try:
        if len(parametrii) < 2:
            print("Parametrii insuficienti")
            return lista
        if len(parametrii) > 2:
            print("Prea multi parametrii")
            return lista
        id = parametrii[1]
        if getById(id, lista) is None:
            raise ValueError("Nu exista Id-ul dat")
        print("Stergere efectuata")
        return stergeCheltuiala(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showall(lista, parametrii):
    if len(parametrii)>1:
        print("Comanda Afisare nu contine alti parametrii")
    else:
        for cheltuiala in lista:
            print(toString(cheltuiala))

def run_console(lista):
    print("Comenzi disponibile: ")
    print("Ajutor: ")
    print("Adauga vanzare: adauga, id, nr_apartament, suma, data, tip ")
    print("Sterge vanzare: sterge, id ")
    print("Afisare: showall ")
    print("Stop ")
    print("Parametrii trebuie separati prin virgula. ")
    print("Comenzile trebuie separate prin ; ")
    contor = True
    while contor:
        comenzi = input("Introduceti comenzile (Ajutor, Adauga, Sterge, Afisare, Stop): ")
        functii = comenzi.split(";")
        for functie in functii:
            parametrii = functie.split(",")
            if(parametrii[0] == "Ajutor"):
                print_help()
            elif parametrii[0] == "Adauga":
                lista = adauga(lista, parametrii)
            elif parametrii[0] == "Sterge":
                lista = sterge(lista, parametrii)
            elif parametrii[0] == "Afisare":
                print("Lista de cheltuieli este: ")
                showall(lista, parametrii)
            elif parametrii[0] == "Stop":
                contor = False
            else:
                print("Comanda incorecta! Reincercati")