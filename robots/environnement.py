from dataclasses import dataclass, field
from enum import Enum

from robots.exceptions import ActionImpossible

Case = tuple[int, int]  # (ligne, colonne), à partir de zéro


class EtatMateriau(Enum):
    AU_STOCK = 1
    TRANSPORTE = 2
    LIVRE = 3

@dataclass
class Materiau:
    id: str
    nature: str
    poids: int
    position: Case   
    etat: EtatMateriau = EtatMateriau.AU_STOCK    #AU_STOCK par défaut


@dataclass
class Robot:
    id: str
    capacite: int
    position: Case    
    depot: Case   
    charge: int = 0   #0 par défaut
    materiaux_portes: list = field(default_factory=list)   # liste vide par défaut


"""True si la case est dans la grille ET n'est pas un obstacle."""
class Grille:
    def __init__(self, nb_lignes: int, nb_colonnes: int, obstacles: set[Case]):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.obstacles = obstacles

    def est_valide(self, case: Case) -> bool:
        ligne, colonne = case
        return (0 <= ligne < self.nb_lignes
                and 0 <= colonne < self.nb_colonnes
                and case not in self.obstacles)


def distance_manhattan(a: Case, b: Case) -> int:
    ligne_a, colonne_a = a #récupère les coordonnées
    ligne_b, colonne_b = b
    
    return abs(ligne_a - ligne_b) + abs(colonne_a - colonne_b) #on utilise les valeurs absolues
    #nombre de cases à parcourir horizontalement + le nombre de cases à parcourir verticalement.

def deplacer(robot: Robot, destination: Case, grille: Grille) -> None:
    if not grille.est_valide(destination):
        raise ActionImpossible(f"la case {destination} est hors grille ou est un obstacle")
    if distance_manhattan(robot.position, destination) != 1: #avance plus de 1
        raise ActionImpossible (f"la distance {distance_manhattan(robot.position, destination)} n'est pas une distance admissible")
    robot.position = destination


def charger(robot: Robot, materiau: Materiau) -> None:
    """Le robot charge le matériau situé sur sa propre case.
    Lève ActionImpossible si : matériau pas AU_STOCK, robot pas sur sa case,
    ou charge + poids > capacité.
    Effets : charge, materiaux_portes, etat du matériau.
    """
    # TODO
    pass


def decharger(robot: Robot) -> None:
    """Le robot dépose tout ce qu'il porte, sur son dépôt.
    Lève ActionImpossible si : robot pas sur son dépôt, ou rien à décharger.
    Effets : matériaux LIVRE (position = dépôt), charge = 0, liste vidée.
    """
    # TODO
    pass


def afficher(grille: Grille, robots: list[Robot], materiaux: list[Materiau]) -> None:
    """Affichage texte : # obstacle, . case libre, R1/R2, M1..M4, D1/D2."""
    # TODO
    pass