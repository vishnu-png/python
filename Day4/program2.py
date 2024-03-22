def get_user_details():
    total_users = int(input("Enter the total number of users: "))
    student_users = int(input("Enter the number of student users: "))
    staff_users = int(input("Enter the number of staff users: "))

    non_teaching_staff_users = staff_users // 3

    print("\nUser details:")
    print("Total users:", total_users)
    print("Student users:", student_users)
    print("Staff users:", staff_users)
    print("Non-teaching staff users:", non_teaching_staff_users)


get_user_details()
