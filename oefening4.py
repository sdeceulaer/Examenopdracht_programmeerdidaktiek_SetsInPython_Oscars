# OEFENING 4: trek willekeurige (of toch bijna) namen uit de verzamelingen genomineerden
###############################################################################################

from namen import genomineerdenBesteActrice2024, genomineerdenBesteActeur2024

# Oefening 4a
#
# Wanneer er geen winnaar kan gekozen worden uit de verzameling met genomineerden, laat men het lot beslissen.
#
# Schrijf een functie die:
# - uit een gegeven verzameling 1 willekeurige naam kiest en deze teruggeeft.
# - zorg ervoor dat de originele verzameling niet wijzigt
# - zorg ervoor dat er een melding teruggegeven wordt 'geen naam getrokken' wanneer geen naam genomen kan worden.
# - met functie voorschrift: willekeurigeNaam(verzameling)
# Laat je functie daarna een willekeurige naam kiezen uit de verzameling genomineerdenBesteActrice2024 en uit genomineerdenBesteActeur2024 en schrijf deze naar willekeurigeNaamBesteActrice2024 en willekeurigeNaamBesteActeur2024.


def willekeurigeNaam(verzameling):
    if len(verzameling) > 0:
        naam = verzameling.pop()
        verzameling.add(naam)
    else:
        naam = 'geen naam getrokken'
    return naam


willekeurigeNaamBesteActrice2024 = willekeurigeNaam(
    genomineerdenBesteActrice2024)
willekeurigeNaamBesteActeur2024 = willekeurigeNaam(
    genomineerdenBesteActeur2024)

print(
    "willekeurigeNaamBesteActrice2024 en willekeurigeNaamBesteActeur2024: De willekeurige gekozen namen uit de genomineerden voor Beste Acteur en Beste Actrice zijn: ",
    willekeurigeNaamBesteActrice2024, " en ", willekeurigeNaamBesteActeur2024,
    ".")

# Oefening 4b
#
# Zoals je al wel gezien hebt, is het belangrijk rekening te houden met namen die niet gebruikt kunnen worden, zoals Susan Sarandon en Jonathan Mayors.  Er bestaat dus een zogenaamde zwarte lijst.
#
# Schrijf een functie die:
# - een willekeurige naam teruggeeft uit een gegeven verzameling, maar rekening houdt met de meegegeven verzameling met zwarte namen.
# - met functie voorschrift: willekeurigeNaamMetZwarteLijst(verzameling, zwartelijst)


def willekeurigeNaamMetZwarteLijst(verzameling, zwarteLijst):
    nieuweVerzameling = verzameling.difference(zwarteLijst)
    return willekeurigeNaam(nieuweVerzameling)


# oefening 4c
#
# Zoals je al wel gezien hebt, is de organisator niet helemaal onpartijdig.  Hij wil bij de willekeurige trekking van namen, toch een voorkeursregeling opstellen.
#
# De voorkeursregeling werkt als volgt:
# - Uit de gegeven verzameling wordt een eerste willekeurige naam gekozen.  Maar de uiteindelijke naam wordt willekeurig gekozen uit de verzameling van namen die zowel in de gegeven verzameling vermeld staan als in de voorkeursverzameling, en aangevuld met de eerste willekeurige naam.
# Schrijf een functie die:
# - een willekeurige naam teruggeeft uit een gegeven verzameling volgens de voorkeursregeling hierboven beschreven, met een voorkeursverzameling.
# - met functie voorschrift: willekeurigeNaamMetVoorkeursregeling(verzameling, voorkeur)
# Let op dat wanneer de gegeven verzameling niet leeg is, er zeker een naam getrokken kan worden.


def willekeurigeNaamMetVoorkeursregeling(verzameling, voorkeur):
    eersteNaam = willekeurigeNaam(verzameling)
    if len(verzameling) > 0:
        nieuweVerzameling = verzameling.intersection(voorkeur)
        nieuweVerzameling.add(eersteNaam)
        naam = willekeurigeNaam(nieuweVerzameling)
        return naam
    else:
        return eersteNaam


# Oefening 4d
#
# Gebruik nu de nieuwe functies om de volgende opdracht te voltooien:
#- willekeurigeWinnaarBesteActrice2024: laat het lot een winnaar kiezen voor de Oscar van beste actrice in 2024, maar zorg ervoor dat een actrice die al eens gewonnen heeft meer kans maakt.
#- willekeurigeWinnaarBesteActeur2024: laat het lot een winnaar kiezen voor de Oscar van beste acteur in 2024, maar zorg ervoor dat een acteur die is gestorven zeker niet getrokken kan worden.
# Je kan daarbij gebruik maken van de verzamelingen winnaarsBesteActeur, winnaarsBesteActrice, genomineerdenBesteActeur2024, genomineerdenBesteActrice2024, dodeActeurs

from namen import winnaarsBesteActeur, winnaarsBesteActrice, genomineerdenBesteActeur2024, genomineerdenBesteActrice2024, dodeActeurs

willekeurigeWinnaarBesteActrice2024 = willekeurigeNaamMetVoorkeursregeling(
    genomineerdenBesteActrice2024, winnaarsBesteActrice)

print("willekeurigeWinnaarBesteActrice2024: De willekeurige winnaar voor de Oscar van beste actrice in 2024 is: ",
      willekeurigeWinnaarBesteActrice2024)

willekeurigeWinnaarBesteActeur2024 = willekeurigeNaamMetZwarteLijst(
    genomineerdenBesteActeur2024, winnaarsBesteActeur)

print("willekeurigeWinnaarBesteActeur2024: De willekeurige winnaar voor de Oscar van beste acteur in 2024 is: ",
      willekeurigeWinnaarBesteActeur2024)
