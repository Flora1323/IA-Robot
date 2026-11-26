from robots.environnement import Grille

g = Grille(6, 6, {(2, 2), (3, 2), (3, 3)})
print(g.est_valide((0, 0)))
print(g.est_valide((2, 2)))
print(g.est_valide((6, 0)))
print(g.est_valide((-1, 3)))