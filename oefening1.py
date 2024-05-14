# OEFENING 1: verzameling van genomineerde acteurs voor het jaar 2024
#####################################################################

# Oefening 1A
#
# Maak een Python set voor de genomineerden voor de Oscar voor beste acteur.
# Nomineer Cillian Murphy, Bradley Cooper, Colman Domingo, Paul Giamatti, Jonathan Mayors en Jeffrey Wright.
# variabele: genomineerdenBesteActeur_v1

genomineerdenBesteActeur_v1 = {
    'Cillian Murphy', 'Bradley Cooper', 'Colman Domingo', 'Paul Giamatti',
    'Jonathan Mayors', 'Jeffrey Wright'
}
print(
    "genomineerdenBesteActeur_v1: De genomineerden voor de Oscar van beste acteur zijn: ",
    *genomineerdenBesteActeur_v1,
    sep="\n")

# Oefening 1B
#
# Omdat Jonathan Mayors betrokken is in een rechtzaak, verliest hij zijn nominatie.
# Maak een nieuwe versie van de verzameling, waarbij Jonathan Mayors niet meer is genomineerd.
# Maak nu van de gelegenheid gebruik om een van jouw favoriete acteurs stiekem toe te voegen.
# variabele: genomineerdenBesteActeur_v2
genomineerdenBesteActeur_v2 = genomineerdenBesteActeur_v1.copy()
genomineerdenBesteActeur_v2.discard('Jonathan Mayors')
genomineerdenBesteActeur_v2.add('Brad Pitt')

print(
    "genomineerdenBesteActeur_v2: De genomineerden, zonder strafblad, voor de Oscar van beste acteur zijn: ",
    *genomineerdenBesteActeur_v2,
    sep="\n")
