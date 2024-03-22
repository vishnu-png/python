def isPalindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())

    return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output: True
