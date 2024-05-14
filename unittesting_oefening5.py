import unittest
from oefening5 import genereerLabels


#hulpfunctie om te testen of een string omgezet kan worden in een int
def canBeNumber(nummer):
  try:
    int(nummer)
    return True
  except ValueError:
    # Not a number
    return False


class TestOefening5(unittest.TestCase):

  def test_oef5_uniekeNummers_genereerLabels(self):
    # controle of elementen in de gegenereerde set geen nummer hergebruiken
    start = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'x', 'y', 'z'}
    evenVerzameling = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
    onevenVerzameling = {'x', 'y', 'z'}
    labels = genereerLabels(start, evenVerzameling, onevenVerzameling)
    controle = set()
    for x in labels:
      nummer = x[:x.find(" ")]
      self.assertNotIn(
          nummer, controle,
          'Controleer of de nummers op een correcte manier optellen, zodat elk nummer maar 1 keer wordt gebruikt.'
      )
      controle.add(nummer)

  def test_oef5_uniekeNamen_genereerLabels(self):
    # controle of elementen in de gegenereerde set geen naam hergebruiken
    start = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'x', 'y', 'z'}
    evenVerzameling = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
    onevenVerzameling = {'x', 'y', 'z'}
    labels = genereerLabels(start, evenVerzameling, onevenVerzameling)
    controle = set()
    for x in labels:
      naam = x[x.find(" "):].strip()
      self.assertNotIn(
          naam, controle,
          'Controleer of de verzamelingen maar 1 keer worden doorlopen, zodat elke naam maar op 1 label voorkomt.'
      )
      controle.add(naam)

  def test_oef5_labelStartMetInt_genereerLabels(self):
    # controle of elementen in de gegenereerde set starten met een nummer
    start = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'x', 'y', 'z'}
    evenVerzameling = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
    onevenVerzameling = {'x', 'y', 'z'}
    labels = genereerLabels(start, evenVerzameling, onevenVerzameling)
    for x in labels:
      nummer = x[:x.find(" ")]
      self.assertTrue(canBeNumber(nummer),
                      'Controleer of de labels starten met een nummer.')

  def test_oef5_labelMetNaamUitStartVerzameling_genereerLabels(self):
    # controle of elementen in de gegenereerde set een naam bevatten uit de startverzameling
    start = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'x', 'y', 'z'}
    evenVerzameling = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
    onevenVerzameling = {'x', 'y', 'z'}
    labels = genereerLabels(start, evenVerzameling, onevenVerzameling)
    for x in labels:
      naam = x[x.find(" "):].strip()
      self.assertIn(
          naam, start,
          'Controleer of de labels eindigen met een naam in de startverzameling.'
      )

  def test_oef5_labelEvenNummers_genereerLabels(self):
    # controle of de namen op de labels met even nummers uit de juiste verameling komen
    start = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'x', 'y', 'z'}
    evenVerzameling = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
    onevenVerzameling = {'x', 'y', 'z'}
    labels = genereerLabels(start, evenVerzameling, onevenVerzameling)
    for x in labels:
      nummer = int(x[:x.find(" ")])
      tekst = x[x.find(" "):].strip()
      if nummer % 2 == 0:
        self.assertIn(
            tekst, evenVerzameling,
            'Controleer of op de juiste manier een even nummer wordt gegenereerd, voor de namen uit de verzameling voor even nummers. Wat is het kleinst mogelijke even nummer?  Hoe bereken je het volgende even nummer?'
        )
      else:
        self.assertIn(
            tekst, onevenVerzameling,
            'Controleer of op de juiste manier een oneven nummer wordt gegenereerd, voor de namen uit de verzameling voor oneven nummers. Wat is het kleinst mogelijke oneven nummer?  Hoe bereken je het volgende oneven nummer?'
        )

  # door de eigenschappen van de set, is het moeilijk om de output van de functie exact te controleren.


if __name__ == '__main__':
  unittest.main()
