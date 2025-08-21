days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday"]
day_number = int(input("Enter a number (1-7): "))
if 1 <= day_number <= 7:
    print(days[day_number - 1])
else:
    print("Invalid input! Please enter a number between 1 and 7.")