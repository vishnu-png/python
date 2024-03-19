def is_valid_number(s):
    # Define states
    states = [
        {'digit': 1, 'sign': 2, 'dot': 3},
        {'digit': 1, 'dot': 4, 'exp': 5},
        {'digit': 1, 'dot': 3},
        {'digit': 6},
        {'digit': 6, 'exp': 5},
        {'sign': 7, 'digit': 8},
        {'digit': 8},
        {'digit': 8},
        {'digit': 8}
    ]
    
    # Define transitions
    transitions = {
        0: {'sign': 2, 'digit': 1, 'dot': 3},
        1: {'digit': 1, 'dot': 4, 'exp': 5},
        2: {'digit': 1, 'dot': 3},
        3: {'digit': 6},
        4: {'digit': 6, 'exp': 5},
        5: {'sign': 7, 'digit': 8},
        6: {'digit': 6, 'exp': 5},
        7: {'digit': 8},
        8: {'digit': 8}
    }
    
    state = 0
    
    for char in s:
        if char.isdigit():
            char_type = 'digit'
        elif char in ['+', '-']:
            char_type = 'sign'
        elif char == '.':
            char_type = 'dot'
        elif char in ['e', 'E']:
            char_type = 'exp'
        else:
            return False
        
        if char_type not in transitions[state]:
            return False
        state = transitions[state][char_type]
    
    return state in {1, 4, 6, 8}

# Example usage:
print(is_valid_number("0"))       
print(is_valid_number(" 0.1"))      
print(is_valid_number("abc"))      
print(is_valid_number("1 a"))       
print(is_valid_number("2e10"))     
print(is_valid_number(" -90e3"))    
print(is_valid_number("1e"))        
print(is_valid_number("e3"))      
print(is_valid_number("6e-1"))     
print(is_valid_number("99e2.5"))    
print(is_valid_number("53.5e93"))  
print(is_valid_number("--6"))       
print(is_valid_number("-+3"))       
print(is_valid_number("95a54e53"))  
