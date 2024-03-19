def count_sorted_vowel_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    def backtrack(current_str, length):
        if length == 0:
            return 1
        count = 0
        for vowel in vowels:
            if not current_str or vowel >= current_str[-1]:
                count += backtrack(current_str + vowel, length - 1)
        return count
    
    return backtrack('', n)
n = int(input("enter the string:"))
print(count_sorted_vowel_strings(n))  # Output: 15
