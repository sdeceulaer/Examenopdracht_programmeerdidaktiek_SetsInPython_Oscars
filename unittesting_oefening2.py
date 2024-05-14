import unittest
from oefening2 import controleNaamGenomineerd, controleNaamNietGenomineerd, genomineerdenBesteActrice2024_v1, genomineerdenBesteActrice2024_v2
from namen import genomineerdenBesteActrice2024


class TestOefening2(unittest.TestCase):

  def test_oef2_nieuweversie(self):
    start = {'a', 'b', 'c'}
    controle = start.copy()
    einde = controleNaamGenomineerd(start, 'd')
    einde2 = controleNaamNietGenomineerd(start, 'd')
    self.assertSetEqual(
        start, controle,
        'Bij het uitvoeren van de functie werd de originele versie van de set aangepast.  Controleer dat een kopie gemaakt wordt voor aanpassingen gedaan worden.'
    )

  def test_oef2a_controle_controleNaamGenomineerd(self):
    # controle of naam wordt toegevoegd als deze niet in de verzameling staat
    start = {'a', 'b', 'c'}
    einde = controleNaamGenomineerd(start, 'd')
    controle = {'a', 'b', 'c', 'd'}
    self.assertSetEqual(
        einde, controle,
        'Unittest oefening 2a controleNaamGenomineerd(verzameling, naam): Controleer of je de te controleren naam toevoegt aan de juiste set, of dat je deze niet hebt verwijderd in plaats van toegevoegd.'
    )

  def test_oef2a_controle2_controleNaamGenomineerd(self):
    start = {'a', 'b', 'c'}
    einde = controleNaamGenomineerd(start, 'c')
    self.assertSetEqual(
        einde, start,
        'Unittest oefening 2a controleNaamGenomineerd(verzameling, naam): Controleer of je de te controleren naam toevoegt aan de juiste set, of dat je deze niet hebt verwijderd in plaats van toegevoegd.'
    )

  def test_oef2b_controle_controleNaamNietGenomineerd(self):
    # controle of naam wordt verwijderd als deze in de verzameling staat
    start = {'a', 'b', 'c'}
    einde = controleNaamNietGenomineerd(start, 'c')
    controle = {'a', 'b'}
    self.assertSetEqual(
        einde, controle,
        'Unittest oefening 2b controleNaamNietGenomineerd(verzameling, naam): Controleer of je de naam verwijdert uit de juiste set, of dat je deze niet hebt toegevoegd in plaats van verwijderd.'
    )

  def test_oef2b_controle2_controleNaamNietGenomineerd(self):
    # controle of verzameling ongewijzigd blijft als naam niet in de verzameling staat
    start = {'a', 'b', 'c'}
    einde = controleNaamNietGenomineerd(start, 'd')
    self.assertSetEqual(
        start, einde,
        'Unittest oefening 2b controleNaamNietGenomineerd(verzameling, naam): Wanneer de gegeven set de gecontroleerde waarde niet bevat, mag deze set niet wijzigen.  Controleer of je deze niet hebt toegevoegd, of een andere hebt verwijderd.'
    )

  def test_oef2a_controleuitvoering(self):
    self.assertSetEqual(
        genomineerdenBesteActrice2024_v1,
        controleNaamGenomineerd(genomineerdenBesteActrice2024,
                                "Julia Roberts"),
        'Unittest oefening 2a uitvoering: Controleer de functie in de test om Julia Roberts te nomineren, wordt uitgevoerd met de juiste verzamelingen en namen.'
    )

  def test_oef2b_controleuitvoering(self):
    self.assertSetEqual(
        genomineerdenBesteActrice2024_v2,
        controleNaamNietGenomineerd(
            controleNaamGenomineerd(genomineerdenBesteActrice2024,
                                    "Julia Roberts"), "Susan Sarandon"),
        'Unittest oefening 2b uitvoering: Controleer de functie in de test om Susan Sarandon te verwijderen wordt uitgevoerd met de juiste verzamelingen en namen.'
    )


if __name__ == '__main__':
  unittest.main()
