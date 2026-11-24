Aborescence du projet : 

IA-ROBOT/
├── README.md                  # instructions d'installation et de lancement
├── main.py                    # point d'entrée : lance la simulation nominale
├── robots/
│   ├── __init__.py
│   ├── exceptions.py          # ActionImpossible -> exception que l'on va appeler pour éviter les répétitions
│   ├── environnement.py       # Étape 1 : EtatMateriau, Materiau, Robot, Grille + deplacer/charger/decharger
│   ├── astar.py               # Étape 2 : recherche de chemin A*
│   ├── csp.py                 # Étape 3 : CSP + backtracking
│   ├── logique.py             # Étape 4 : faits, règles, inférence
│   ├── sma.py                 # Étape 5 : intentions, priorité, détection de blocage
│   └── simulation.py          # Étape 6 : boucle d'intégration
├── tests/
│   ├── test_environnement.py
│   ├── test_astar.py          # T1
│   ├── test_csp.py            # T2
│   ├── test_logique.py        # T3
│   ├── test_sma.py            # T4
│   └── test_integration.py    # T5
└── docs/
    └── rapport.md             # brouillon du rapport et de la soutenance