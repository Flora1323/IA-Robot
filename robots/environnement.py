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


class Grille:
    def __init__(self, nb_lignes: int, nb_colonnes: int, obstacles: set[Case]):
        # TODO : stocker les trois attributs
        pass

    def est_valide(self, case: Case) -> bool:
        """True si la case est dans la grille ET n'est pas un obstacle."""
        # TODO
        pass


def distance_manhattan(a: Case, b: Case) -> int:
    # TODO
    pass


def deplacer(robot: Robot, destination: Case, grille: Grille) -> None:
    """Déplace le robot d'une case orthogonale.
    Lève ActionImpossible si : destination invalide, ou distance != 1.
    """
    # TODO
    pass


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