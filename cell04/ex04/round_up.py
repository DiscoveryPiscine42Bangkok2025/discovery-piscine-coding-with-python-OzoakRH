import math

try:
    num = float(input("Give me a number: "))
    rounded_num = math.ceil(num)
    print(rounded_num)
except ValueError:
    print("Error: Invalid input. Please enter a number.")
