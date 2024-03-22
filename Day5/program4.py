def can_divide(prod, summation):
    if prod % summation == 0:
        return "YEAH"
    else:
        return "NAH"

test_cases = int(input("Enter the number of test cases: "))

for _ in range(test_cases):
    prod, summation = map(int, input("Enter the product and sum separated by space: ").split())
    print(can_divide(prod, summation))
