def creeazaLibrarie(id, nr_apartament, suma, data, tip):
    return {
        "id": id,
        "nr_apartament": nr_apartament,
        "suma": suma,
        "data": data,
        "tip": tip,
    }


#id, nr_apartament, suma, data, tip
def getId(cheltuiala):
    return cheltuiala["id"]


def getNr_apartament(cheltuiala):
    return cheltuiala["nr_apartament"]


def getSuma(cheltuiala):
    return cheltuiala["suma"]


def getData(cheltuiala):
    return cheltuiala["data"]


def getTip(cheltuiala):
    return cheltuiala["tip"]


def toString(cheltuiala):
    return "Id: {}, Nr_apartament: {}, Suma: {}, Data: {}, Tip: {}".format(
        getId(cheltuiala),
        getNr_apartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala),

    )
