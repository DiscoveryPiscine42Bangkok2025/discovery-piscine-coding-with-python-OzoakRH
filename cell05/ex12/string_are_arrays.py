import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    result_string = ""
    z_found = False

    for char in input_string:
        if char == 'z':
            result_string += "z"
            z_found = True

    if z_found:
        print(result_string)
    else:
        print("none")
