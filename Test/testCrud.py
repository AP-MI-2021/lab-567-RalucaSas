from Domain.Cheltuiala import getId, getNr_apartament, getSuma, getData, getTip
from Logic.CRUD import adaugaCheltuiala, getById, stergeCheltuiala, modificaCheltuiala

"""def testGetById():
    lista = []
    lista = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista)
    lista = adaugaCheltuiala("2", 24, 200, 2020, "cadura", lista)
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    lista2 = []
    lista2 = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista2)
    lista2 = adaugaCheltuiala("3", 24, 200, 2020, "cadura", lista2)
    assert getById("1", lista2) is not None
    assert getById("2", lista2) is None
    assert getById("3", lista2) is not None

def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNr_apartament(getById("1", lista)) == 2
    assert getSuma(getById("1", lista)) == 250
    assert getData(getById("1", lista)) == 2015
    assert getTip(getById("1", lista)) == "apa"


    lista = []
    lista = adaugaCheltuiala("2", 24, 200, 2020, "caldura", lista)

    assert len(lista) == 1
    assert getId(getById("2", lista)) == "2"
    assert getNr_apartament(getById("2", lista)) == 24
    assert getSuma(getById("2", lista)) == 200
    assert getData(getById("2", lista)) == 2020
    assert getTip(getById("2", lista)) == "caldura"

def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista)
    lista = adaugaCheltuiala("2", 24, 200, 2020, "caldura", lista)

    lista = stergeCheltuiala("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergeCheltuiala("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False


    lista = []
    lista = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista)
    lista = adaugaCheltuiala("2", 24, 200, 2020, "caldura", lista)
    lista = adaugaCheltuiala("3", 45, 100, 2005, "apa", lista)

    lista = stergeCheltuiala("2", lista)

    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is not None

def testModificaCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista)
    lista = adaugaCheltuiala("2", 24, 200, 2020, "caldura", lista)

    lista = modificaCheltuiala("1" , 45, 100, 2005, "apa", lista)

    cheltuialaUpdatata = getById("1", lista)
    assert getId(cheltuialaUpdatata) == "1"
    assert getNr_apartament(cheltuialaUpdatata) == 45
    assert getSuma(cheltuialaUpdatata) == 100
    assert getData(cheltuialaUpdatata) == 2005
    assert getTip(cheltuialaUpdatata) == "apa"

    cheltuialaNeupdatata = getById("2", lista)
    assert getId(cheltuialaNeupdatata) == "2"
    assert getNr_apartament(cheltuialaNeupdatata) == 24
    assert getSuma(cheltuialaNeupdatata) == 200
    assert getData(cheltuialaNeupdatata) == 2020
    assert getTip(cheltuialaNeupdatata) == "caldura"


    lista = []
    lista = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista)
    try:
        lista = modificaCheltuiala("3", 24, 200, 2020, "caldura", lista)
    except ValueError:
        cheltuialaNeupdatata = getById("1", lista)
        assert getId(cheltuialaNeupdatata) == "1"
        assert getNr_apartament(cheltuialaNeupdatata) == 2
        assert getSuma(cheltuialaNeupdatata) == 250
        assert getData(cheltuialaNeupdatata) == 2015
        assert getTip(cheltuialaNeupdatata) == "apa"
    except Exception:
        assert False

    lista = []
    lista = adaugaCheltuiala("1", 2, 250, 2015, "apa", lista)
    lista = adaugaCheltuiala("3",  45, 100, 2005, "apa", lista)

    lista = modificaCheltuiala("2", 24, 200, 2020, "caldura", lista)

    cheltuialaNeupdatata = getById("1", lista)
    assert getId(cheltuialaNeupdatata) == "1"
    assert getNr_apartament(cheltuialaNeupdatata) == 2
    assert getSuma(cheltuialaNeupdatata) == 250
    assert getData(cheltuialaNeupdatata) == 2015
    assert getTip(cheltuialaNeupdatata) == "apa"

    cheltuialaUpdatata = getById("2", lista)
    assert getId(cheltuialaUpdatata) == "2"
    assert getNr_apartament(cheltuialaUpdatata) == 24
    assert getSuma(cheltuialaUpdatata) == 200
    assert getData(cheltuialaUpdatata) == 2020
    assert getTip(cheltuialaUpdatata) == "caldura" """
