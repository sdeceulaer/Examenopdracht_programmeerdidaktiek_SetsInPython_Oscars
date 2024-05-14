import unittest
from oefening3 import controleVerzamelingTeKort, controleVerzamelingTeLang, genomineerdenBesteActrice2024_v3, genomineerdenBesteActrice2024_v4
from namen import genomineerdenBesteActrice2024


class TestOefening3(unittest.TestCase):

  def test_oef3_nieuweversie(self):
    start = {'a', 'b', 'c'}
    controle = start.copy()
    einde3 = controleVerzamelingTeLang(start, 2)
    einde4 = controleVerzamelingTeKort(start, 2, controle)
    self.assertSetEqual(
        start, controle,
        'Bij het uitvoeren van de functie werd de originele versie van de set aangepast.  Controleer dat een kopie gemaakt wordt voor aanpassingen gedaan worden.'
    )

  def test_oef3a_correcteLengte_controleVerzamelingTeLang(self):
    # controle of de resulterende verzameling de correcte lengte heeft, wanneer het origineel ook de correcte lengte heeft.
    aantal = 3
    start = {'a', 'b', 'c'}
    einde = controleVerzamelingTeLang(start, aantal)
    self.assertSetEqual(
        einde, start,
        'Unittest oefening 3a controleVerzamelingTeLang (verzameling,lengte):         Bij een verzameling met de juiste lengte, moet de nieuwe versie overeenkomen met het origineel.  Controleer goed hoe de lengte wordt gecontroleerd en of er bij een correcte lengte wijzigingen worden uitgevoerd.'
    )

  def test_oef3a_telang_controleVerzamelingTeLang(self):
    # controle of niet te veel of te weinig elementen uit de originele verzameling worden verwijderd.
    aantal = 2
    start = {'a', 'b', 'c'}
    einde = controleVerzamelingTeLang(start, aantal)
    self.assertEqual(
        len(einde), aantal,
        'Unittest oefening 3a controleVerzamelingTeLang (verzameling,lengte): De lengte van de nieuwe set, moet gelijk zijn aan de gewenste lengte.  Controleer hoe de lengte wordt gecontroleerd voor gestart wordt met verwijderen, en hoeveel keer dan een element wordt verwijderd uit de set.'
    )

  def test_oef3a_telang2_controleVerzamelingTeLang(self):
    # controle of de nieuwe verzameling ontstaat uit de originele.
    aantal = 2
    start = {'a', 'b', 'c'}
    einde = controleVerzamelingTeLang(start, aantal)
    self.assertTrue(
        start.issuperset(einde),
        'Unittest oefening 3a controleVerzamelingTeLang (verzameling,lengte): Bij een verzameling die te lang is, moet een element worden verwijderd.  Het resultaat is een deelverzameling van het origineel.  Controleer goed hoe de lengte wordt gecontroleerd.'
    )

  def test_oef3a_tekort_controleVerzamelingTeLang(self):
    # controle of te korte verzamelingen met rust worden gelaten.
    aantal = 4
    start = {'a', 'b', 'c'}
    einde = controleVerzamelingTeLang(start, aantal)
    self.assertSetEqual(
        start, einde,
        'Unittest oefening 3a controleVerzamelingTeLang (verzameling,lengte): Bij een verzameling die te kort is, hoeft niets te gebeuren.  Controleer goed hoe de lengte wordt gecontroleerd.'
    )

  def test_oef3b_correcteLengte_controleVerzamelingTeKort(self):
    # controle of verzamelingen met correcte lengte of te lang, met rust worden gelaten.
    aantal = 3
    start = {'a', 'b', 'c'}
    reserve = {'x', 'y', 'z'}
    einde = controleVerzamelingTeKort(start, aantal, reserve)
    self.assertSetEqual(
        einde, start,
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Bij een verzameling met de juiste lengte, hoeft er niets te gebeuren en zal de nieuwe versie overeenkomen met het origineel.  Controleer goed hoe de lengte wordt gecontroleerd.'
    )
    aantal = 2
    einde = controleVerzamelingTeKort(start, aantal, reserve)
    self.assertSetEqual(
        einde, start,
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Bij een verzameling die te lang is, hoeft er niets te gebeuren en zal de nieuwe versie overeenkomen met het origineel.  Controleer goed hoe de lengte wordt gecontroleerd.'
    )

  def test_oef3b_tekort_controleVerzamelingTeKort(self):
    # controle of in een te korte verzameling zeker eerst de naam Susan Sarandon wordt toegevoegd.
    aantal = 4
    start = {'a', 'b', 'c'}
    reserve = {'x', 'y', 'z'}
    einde = controleVerzamelingTeKort(start, aantal, reserve)
    self.assertIn(
        'Susan Sarandon', einde,
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Bij een verzameling die te kort is, moet eerst het element "Susan Sarandon" worden toegevoegd.  Controleer goed hoe de lengte wordt gecontroleerd en wanneer "Susan Sarandon" wordt toegevoegd.'
    )

  def test_oef3b_tekort2_controleVerzamelingTeKort(self):
    # controle van lengte bij een te korte verzameling, en ruim voldoende elementen in de reserve
    aantal = 6
    start = {'a', 'b', 'c'}
    reserve = {'x', 'y', 'z'}
    einde = controleVerzamelingTeKort(start, aantal, reserve)
    self.assertEquals(
        len(einde), aantal,
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Een verzameling die te kort is, moet aangevuld worden tot de gewenste lengte.  Controleer goed hoe de lengte wordt gecontroleerd en hoeveel elementen er na "Susan Sarandon" worden toegevoegd.'
    )

  def test_oef3b_tekort3_controleVerzamelingTeKort(self):
    # controle van een te korte verzameling, met een te korte reserve verzameling.
    aantal = 7
    start = {'a', 'b', 'c'}
    reserve = {'x', 'y'}
    controle = {'a', 'b', 'c', 'x', 'y', 'Susan Sarandon'}
    einde = controleVerzamelingTeKort(start, aantal, reserve)
    self.assertSetEqual(
        einde, controle,
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Bij een verzameling die te kort is, moet eerst het element "Susan Sarandon" worden toegevoegd en daarna elementen uit de reserve verzameling.  Houd zeker rekening met een reserve verzameling die te weinig elementen bevat om tot het gewenste aantal te komen.'
    )

  def test_oef3b_tekort4_controleVerzamelingTeKort(self):
    # controle van een te korte verzameling, met een te korte reserve verzameling wanneer rekening gehouden wordt met overlapping .
    aantal = 7
    start = {'a', 'b', 'c'}
    reserve = {'x', 'y', 'a', 'b', 'c'}
    controle = {'a', 'b', 'c', 'x', 'y', 'Susan Sarandon'}
    einde = controleVerzamelingTeKort(start, aantal, reserve)
    self.assertSetEqual(
        einde, controle,
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Bij een verzameling die te kort is, moet eerst het element "Susan Sarandon" worden toegevoegd en daarna elementen uit de reserve verzameling.  Houd zeker rekening met een reserve verzameling die te weinig elementen bevat omdat er zo veel dubbels zijn met de originele lijst.'
    )

  def test_oef3c_tekort4_controleVerzamelingTeKort(self):
    # Controle of de resulterende verzameling een superset is van de originele en of elk element dat werd toegevoegd (uitgezonderd Susan Sarandon) uit de reserve lijst komt
    aantal = 7
    start = {'a', 'b', 'c', 'Susan Sarandon'}
    reserve = {'x', 'y', 'z'}
    einde = controleVerzamelingTeKort(start, aantal, reserve)
    reserve = {'x', 'y', 'z'}
    self.assertTrue(
        einde.issuperset(start),
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Bij het aanvullen van een te korte verzameling, is de originele verzameling een deelverzameling van de resterende verzameling. Controleer in welke verzameling de elementen worden toegevoegd.'
    )
    self.assertTrue(
        reserve.issuperset(einde.difference(start)),
        'Unittest oefening 3b controleVerzamelingTeKort(verzameling,lengte,reserve): Bij het aanvullen van een te grote verzameling, komen na het toevoegen van "Susan Sarandon" alle elementen die extra worden toegevoegd uit de reserve verzameling. Controleer vanuit welke verzameling de elementen worden toegevoegd.'
    )

  def test_oef3a_controleuitvoering(self):
    self.assertSetEqual(
        genomineerdenBesteActrice2024_v3,
        controleVerzamelingTeLang(genomineerdenBesteActrice2024, 5),
        'Unittest oefening 3a uitvoering: Controleer of de test uitgevoerd wordt met de juiste verzamelingen.'
    )

  def test_oef3a_controleuitvoering(self):
    reserveGenomineerdenBesteActrice = {
        'Michelle Yeoh', 'Cate Blanchett', 'Ana de Armas',
        'Andrea Riseborough', 'Michelle William'
    }
    self.assertSetEqual(
        genomineerdenBesteActrice2024_v4,
        controleVerzamelingTeKort(genomineerdenBesteActrice2024_v3, 5,
                                  reserveGenomineerdenBesteActrice),
        'Unittest oefening 3b uitvoering: Controleer of de test uitgevoerd wordt met de juiste verzamelingen.'
    )


if __name__ == '__main__':
  unittest.main()
