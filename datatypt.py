x = input()
try:
    x = int(x)
    print(f"Value: {x}, Type: int")
except ValueError:
    try:
        x = float(x)
        print(f"Value: {x}, Type: float")
    except ValueError:
        print(f"Value: {x}, Type: str")
