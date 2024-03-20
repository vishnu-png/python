import itertools

def find_combinations(digits):
    return list(itertools.permutations(digits, 3))

digits = input("Enter 3 digits separated by spaces: ").split()
combinations = find_combinations(digits)
print("All possible combinations:", combinations)
