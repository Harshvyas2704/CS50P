def main():
    x = int(input("What's x? "))
    print("x square is", square(x))


def square(n):
    return pow(n, 2)


if __name__ == "__main__":
    main()
