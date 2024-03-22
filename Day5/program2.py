def calculate_bonus(salary, grade):
    bonus_percentage = 0
    if salary < 10000:
        bonus_percentage += 2
    if grade == 'A':
        bonus_percentage += 5
    elif grade == 'B':
        bonus_percentage += 10
    
    bonus_amount = (salary * bonus_percentage) / 100
    total_salary = salary + bonus_amount
    
    return total_salary

salary = float(input("Enter the salary of the employee: $"))
grade = input("Enter the grade of the employee (A or B): ")

total_salary = calculate_bonus(salary, grade)
print("The salary that the employee will get is: $", total_salary)
