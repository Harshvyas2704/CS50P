class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

def check():
    print("Hi")
"""
Implemantation of get_student method with tuple
# name = input("Name: ")
    # house = input("House: ")
    # #return (name, house) # This is tuple and tuple are immutable, but we can iterate through it like list, but this is immutable
    # return [name, house]

    ---------------------------------------
def get_student():
    
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

"""
