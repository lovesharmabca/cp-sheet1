a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
if a >= b:
    if a >= c:
        max_num = a
    else:
        max_num = c
else:
    if b >= c:
        max_num = b
    else:
        max_num = c
print(f"The maximum number is: {max_num}")