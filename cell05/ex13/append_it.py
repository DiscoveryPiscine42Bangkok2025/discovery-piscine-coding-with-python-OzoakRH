import sys

if len(sys.argv) == 1:
    print("none")
else:

    for arg in sys.argv[1:]:

        if arg.endswith("ism"):
            continue
        else:
            print(f"{arg}ism")
