num = int(input("Enter a number to check palindrome: "))
if str(num) == str(num)[::-1]: 
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

a = int(input("Enter first number for GCD: "))
b = int(input("Enter second number for GCD: "))

while b != 0:
    a, b = b, a % b

print(f"GCD / HCF is: {a}")
