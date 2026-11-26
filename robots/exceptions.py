class ActionImpossible(Exception):
    """Levée quand une action est refusée. Message : 'action impossible car <raison>'."""

    def __init__(self, raison):
        self.raison = raison
        super().__init__("action impossible car " + raison)