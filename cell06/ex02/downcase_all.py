import sys

def downcase_it(a_string):
    return a_string.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        print(downcase_it(param))
