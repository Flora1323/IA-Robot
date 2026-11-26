from robots.environnement import Materiau, Robot, EtatMateriau, Grille, deplacer, charger
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

m1 = Materiau("M1", "Bois", 4, (1, 3))

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