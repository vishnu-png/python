def is_palindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]

print(is_palindrome(121))  
print(is_palindrome(123))  
