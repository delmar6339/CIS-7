start_value = int(input("Enter start value: "))
stop_value = int(input("Enter stop value: "))
increment_value = int(input("Enter increment value: "))
if increment_value <= 0:
    increment_value = abs(increment_value)
current_value = start_value  
while current_value <= stop_value:
    print(current_value)
    current_value += increment_value 