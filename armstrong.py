num = int(input("Enter a number: "))
n = num
sum = 0
digits = len(str(num))  

while n > 0:
    digit = n % 10
    sum += digit ** digits
    n //= 10

if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
