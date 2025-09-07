N = 5
name = "Sharmila"

def print_name(n):
    if n <= 0:
        return  
    print(name)
    print_name(n-1)

print_name(N)