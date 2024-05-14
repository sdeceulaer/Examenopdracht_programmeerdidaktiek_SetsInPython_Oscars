# OEFENING 3: verzameling van genomineerde actrices voor het jaar 2024, met controles op lengte
###############################################################################################

from namen import genomineerdenBesteActrice2024

# De genomineerde actrices voor de Oscar van beste actrice in 2024 zijn beschikbaar in de variabele genomineerdenBesteActrice2024
print(
    "De verzameling genomineerden voor de Oscar van beste actrice in 2024 is: ",
    *genomineerdenBesteActrice2024,
    sep="\n")

# Oefening 3A
#
# Traditioneel worden er 5 namen genomineerd. Wanneer er te veel namen zijn, zal het lot beslissen welke naam verwijderd wordt.
#
# Schrijf een functie die:
# - controleert of een gegeven verzameling niet meer dan 5 namen bevat
# - een nieuwe versie van de verzameling teruggeeft, waarin bij een te grote verzameling de overtollige namen op een willekeurige manier worden verwijderd
# - volgens functie voorschrift: controleVerzamelingTeLang (verzameling,lengte)
# Voer daarna de controle uit op de verzameling genomineerdenBesteActrice2024 en maak en nieuwe versie van de verzameling genomineerdenBesteActrice2024_v3 met maximaal 5 namen.


def controleVerzamelingTeLang(verzameling, lengte):
    nieuweVerzameling = verzameling.copy()
    if len(nieuweVerzameling) > lengte:
        print('De gegeven verzameling bevat ', len(nieuweVerzameling),
              ' namen, dat zijn ',
              len(nieuweVerzameling) - lengte,
              ' namen te veel. Volgende namen worden verwijderd')
        while len(nieuweVerzameling) > lengte:
            print(nieuweVerzameling.pop())
    return nieuweVerzameling


genomineerdenBesteActrice2024_v3 = controleVerzamelingTeLang(
    genomineerdenBesteActrice2024, 5)

print(
    "genomineerdenBesteActrice2024_v3: genomineerdenBesteActrice2024_v3: De verzameling genomineerden voor de Oscar van beste actrice in 2024 is: ",
    *genomineerdenBesteActrice2024_v3,
    sep="\n")

# Oefening 3B
#
# Schrijf een extra functie die:
# - controleert of een gegeven verzameling een gewenste lengte heeft
# - als de verzameling te kort is
# --- voeg je uit protest eerst de naam 'Susan Sarandon' toe
# --- vul je willekeurige namen toe uit de reservelijst
# - volgens functie voorschrift: controleVerzamelingTeKort (verzameling,lengte,reserve)
# Voer daarna de controle uit op de verzameling genomineerdenBesteActrice2024_v3. Maak en nieuwe versie van de verzameling genomineerdenBesteActrice2024_v4 met een gewenste lengte met 5 namen, waarbij je gebruik kan maken van een reserveverzameling met deze namen: Michelle Yeoh, Cate Blanchett, Ana de Armas, Andrea Riseborough en Michelle Williams.


def controleVerzamelingTeKort(verzameling, lengte, reserve):
    nieuweVerzameling = verzameling.copy()
    if len(nieuweVerzameling) < lengte:
        nieuweVerzameling.add('Susan Sarandon')
        print('De gegeven verzameling bevat ', len(nieuweVerzameling),
              ' namen, dat zijn ', lengte - len(nieuweVerzameling),
              ' namen te weinig. Volgende namen worden toegevoegd')
        while len(nieuweVerzameling) < lengte and len(reserve) > 0:
            naam = reserve.pop()
            nieuweVerzameling.add(naam)
            print(naam)
    return nieuweVerzameling


reserveGenomineerdenBesteActrice = {
    'Michelle Yeoh', 'Cate Blanchett', 'Ana de Armas', 'Andrea Riseborough',
    'Michelle William'
}
genomineerdenBesteActrice2024_v4 = controleVerzamelingTeKort(
    genomineerdenBesteActrice2024_v3, 5, reserveGenomineerdenBesteActrice)
print(
    "genomineerdenBesteActrice2024_v4: De verzameling genomineerden voor de Oscar van beste actrice in 2024 is: ",
    *genomineerdenBesteActrice2024_v4,
    sep="\n")
