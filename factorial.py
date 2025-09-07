N = int(input())
factorial = 1
for i in range(1, N+1):
    factorial *= i
print(f"Factorial of {N} is {factorial}")