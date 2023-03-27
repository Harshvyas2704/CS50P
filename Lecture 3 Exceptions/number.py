def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            pass


main()


"""
we can use else statement after except, it will work same as finally in Java

"""