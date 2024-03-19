def max_guests_within_T_hours(E, L, T):
    max_guests = 0
    current_guests = 0

    for i in range(T):
        # Update the number of guests
        current_guests += E[i] - L[i]
        # Update the maximum number of guests
        max_guests = max(max_guests, current_guests)

    return max_guests

E = [10, 20, 15, 25]
L = [5, 10, 15, 20]
T = len(E)
print(max_guests_within_T_hours(E, L, T)) 
