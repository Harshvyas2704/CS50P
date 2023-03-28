import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # This is slice
    print(arg)



# Slice -> we have to give first element and last, if we don't want to give last element then use ":" this with quotes