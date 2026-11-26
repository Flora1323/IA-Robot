from robots.exceptions import ActionImpossible

try:
    raise ActionImpossible("la case (2, 2) est un obstacle")
except ActionImpossible as e:
    print(e)          # attendu : action impossible car la case (2, 2) est un obstacle
    print(e.raison)   # attendu : la case (2, 2) est un obstacle