def printNumber():
    while True:
        try:
            num = int(input("Enter a number: "))
            if -1000 <= num <= 1000:
                print(num)
                break
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

printNumber()
