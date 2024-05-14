# Oefening 2A

def controleNaamGenomineerd(verzameling, naam):
    if naam in verzameling:
        print(naam, " is genoteerd")
    else:
        print(naam, " is niet genoteerd, en wordt toegevoegd")
    verzameling.add(naam)
    return verzameling



# Oefening 2B
def controleNaamNietGenomineerd(verzameling, naam):
    if naam not in verzameling:
        print(naam, " is niet genoteerd")
    else:
        print(naam, " is genoteerd, en wordt verwijderd")
    verzameling.discard(naam)
    return verzameling


genomineerdenBesteActrice2024_v2 = controleNaamNietGenomineerd(
    genomineerdenBesteActrice2024_v1, "Susan Sarandon")

#if susanSarandonGenomineerd:
#      genomineerdenBesteActrice2024_v2.remove('Susan Sarandon')

genomineerdenBesteActrice2024_v2.discard('Susan Sarandon')
print('v2', genomineerdenBesteActrice2024_v2)

# Traditioneel worden er 5 namen genomineerd. Wanneer er te veel namen zijn, zal het lot beslissen welke naam verwijderd wordt.
#
# Schrijf een functie die:
# - controleert of een gegeven verzameling niet meer dan 5 namen bevat
# - een nieuwe versie van de verzameling teruggeeft, waarin bij een te grote verzameling de overtollige namen op een lukrake manier worden verwijderd
# - volgens functie voorschrift: controleVerzamelingTeLang (verzameling,lengte)
# Voer daarna de controle uit op de verzameling genomineerdenBesteActrice2024_v2 en maak en nieuwe versie van de verzameling genomineerdenBesteActrice2024_v3 met maximaal 5 namen.



genomineerdenBesteActrice2024_v3 = controleVerzamelingTeLang(
    genomineerdenBesteActrice2024_v2, 5)

print(
    "De verzameling genomineerden voor de Oscar van beste actrice in 2024 is: ",
    *genomineerdenBesteActrice2024_v3,
    sep="\n")

# Schrijf een extra functie die:
# - controleert of een gegeven verzameling een gewenste lengte heeft
# - als de verzameling te kort is
# --- voeg je uit protest de naam 'Susan Sarandon' toe
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
    "De verzameling genomineerden voor de Oscar van beste actrice in 2024 is: ",
    *genomineerdenBesteActrice2024_v4,
    sep="\n")
