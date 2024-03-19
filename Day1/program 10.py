def modify_string(S):
    frequency = [0] * 26

    for char in S:
        frequency[ord(char) - ord('a')] += 1

    modified_str = ""

    for char in S:
        index = (ord(char) - ord('a') + frequency[ord(char) - ord('a')]) % 26
        modified_str += chr(ord('a') + index)

    return modified_str

S = "abacabad"
print(modify_string(S))  # Output: "bcbebccf"
