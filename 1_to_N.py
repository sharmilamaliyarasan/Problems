N = 10

def print_1_to_N(n):
    if n == 0:
        return  
    print_1_to_N(n-1)  
    print(n)  

print_1_to_N(N)