import sys

if len(sys.argv) >= 3:
    parameters = sys.argv[1:]
    
    for param in reversed(parameters):
        print(param)
else:
    print('none')
