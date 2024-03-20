def is_mirror_number(number):
    reverse_number = number[::-1] 
    return number == reverse_number
number = "12321"
if is_mirror_number(number):
    print("The number is a mirror number.")
else:
    print("The number is not a mirror number.")
