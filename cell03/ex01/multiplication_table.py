try:
    num = int(input("Enter a number\n"))
    for i in range(10):  # i จะนับจาก 0 ถึง 9
        result = num * i
        print(f"{num} x {i} = {result}")
except ValueError:
    print("Invalid input. Please enter a number.")
