from Domain.Cheltuiala import getId, getTip, getSuma
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.functionalitate import ordonareDupaSuma


def test_undo_redo():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima cheltuiala
    rezultat = adaugaCheltuiala("1", 1, 200, 2021, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua cheltuiala
    rezultat = adaugaCheltuiala("2", 6, 300, 2021, "gaz", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia cheltuiala
    rezultat = adaugaCheltuiala("3", 78, 400, 2021, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

    # 5. primul undo scoate ultima cheltuiala adaugata
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    # 6. inca un undo scoate penultima cheltuiala adaugata
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]

    # 7. inca un undo scoate prima cheltuiala adaugata
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert undo_list == []

    # 8. inca un undo care nu face nimic
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list
    assert len(lista) == 0
    assert undo_list == []

    # 9. se adauga trei cheltuielii
    rezultat = adaugaCheltuiala("1", 1, 200, 2021, "apa", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    rezultat = adaugaCheltuiala("2", 6, 300, 2021, "gaz", lista)
    undo_list.append(lista)
    lista = rezultat

    rezultat = adaugaCheltuiala("3", 78, 400, 2021, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 10. se face redo (fara sa faca nimic)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 11. se fac 2 undo-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]

    # 12. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert len(lista) == 2

    # 13. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 14. se fac 2 undo-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]

    # 15. se adauga a patra cheltuiala
    rezultat = adaugaCheltuiala("4", 5, 890, 2020, "gaz", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    # 16. se face redo (fara sa faca nimic)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(undo_list) == 2

    # 17. se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert len(undo_list) == 1
    assert len(redo_list) == 1

    # 18. se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert len(undo_list) == 0
    assert len(redo_list) == 2

    # 19. se face 2 redo-uri
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 1

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0

    # 20. se face ultimul redo, care nu face nimic
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0
    assert len(undo_list) == 2

def test_undo_redo_modificare_gen():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima librarie
    rezultat = adaugaCheltuiala("1", 23, 500, 2015, "gaz", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua librarie
    rezultat = adaugaCheltuiala("2", 24, 80, 2025, "gaz", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia librarie
    rezultat = adaugaCheltuiala("3", 25, 250, 2020, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

    # 5. primul undo intoarce la genul original
    redo_list.append(lista)
    lista = undo_list.pop()
    assert getTip(getById("1", lista)) == "apa"

    # 6. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert getTip(getById("1", lista)) == "gaz"


def test_undo_redo_discount():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima cheltuiala
    rezultat = adaugaCheltuiala("1", 23, 500, 2015, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua cheltuiala
    rezultat = adaugaCheltuiala("2", 24, 80, 2025, "gaz", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia cheltuiala
    rezultat = adaugaCheltuiala("3", 25, 250, 2020, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

def test_undo_redo_OrdonareDupaSumat():
    # 1. lista goala
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga prima librarie
    rezultat = adaugaCheltuiala("1", 23, 500, 2015, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga a doua librarie
    rezultat = adaugaCheltuiala("2", 24, 80, 2025, "gaz", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga a treia librarie
    rezultat = adaugaCheltuiala("3", 25, 250, 2020, "apa", lista)
    undo_list.append(lista)
    lista = rezultat

    # 5. se ordoneaza lista
    rezultat = ordonareDupaSuma(lista)
    undo_list.append(lista)
    lista = rezultat
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "3"
    assert getId(lista[2]) == "2"

    # 6. primul undo intoarce la lista originala
    redo_list.append(lista)
    lista = undo_list.pop()
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "3"

    # 7. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "3"
    assert getId(lista[2]) == "2"