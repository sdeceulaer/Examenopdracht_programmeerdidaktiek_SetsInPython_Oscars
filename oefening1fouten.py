# Oefening 1A

genomineerdenBesteActeur_v1 = {
    'Cillian Murphy', 'Bradley Cooper', 'Colman Domingo', 'Paul Giamatti',
    'Jonathan Mayors Jeffrey Wright'
}
print("v1: De genomineerden voor de Oscar van beste acteur zijn: ",
      *genomineerdenBesteActeur_v1,
      sep="\n")

# Oefening 1B
genomineerdenBesteActeur_v2 = genomineerdenBesteActeur_v1.copy()
genomineerdenBesteActeur_v2.remove('Jonatha Mayors')
print(*genomineerdenBesteActeur_v1, sep="\n")
print(
    "v2: De genomineerden, zonder strafblad, voor de Oscar van beste acteur zijn: ",
    *genomineerdenBesteActeur_v2,
    sep="\n")

# Oefening 1B
genomineerdenBesteActeur_v2 = genomineerdenBesteActeur_v1.copy()
genomineerdenBesteActeur_v2.add('Brad Pitt')
print(*genomineerdenBesteActeur_v1, sep="\n")
print(
    "v2: De genomineerden, zonder strafblad, voor de Oscar van beste acteur zijn: ",
    *genomineerdenBesteActeur_v2,
    sep="\n")
