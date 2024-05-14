# OEFENING 2: verzameling van genomineerde actrices voor het jaar 2024, met controles op namen
#####################################################################

from namen import genomineerdenBesteActrice2024

# De genomineerde actrices voor de Oscar van beste actrice in 2024 zijn beschikbaar in de variabele genomineerdenBesteActrice2024
print(
    "De verzameling genomineerden voor de Oscar van beste actrice in 2024 is: ",
    *genomineerdenBesteActrice2024,
    sep="\n")

# Oefening 2A
# De organisator van de Oscars is grote fan van Julia Roberts en wil vlot kunnen checken of zij in de lijst genomineerden staat.
#
# Schrijf een functie die:
# - controleert of een gegeven naam genoteerd staat in de gegeven verzameling en daarvan bericht print.
# - een nieuwe versie van de verzameling teruggeeft, waar de naam is toegevoegd als deze ontbreekt.
# - volgens functie voorschrift: controleNaamGenomineerd (verzameling, naam)
# Voer daarna de controle uit of Julia Roberts genoteerd staat op de verzameling genomineerdenBesteActrice2024 en maak en nieuwe versie van de lijst genomineerdenBesteActrice2024_v1.

def controleNaamGenomineerd(verzameling, naam):
    nieuweVerzameling = verzameling.copy()
    if naam in nieuweVerzameling:
        print(naam, " is genoteerd in de verzameling.")
    else:
        print(naam,
              " is niet genoteerd in de verzameling, en wordt toegevoegd.")
    nieuweVerzameling.add(naam)
    return nieuweVerzameling


genomineerdenBesteActrice2024_v1 = controleNaamGenomineerd(
    genomineerdenBesteActrice2024, "Julia Roberts")

print(
    "genomineerdenBesteActrice2024_v1: De verzameling genomineerden voor de Oscar van beste actrice in 2024, inclusief Julia Roberts, is: ",
    *genomineerdenBesteActrice2024_v1,
    sep="\n")

# Oefening 2B
#
# Gezien Susan Sarandon heeft gesproken op een pro-palestijnse betoging in november, wenst de organisator van de Oscars spijtig genoeg zeker te zijn dat zij niet genomineerd wordt dit jaar.
#
# Schrijf een functie die:
# - controleert of een gegeven naam zeker niet genoteerd staat in de gegeven verzameling en daarvan bericht print.
# - een nieuwe versie van de verzameling teruggeeft, waar de naam is verwijderd als deze aanwezig was.
# - volgens functie voorschrift: controleNaamNietGenomineerd (verzameling, naam)
# Voer daarna de controle uit of Susan Sarandon genoteerd staat op de verzameling genomineerdenBesteActrice2024_v1 en maak en nieuwe versie van de lijst genomineerdenBesteActrice2024_v2.


def controleNaamNietGenomineerd(verzameling, naam):
    nieuweVerzameling = verzameling.copy()
    if naam not in nieuweVerzameling:
        print(naam, " is niet genoteerd")
    else:
        print(naam, " is genoteerd, en wordt verwijderd")
    nieuweVerzameling.discard(naam)
    return nieuweVerzameling


genomineerdenBesteActrice2024_v2 = controleNaamNietGenomineerd(
    genomineerdenBesteActrice2024_v1, "Susan Sarandon")

print(
    "genomineerdenBesteActrice2024_v2: De verzameling genomineerden voor de Oscar van beste actrice in 2024, zonder Susan Sarandon, is: ",
    *genomineerdenBesteActrice2024_v2,
    sep="\n")
