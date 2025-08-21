num = int(input("Enter a number: "))
if num % 3 == 0 and abs(num) % 10 == 4:
    print(f"{num} is divisible by 3 and ends with 4")
else:
    print(f"{num} does not meet both conditions")