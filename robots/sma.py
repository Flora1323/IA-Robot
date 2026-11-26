class Multiagents:
    def __init__(self, robots):
        # Tri des robots par identifiant (ex. "R1" < "R2") pour fixer l'ordre de priorité déterministe
        self.robots = sorted(robots, key=lambda r: r.id)
        # Compteur de pas consécutifs où aucun robot actif n'a pu avancer
        self.bloqued_steps = 0

    def collect_intentions(self):
        intentions = {}
        for robot in self.robots:
            end = len(robot.plan == 0)
            target = robot.position if end else robot.plan[0]
            intentions[robot.id] = {
                "pos": robot.position,
                "target": target,
                "end": end,
            }
        return intentions

    def resoudre_conflits(self, intentions):

        actions = {}
        occupied_cells = {info["pos"] for info in intentions.values()}

        for robot in self.robots:
            robotId = robot.id
            info = intentions[robotId]

            if info["termine"]:
                actions[robotId] = {'DONE'}
                continue

            if info["cible"] in occupied_cells:
                actions[robotId] = {'WAIT'}
                continue

            already_claimed = any(actions.get(other_id) == "MOVE" and intentions[other_id]["cible"] == info["cible"]
                for other_id in intentions
                if other_id != robotId
            )
            if already_claimed:
                actions[robotId] = "WAIT"
            else:
                actions[robotId] = "MOVE"

        return actions


    def step_execution(self, actions):

        for robot in self.robots:
            if actions[robot.id] == "MOVE" and robot.plan:
                robot.position = robot.plan.pop(0)

    def detecter_blocage(self, actions):
        actives_actions = [act for act in actions.values() if act != "DONE"]

        if actives_actions and all(act == "WAIT" for act in actives_actions):
            self.bloqued_steps += 1
        else:
            self.bloqued_steps = 0

        return self.bloqued_steps >= 2

        pass

    def generer_diagnostic(self, pas, intentions, actions):

        pass