
A = int(input("Enter angle A: "))
B = int(input("Enter angle B: "))
C = int(input("Enter angle C: "))
if A > 0 and B > 0 and C > 0 and A + B + C == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")