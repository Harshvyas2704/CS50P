
# Ask user for their name
# name = input("What's your name? ")

# Remove whitespace from str from both the side
# name = name.strip()

# Capitalize user's name only fist letter
# name = name.capitalize()

# Capitalize user's name from space ex -> harsh vyas -> Harsh Vyas
# name = name.title()

# We can merge method like this
name = input("What's your name? ").strip().title()

# Split user's name in first name and last name
first, last = name.split(" ") # this will work like this now first = harsh and last = vyas assiging 2 variables at same time

# Say hello to user
print(f"Hello, {last}")








# print("Hello, ", end="") # we override value of end to "" from "\n" so it will print in same line
# print(name)

# print(f"Hello, {name}") Another way to do this

# input is inbuilt function to take input from user

"""
    This is another way to comment

"""

#-----------------------------------------------------------------------------------------------

"""
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> Documentation of print function
    print("Hello, ", name, sep="???")  -> we override sep method so o/p will be -> Hello, ???Harsh
    same we can override end method 

"""