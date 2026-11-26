from robots.csp import resoudre_csp

POIDS = {
    "M1": 4,
    "M2": 6,
    "M3": 3,
    "M4": 5
}

CAPACITES = {
    "R1": 10,
    "R2": 8
}

def calculer_charges(solution, poids):
    """
    Calcule la charge totale de chaque robot.
    """

    charges = {
        "R1": 0,
        "R2": 0
    }

    for materiau, robot in solution.items():
        charges[robot] = charges[robot] + poids[materiau]

    return charges

def test_poids_nominaux():

    solution = resoudre_csp(POIDS, CAPACITES)

    assert solution is not None

    assert len(solution) == len(POIDS)

    for materiau in POIDS:
        assert materiau in solution

    charges = calculer_charges(solution, POIDS)

    assert charges["R1"] <= CAPACITES["R1"]
    assert charges["R2"] <= CAPACITES["R2"]

def test_m2_7kg_insoluble():

    poids_modifies = POIDS.copy()

    poids_modifies["M2"] = 7

    solution = resoudre_csp(poids_modifies, CAPACITES)

    # Le poids total est 19 kg,
    # mais les deux robots peuvent transporter seulement 18 kg.
    # Donc aucune solution ne doit exister.
    assert solution is None