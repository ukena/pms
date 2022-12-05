i = 4  # Vorgang i
t_i = 6  # Dauer für Vorgang i
j = 5  # Vorgang j
t_j = 3  # Dauer für Vorgang j

# Anfangsfolge
d_ij_min_a = 2/3 * t_i
d_ij_max_a = False

# Normalfolge
d_ij_min = False
d_ij_max = False

# Endfolge
d_ij_min_e = False
d_ij_max_e = False

# Sprungfolge
d_ij_min_s = False
d_ij_max_s = False

# Mindestabstände werden zu d_ij
# Maximalabstände werden zu d_ji

if __name__ == "__main__":
    # Anfangsfolge testen
    if d_ij_max_a:
        d_ji = -d_ij_max_a - t_j
        print(f"Anfangsfolge bei Maximalabstand d_{j}{i}={d_ji}")
    if d_ij_min_a:
        d_ij = d_ij_min_a - t_i
        print(f"Anfangsfolge bei Mindestabstand d_{i}{j}={d_ij}")
    # Normalfolge testen
    if d_ij_max:
        d_ji = -d_ij_max - t_j - t_i
        print(f"Normalfolge bei Maximalabstand d_{j}{i}={d_ji}")
    if d_ij_min:
        print(f"Normalfolge bei Mindestabstand d_{i}{j}={d_ij_min}")
    # Endfolge testen
    if d_ij_max_e:
        d_ji = -d_ij_max_e - t_i
        print(f"Endfolge bei Maximalabstand d_{j}{i}={d_ji}")
    if d_ij_min_e:
        d_ij = d_ij_min_e - t_j
        print(f"Endfolge bei Mindestabstand d_{i}{j}={d_ij}")
    # Sprungfolge testen
    if d_ij_max_s:
        d_ji = -d_ij_max_s
        print(f"Sprungfolge bei Maximalabstand d_{j}{i}={d_ji}")
    if d_ij_min_s:
        d_ij = d_ij_min_s - t_i - t_j
        print(f"Sprungfolge bei Mindestabstand d_{i}{j}={d_ij}")