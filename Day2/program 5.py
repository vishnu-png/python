def evaluate_expression(s):
    stack = []
    num = 0
    sign = '+'
    operators = {'+', '-', '*', '/'}

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in operators or char == ' ':
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                # Perform integer division
                stack[-1] = int(stack[-1] / num)
            num = 0
            sign = char
    if num != 0:
        if sign == '+':
            stack.append(num)
        elif sign == '-':
            stack.append(-num)
        elif sign == '*':
            stack[-1] *= num
        elif sign == '/':
            # Perform integer division
            stack[-1] = int(stack[-1] / num)

    return sum(stack)
expression = "3 + 2 * 2"
print(evaluate_expression(expression))  # Output: 7
