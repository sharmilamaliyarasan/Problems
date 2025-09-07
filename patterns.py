## Right angle
N = 5
for i in range(1, N+1):
    print('*' * i)

## Inverted Right angle
N = 5
for i in range(N, 0, -1):
    print('*' * i)

## Pyramid Pattern
N = 5
for i in range(1, N+1):
    print(' ' * (N-i) + '*' * (2*i-1))
