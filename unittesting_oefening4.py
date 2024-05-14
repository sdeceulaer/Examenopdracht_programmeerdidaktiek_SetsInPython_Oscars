import unittest
from oefening4 import willekeurigeNaam, willekeurigeNaamMetVoorkeursregeling, willekeurigeNaamMetZwarteLijst
from unittesting_namen import genomineerdenBesteActrice2024


class TestOefening4(unittest.TestCase):

    def test_oef4_nieuweversie(self):
        start = {'a', 'b', 'c'}
        controle = start.copy()
        einde5 = willekeurigeNaam(start)
        einde6 = willekeurigeNaamMetZwarteLijst(start, controle)
        einde7 = willekeurigeNaamMetVoorkeursregeling(start, controle)
        self.assertSetEqual(
            start, controle,
            'Bij het uitvoeren van de functie werd de originele versie van de set aangepast.  Controleer dat een kopie gemaakt wordt voor aanpassingen gedaan worden.'
        )

    def test_oef4a_trekking_willekeurigeNaam(self):
        # de willekeurige naam, komt zeker uit de start verzameling
        start = {'a', 'b', 'c'}
        self.assertIn(
            willekeurigeNaam(start), start,
            'Unittest oefening 4a willekeurigeNaam(verzameling): De naam die willekeurig uit de verzameling genomen wordt, moet wel in de verzameling voorkomen.  Waar komt jouw naam vandaan?'
        )

    def test_oef4a_trekking2_willekeurigeNaam(self):
        start = set()
        self.assertEqual(
            willekeurigeNaam(start), 'geen naam getrokken',
            'Unittest oefening 4a willekeurigeNaam(verzameling): Wanneer de verzameling leeg is, moet de functie de string "geen naam getrokken" teruggeven.  Controleer of de code een lege verzameling controleert en of een correcte string wordt teruggegeven.'
        )

    def test_oef4b_trekking2_willekeurigeNaamMetZwarteLijst(self):
        # controle bij een lege startverzameling
        start = set()
        zwart = {'x', 'y', 'z'}
        self.assertEquals(
            willekeurigeNaamMetZwarteLijst(start,
                                           zwart), 'geen naam getrokken',
            'Unittest oefening 4b willekeurigeNaamMetZwarteLijst(verzameling,zwart): Controleer uit welke verzameling de naam wordt gehaald.  Wanneer de verzameling leeg is, moet de functie de string "geen naam getrokken" teruggeven.  De functie willekeurigeNaam(verzameling) helpt hier ook om de juiste string te geven.'
        )

    def test_oef4b_trekking2_willekeurigeNaamMetZwarteLijst(self):
        # controle of de willekeurige naamzeker uit de start verzameling komt
        start = {'a', 'b', 'c'}
        zwart = set()
        controle = {'x', 'y', 'z'}
        self.assertIn(
            willekeurigeNaamMetZwarteLijst(start, zwart), start,
            'Unittest oefening 4b willekeurigeNaamMetZwarteLijst(verzameling,zwart): De naam die willekeurig uit de verzameling genomen wordt, moet wel in de gegeven verzameling aanwezig zijn.  Controleer uit welke verzameling de naam wordt gehaald.'
        )

    def test_oef4b_trekking3_willekeurigeNaamMetZwarteLijst(self):
        # controle of de getrokken naam niet uit de zwart lijst komt
        start = {'a', 'b'}
        zwart = {'a'}
        self.assertNotIn(
            willekeurigeNaamMetZwarteLijst(start, zwart), zwart,
            'Unittest oefening 4b willekeurigeNaamMetZwarteLijst(verzameling,zwart): De getrokken naam mag niet in de zwarte lijst staan.  Controleer of je de naam hebt getrokken uit de zwarte verzameling, de unie van beide verzamelingen of wel degelijk uit het verschil.'
        )
        zwart = {'d'}
        self.assertNotIn(
            willekeurigeNaamMetZwarteLijst(start, zwart), zwart,
            'Unittest oefening 4b willekeurigeNaamMetZwarteLijst(verzameling,zwart): De getrokken naam mag niet in de zwarte lijst staan.  Controleer of je de naam hebt getrokken uit de zwarte verzameling, de unie van beide verzamelingen of wel degelijk uit het verschil.'
        )

    def test_oef4b_trekking4_willekeurigeNaamMetZwarteLijst(self):
        # controle bij overlappende verzamelingen
        start = {'a', 'b', 'c'}
        zwart = start.copy()
        self.assertEqual(
            willekeurigeNaamMetZwarteLijst(start,
                                           zwart), 'geen naam getrokken',
            'Unittest oefening 4b willekeurigeNaamMetZwarteLijst(verzameling,zwart): Wanneer de zwarte lijst de gegeven verzameling volledig overlapt, moet de functie de string "geen naam getrokken" teruggeven.  Controleer of je de naam hebt getrokken uit de zwarte verzameling, de unie van beide verzamelingen of wel degelijk uit het verschil.  De functie willekeurigeNaam(verzameling) helpt hier ook om de juiste string te geven.'
        )

    def test_oef4c_trekking_willekeurigeNaamMetVoorkeursregeling(self):
        start = {'a'}
        voorkeur = {'a', 'x'}
        self.assertIn(
            willekeurigeNaamMetVoorkeursregeling(start, voorkeur), start,
            'Unittest oefening 4c willekeurigeNaamMetVoorkeursregeling(verzameling,voorkeur): De getrokken moet aanwezig zijn in de gegeven lijst.  Controleer of je de naam hebt getrokken uit de voorkeursverzameling, de unie van beide verzamelingen, de doorsnede of het verschil.'
        )

    def test_oef4c_trekking2_willekeurigeNaamMetVoorkeursregeling(self):
        start = {'a', 'b', 'c'}
        voorkeur = {'x'}
        self.assertNotIn(
            willekeurigeNaamMetVoorkeursregeling(start, voorkeur), voorkeur,
            'Unittest oefening 4c willekeurigeNaamMetVoorkeursregeling(verzameling,voorkeur): Controleer of je de naam hebt getrokken uit de voorkeursverzameling, de unie van beide verzamelingen, de doorsnede of het verschil.'
        )

    def test_oef4c_trekking3_willekeurigeNaamMetVoorkeursregeling(self):
        start = set()
        voorkeur = {'a', 'x'}
        self.assertEqual(
            willekeurigeNaamMetVoorkeursregeling(start, voorkeur),
            'geen naam getrokken',
            'Unittest oefening 4bc willekeurigeNaamMetVoorkeursregeling(verzameling,voorkeur): Wanneer de gegeven verzameling leeg is, kan je geen naam trekken.  De functie willekeurigeNaam helpt al met het schrijven van de melding.'
        )


if __name__ == '__main__':
    unittest.main()
