employees_count = 0 
total_gross_pay = 0  
while True:
    user_input = input("Do you want to enter employee data? Enter 'Yes' to continue, or any other key to stop: ")
    if user_input.lower() != "yes":
        break 
    last_name = input("Enter the employee's last name: ")
    hours_worked = float(input("Enter the number of hours worked: "))
    rate_of_pay = float(input("Enter the rate of pay: "))
    if hours_worked <= 40:
        gross_pay = hours_worked * rate_of_pay
    else:
        gross_pay = (40 * rate_of_pay) + ((hours_worked - 40) * rate_of_pay * 1.5)
    print(f"Employee last name: {last_name}")
    print(f"Gross pay: {gross_pay}")
    
    employees_count += 1  
    total_gross_pay += gross_pay  
    user_input = input("Do you want to enter data for another employee? Enter 'Yes' to continue, or any other key to stop: ")
    if user_input.lower() != "yes":
        break 
print(f"Total number of employees entered: {employees_count}")
print(f"Total gross pay: {total_gross_pay}")
print(f"Average gross pay: {total_gross_pay / employees_count + 1}")