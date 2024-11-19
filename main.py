n = int(input("Enter a number: "))
factorial = 1
sum_of_factorials = 0
for digit in str(n):
    factorial = 1
    for i in range(1, int(digit) + 1):
        factorial *= i
    sum_of_factorials += factorial
if sum_of_factorials == n:
    print(f"{n} is a Strong number")
else:
    print(f"{n} is not a Strong number")
