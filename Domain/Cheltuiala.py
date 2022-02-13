
def creeazaCheltuiala(id, nr_apartament, suma, data, tip):
    return [str(id), nr_apartament, suma, data, str(tip)]

def getId(cheltuiala):
    return cheltuiala[0]

def getNr_apartament(cheltuiala):
    return cheltuiala[1]

def getSuma(cheltuiala):
    return cheltuiala[2]

def getData(cheltuiala):
    return cheltuiala[3]

def getTip(cheltuiala):
    return cheltuiala[4]

def toString(cheltuiala):
    return "Id: {}, Nr_apartament: {}, Suma: {}, Data: {}, Tip: {}".format(
        getId(cheltuiala),
        getNr_apartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala),

    )
#id, nr_apartament, suma, data, tip