num = int(input("Enter a number: "))
if num % 7 == 0 or abs(num) % 10 == 5:
    print(f"{num} satisfies at least one condition (divisible by 7 or ends with 5)")
else:
    print(f"{num} does not satisfy either condition")