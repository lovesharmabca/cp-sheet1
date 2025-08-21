
A = float(input("Enter first number (A): "))
B = float(input("Enter second number (B): "))
C = float(input("Enter third number (C): "))

if A <= B and A <= C:
    print(f"Minimum number is: {A}")
elif B <= A and B <= C:
    print(f"Minimum number is: {B}")
else:
    print(f"Minimum number is: {C}")