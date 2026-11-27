from robots.environnement import Materiau, Robot, EtatMateriau, Grille, deplacer, charger, decharger, afficher
from robots.exceptions import ActionImpossible

#---- TEST 1 ----#

#m1 = Materiau("M1", "Bois", 4, (1, 3))
#r1 = Robot("R1", 10, (1, 0), (5, 4))
#print(m1)
#print(r1)

#---- TEST 2 ----#

#g = Grille(6, 6, {(2, 2), (3, 2), (3, 3)})
#print(g.est_valide((0, 0)))
#print(g.est_valide((2, 2)))
#print(g.est_valide((6, 0)))
#print(g.est_valide((-1, 3)))

#---- TEST 3 ----#

"""g = Grille(6, 6, {(2, 2), (3, 2), (3, 3)})
r1 = Robot("R1", 10, (1, 0), (5, 4))

deplacer(r1, (1, 1), g)
print(r1.position)            # à prédire

for dest in [(2, 2), (6, 1), (1, 3)]:
    try:
        deplacer(r1, dest, g)
    except ActionImpossible as e:
        print(e)
 """
        
#---- TEST 4 ----#

"""m1 = Materiau("M1", "Bois", 4, (1, 3))

r1 = Robot("R1", 10, (1, 3), (5, 4))
charger(r1, m1)
print(r1.charge, r1.materiaux_portes, m1.etat)

# déjà transporté : refus attendu
try:
    charger(r1, m1)
except ActionImpossible as e:
    print(e)

# mauvaise case
m3 = Materiau("M3", "Plastique", 3, (4, 1))
try:
    charger(r1, m3)
except ActionImpossible as e:
    print(e)

# capacité dépassée : 8 + 4 > 10
r1b = Robot("R1", 10, (1, 3), (5, 4), charge=8)
m1b = Materiau("M1", "Bois", 4, (1, 3))
try:
    charger(r1b, m1b)
except ActionImpossible as e:
    print(e)
"""

#---- TEST 5 ----#
"""
# Création des matériaux
m1 = Materiau("M1", "Bois", 4, (1, 3))
m2 = Materiau("M2", "Métal", 3, (1, 3))

# Création du robot
r1 = Robot("R1", 10, (5, 4), (5, 4))

# Le robot charge les deux matériaux
# On le place directement sur la case des matériaux
r1.position = (1, 3)

charger(r1, m1)
charger(r1, m2)

print("Avant déchargement :")
print(r1.charge)             # 7
print(r1.materiaux_portes)   # M1 et M2

# Le robot se déplace jusqu'à son dépôt
r1.position = r1.depot

# Déchargement
decharger(r1)

print("Après déchargement :")
print(r1.charge)             # 0
print(r1.materiaux_portes)   # []
print(m1.etat)               # EtatMateriau.LIVRE
print(m2.etat)               # EtatMateriau.LIVRE
print(m1.position)           # (5, 4)
print(m2.position)           # (5, 4)


# TEST : robot pas sur son dépôt
r2 = Robot("R2", 10, (1, 1), (5, 4))

try:
    decharger(r2)
except ActionImpossible as e:
    print("Erreur attendue :", e)


# TEST : rien à décharger
r3 = Robot("R3", 10, (5, 4), (5, 4))

try:
    decharger(r3)
except ActionImpossible as e:
    print("Erreur attendue :", e)
"""

#---- TEST 6 ----#

g = Grille(6, 6, {(2, 2), (3, 2), (3, 3)})
robots = [Robot("R1", 10, (1, 0), (5, 4)), Robot("R2", 8, (4, 0), (5, 5))]
materiaux = [
    Materiau("M1", "Bois", 4, (1, 3)),
    Materiau("M2", "Acier", 6, (1, 5)),
    Materiau("M3", "Plastique", 3, (4, 1)),
    Materiau("M4", "Aluminium", 5, (4, 4)),
]
afficher(g, robots, materiaux)
# afficher(g, robots[::-1], materiaux[::-1]) - l'inverse fonctionne aussi


