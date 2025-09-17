import sys

num_params = len(sys.argv) - 1

if num_params == 0:
    print("none")
else:
    print(f"parameters: {num_params}")


    for i in range(1, len(sys.argv)):
        param = sys.argv[i]
        param_length = len(param)
        print(f"{param}: {param_length}$")
