def print_n_times(message, n):
    if n <= 0:
        return 
    print(message)
    print_n_times(message, n-1) 

print_n_times("Hello", 5)