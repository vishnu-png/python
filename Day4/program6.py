def delchar(s, c):
    if len(c) != 1:
        return s
    
    return ''.join(char for char in s if char != c)

s = "hello world"
c = "o"
print(delchar(s, c))  # Output: "hell wrld"
