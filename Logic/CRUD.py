from Domain.Cheltuiala import creeazaCheltuiala, getId

#id, nr_apartament, suma, data, tip
def adaugaCheltuiala(id, nr_apartament, suma, data, tip, lista):
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    if int(id) < 1:
        raise ValueError("ID-ul nu poate fi nul sau negativ!")
    if int(nr_apartament) == 0:
        raise ValueError("Introduceti numarulul apartamentului!")
    if suma < 0:
        raise ValueError("Introduceti suma!")
    if int(data) < 1:
        raise ValueError("Introduceti data")
    if tip != "gaz" and tip != "caldura" and tip != "apa" and tip != "gaz" and tip != "gaz" and tip != "apa":
        raise ValueError("Reducere invalida! Introduceti apa, gaz sau  caldura")
    cheltuiala = creeazaCheltuiala(id, nr_apartament, suma, data, tip)
    return lista + [cheltuiala]

def getById(id, cheltuielii):
    for cheltuiala in cheltuielii:
        if getId(cheltuiala) == id:
            return cheltuiala
    return None

def stergeCheltuiala(id, lista):
    if getById(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat")
    return [cheltuiala for cheltuiala in lista if getId(cheltuiala) != id]

def modificaCheltuiala(id, nr_apartament, suma, data, tip, lista):
    if getById(id, lista) is None:
        raise ValueError("Nu exista o librarie cu id-ul dat")
    if int(nr_apartament) == 0:
        raise ValueError("Introduceti nr_apartament!")
    if suma < 0:
        raise ValueError("Introduceti suma!")
    if int(data) < 1:
        raise ValueError("Introduceti data")
    if tip != "gaz" and tip != "caldura" and tip != "apa" and tip != "gaz" and tip != "gaz" and tip != "apa":
        raise ValueError("Reducere invalida! Introduceti apa, gaz sau  caldura")
    listaNoua = []
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            cheltuialaNoua = creeazaCheltuiala(id, nr_apartament, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
