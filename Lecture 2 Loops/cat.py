# Validation
def main():
    number = get_number()
    meow(number)


def meow(n):
    for _ in range(n):
        print("meow")


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

main()













"""
while True:   
    n = int(input("What's n? "))
    if n > 0:
        break


for _ in range(n):
    print("meow")



"""