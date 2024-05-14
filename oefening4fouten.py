# oefening 4a
def willekeurigeNaam(verzameling):
    return verzameling.pop()


def willekeurigeNaam(verzameling):
    naam = verzameling.pop()
    verzameling.add(naam)
    return naam


# oefening4b
def willekeurigeNaamMetZwarteLijst(verzameling, zwarteLijst):
    nieuweVerzameling = verzameling.union(zwarteLijst)
    return willekeurigeNaam(nieuweVerzameling)


def willekeurigeNaamMetZwarteLijst(verzameling, zwarteLijst):
    nieuweVerzameling = verzameling.intersection(zwarteLijst)
    return willekeurigeNaam(nieuweVerzameling)


# Oefening 4c

def willekeurigeNaamMetVoorkeursregeling(verzameling, voorkeur):
    eersteNaam = willekeurigeNaam(verzameling)
    nieuweVerzameling = verzameling.intersection(voorkeur)
    nieuweVerzameling.add(eersteNaam)
    naam = willekeurigeNaam(nieuweVerzameling)
    return naam


def willekeurigeNaamMetVoorkeursregeling(verzameling, voorkeur):
    eersteNaam = willekeurigeNaam(verzameling)
    nieuweVerzameling = verzameling.union(voorkeur)
    nieuweVerzameling.add(eersteNaam)
    naam = willekeurigeNaam(nieuweVerzameling)
    return naam


def willekeurigeNaamMetVoorkeursregeling(verzameling, voorkeur):
    nieuweVerzameling = verzameling.intersection(voorkeur)
    naam = willekeurigeNaam(nieuweVerzameling)
    return naam
