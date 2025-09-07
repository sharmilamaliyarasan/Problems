num = int(input("Enter a number: "))
n = num
count = 0
rev = 0

while n > 0:
    digit = n % 10         
    rev = rev * 10 + digit 
    n //= 10              
    count += 1             
print(f"Number of digits in {num}: {count}")
print(f"Reverse of {num}: {rev}")
