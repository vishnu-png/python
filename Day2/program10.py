def remove_common_words(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    
    set1 = set(words1)
    set2 = set(words2)
    
    unique_words1 = set1 - set2
    unique_words2 = set2 - set1
    
    result1 = ' '.join(unique_words1)
    result2 = ' '.join(unique_words2)
    
    return result1, result2

S1 = input("enter the string 1:")
S2 = input("enter the string 2:")
result1, result2 = remove_common_words(S1, S2)
print("Result 1:", result1)
print("Result 2:", result2)
