# OEFENING 5: maak voor elke naam in een verzameling een persoonlijke sticker
#############################################################################

# De Oscar uitreiking is een belangrijk event, dat goed georganiseerd moet verlopen.  Van het regelen van de parking en de sleutels, tot de vestiaire en de tafelzitting.
# Daarvoor worden stickers gedrukt, met een nummer en een naam, die overal gebruikt worden: op de parkeerplaats van de auto, het haakje voor de autosleutel, het haakje in de vestiaire.
#
# Schrijf een functie die:
#- een nieuwe Python set aanmaakt met strings
#- de string is als volgt opgebouwd: een volgnummer, gevolgd door een spatie en daarna de naam van de acteur of actrice.
#- de toekenning van de nummers is willekeurig, maar wel uniek.
#- actrices krijgen even nummers en acteurs krijgen oneven nummers.
# - met functie voorschrift: genereerLabels (verzameling, deelverzamelingEven, deelverzamelingOneven)

from namen import genomineerden10Jaar, acteurs, actrices


def genereerLabels(verzameling, deelverzamelingEven, deelverzamelingOneven):
  labels = set()
  getalOneven = 1
  getalEven = 2
  for x in verzameling:
    if x in deelverzamelingEven:
      labels.add(str(getalEven) + " " + x)
      getalEven += 2
    else:
      labels.add(str(getalOneven) + " " + x)
      getalOneven += 2
  return labels
