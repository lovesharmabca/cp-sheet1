
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    years_left = 18 - age
    print(f"You cannot vote yet. You'll be eligible in {years_left} year{'s' if years_left > 1 else ''}.")