# oefening 3A
def controleVerzamelingTeLang(verzameling, lengte):
    if len(verzameling) > lengte:
        print('De gegeven verzameling bevat ', len(verzameling),
              ' namen, dat zijn ',
              len(verzameling) - lengte,
              ' namen te veel. Volgende namen worden verwijderd')
        while len(verzameling) > lengte:
            print(verzameling.pop())
    return verzameling


def controleVerzamelingTeLang(verzameling, lengte):
    nieuweVerzameling = verzameling.copy()
    if len(nieuweVerzameling) >= lengte:
        print('De gegeven verzameling bevat ', len(nieuweVerzameling),
              ' namen, dat zijn ',
              len(nieuweVerzameling) - lengte,
              ' namen te veel. Volgende namen worden verwijderd')
        while len(nieuweVerzameling) >= lengte:
            print(nieuweVerzameling.pop())
    return nieuweVerzameling


# oefening 3B
def controleVerzamelingTeKort(verzameling, lengte, reserve):
    if len(verzameling) < lengte:
        verzameling.add('Susan Sarandon')
        print('De gegeven verzameling bevat ', len(verzameling),
              ' namen, dat zijn ', lengte - len(verzameling),
              ' namen te weinig. Volgende namen worden toegevoegd')
        while len(verzameling) < lengte and len(reserve) > 0:
            naam = reserve.pop()
            verzameling.add(naam)
            print(naam)
    return verzameling


def controleVerzamelingTeKort(verzameling, lengte, reserve):
    nieuweVerzameling = verzameling.copy()
    if len(nieuweVerzameling) < lengte:
        nieuweVerzameling.add('Susan Sarandon')
        print('De gegeven verzameling bevat ', len(nieuweVerzameling),
              ' namen, dat zijn ', lengte - len(nieuweVerzameling),
              ' namen te weinig. Volgende namen worden toegevoegd')
        while len(nieuweVerzameling) < lengte:
            naam = reserve.pop()
            nieuweVerzameling.add(naam)
            print(naam)
    return nieuweVerzameling
