with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)
















# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")


# name = input("What's you name? ")

# # file = open("names.txt", "a")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
# This will automatic file closing system
