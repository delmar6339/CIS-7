while True:
    user_input = input("Do you want to enter student data? Enter 'Yes' to continue, or any other key to stop: ")
    if user_input.lower() != "yes":
        break 
    last_name = input("Enter the student's last name: ")
    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))
    average_score = (score1 + score2) / 2
    print(f"Student last name: {last_name}")
    print(f"Average score: {average_score}")
    students_count = 1
    user_input = input("Do you want to enter data for another student? Enter 'Yes' to continue, or any other key to stop: ")
    if user_input.lower() != "yes":
        break
print(f"Total number of students entered: {students_count}")