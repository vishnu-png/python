import itertools

def generate_combinations(digits):
    if not digits:
        return []

    num_to_letters = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }

    letters_list = [num_to_letters[d] for d in digits]

    combinations = [''.join(comb) for comb in itertools.product(*letters_list)]

    return combinations

input_digits = '25'
output_combinations = generate_combinations(input_digits)
for combination in output_combinations:
    print(combination)
