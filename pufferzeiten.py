
# Knoten
i = 3
t_i = 4
FA_i = 2
FE_i = 6
SA_i = 4
SE_i = 8

# Mindestabstände (d = {"i_j": 1, ...])
d = {"1_2": 1, "6_2": -11, "1_3": 2}

# {j: [t_j, FA_j, FE_j, SA_j, SE_j], ...}
nachfolger = {5: [4, 8, 12, 8, 12]}
vorgänger = {1: [0, 0, 0, 0, 0]}

if __name__ == "__main__":
    # spätester Anfang - frühester Anfang
    GP_i = SA_i - FA_i
    # minimum { aller FA der Nachfolger - eventuelle Mindestabstände in d} - FE_i
    FP_i = min(nachfolger[j][1] - d.get(f"{i}_{j}", 0) for j in nachfolger.keys()) - FE_i
    # spätester Anfang - maximum { aller SA der Vorgänger + eventuelle Mindestabstände in d}
    FRP_i = SA_i - max(vorgänger[j][4] + d.get(f"{j}_{i}", 0) for j in vorgänger.keys())
    # 0 oder FP + FRP - GP
    UP_i = max(((FP_i + FRP_i - GP_i), 0))

    print(f"GP={GP_i}, FP={FP_i}, FRP={FRP_i}, UP={UP_i}")