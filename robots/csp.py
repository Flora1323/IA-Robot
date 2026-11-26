"""
X : une variable par matériau
D : {robots} pour chaque variable
C : pour chaque robot, somme des poids affectés <= capacité

"""

def charge_robot(robot, assignment, poids):
    """Poids total déjà affecté à `robot` dans l'affectation partielle."""
    charge_totale = 0

    for materiau, robot_assigne in assignment.items():
        if robot_assigne == robot:
            charge_totale = charge_totale + poids[materiau]

    return charge_totale


def est_consistant(materiau, robot, assignment, poids, capacites):
    """Vérifie la contrainte de capacité si on affecte `materiau` à `robot`."""
    
    nouvelle_charge = charge_robot(robot, assignment, poids) + poids[materiau]
    
    return nouvelle_charge <= capacites[robot]


def backtrack(assignment, variables, domaines, poids, capacites):
 # Cas de base : toutes les variables sont affectées -> solution
    if len(assignment) == len(variables):
        solution = assignment.copy()
        return solution

# Choix de la prochaine variable non affectée 
    var = None

    for variable in variables:
        if variable not in assignment:
            var = variable
            break

    for robot in domaines[var]:

        if est_consistant(var, robot, assignment, poids, capacites):

            assignment[var] = robot

            resultat = backtrack(
                assignment,
                variables,
                domaines,
                poids,
                capacites
            )

            if resultat is not None:
                return resultat

            del assignment[var]

    return None # aucune valeur possible : échec 

def resoudre_csp(poids, capacites):
    """
    poids     : {"M1": 4, "M2": 6, "M3": 3, "M4": 5}
    capacites : {"R1": 10, "R2": 8}

    Retourne une solution comme :
    {"M1": "R1", "M2": "R1", ...}

    Retourne None si aucune solution n'existe.
    """

    # X : liste des matériaux
    variables = list(poids.keys())

    # D : chaque matériau peut être affecté à chaque robot
    domaines = {}

    for variable in variables:
        domaines[variable] = list(capacites.keys())

    # Au début, aucun matériau n'est encore affecté
    assignment = {}

    # Lancer la recherche par Backtracking
    solution = backtrack(
        assignment,
        variables,
        domaines,
        poids,
        capacites
    )

    return solution