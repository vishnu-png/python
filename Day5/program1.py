def lengthOfLastWord(s):
    words = s.split()
    
    if not words:
        return 0
    
    return len(words[-1])

s = "Hello World"
print(lengthOfLastWord(s))  # Output: 5
