
def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="world"): # *
    print("hello,", to)


main()

# * => this is default value that if caller do not pass arguments then default value will be there