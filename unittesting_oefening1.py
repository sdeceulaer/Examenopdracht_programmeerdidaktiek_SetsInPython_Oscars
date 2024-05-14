import unittest
from oefening1 import *


class TestOefening1(unittest.TestCase):

    def test_oef1a_isSet_genomineerdenBesteActeur_v1(self):
        # controle of de variabele een set is
        self.assertTrue(
            isinstance(genomineerdenBesteActeur_v1, set),
            'GenomineerdenBesteActeur_v1 is geen Python set.  Controleer je syntax: heb je accolades gebruikt?'
        )

    def test_oef1a_set_genomineerdenBesteActeur_v1(self):
        # controle of de set overeenkomt met gewenste set
        correcteSet = {
            'Cillian Murphy', 'Bradley Cooper', 'Colman Domingo',
            'Paul Giamatti', 'Jonathan Mayors', 'Jeffrey Wright'
        }
        self.assertSetEqual(
            genomineerdenBesteActeur_v1, correcteSet,
            "De set komt niet overeen met de gegevens.  Controleer of je op de juiste plaats komma's en quotes hebt gebruikt bij het aanmaken, of dat je deze niet aanpast verder in je code."
        )

    def test_oef1b_aanpassing_genomineerdenBesteActeur_v2(self):
        # controle of de naam Jonathan Meyers correct wordt verwijderd en een andere naam correct wordt toegevoegd
        correcteSet = {
            'Cillian Murphy', 'Bradley Cooper', 'Colman Domingo',
            'Paul Giamatti', 'Jeffrey Wright'
        }

        # controle of Jonathan Mayors wordt verwijdeerd
        self.assertNotIn(
            'Jonathan Mayors', genomineerdenBesteActeur_v2,
            'Controleer of de naam Jonathan Mayors correct wordt verwijderd uit je tweede versie van de verzameling.'
        )

        # controle of extra naam wordt toegevoegd
        controleSet = genomineerdenBesteActeur_v2.copy()
        controleSet.discard('Jonathan Meyers')
        self.assertTrue(
            controleSet.issuperset(correcteSet),
            'Controleer of je eigen naam correct werd toegevoegd.')
        self.assertTrue(
            len(correcteSet) == len(genomineerdenBesteActeur_v2) - 1,
            'Controleer of ja exact een extra naam hebt toegevoegd.')


if __name__ == '__main__':
    unittest.main()
