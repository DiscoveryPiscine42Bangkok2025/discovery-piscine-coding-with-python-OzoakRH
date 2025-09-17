import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        numbers_list = list(range(start, end + 1))
        
        print(numbers_list)

    except ValueError:
        print("none")
