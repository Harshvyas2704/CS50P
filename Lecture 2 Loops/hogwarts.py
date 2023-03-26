# This is list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# Hermione, Gryffindor, Otter
# Harry, Gryffindor, Stag
# Ron, Gryffindor, Jack Russell terrier
# Draco, Slytherin, None



#---------------------------------------------------------------------------------

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# # print(students) -> ['Hermione', 'Harry', 'Ron']
# # print(students[0]) # -> Hermione 

# # for student in students:
# #     print(student)

# for i in range(len(students)):
#     print(i, students[i], houses[i])


# # dictionaries
# # similar like map in Java -> key value pairs
# # when you inerate through dictionaries it will by default iterate on keys

# students = {
#     "Harmione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Dreco": "slytherin"     
# }

# # print(students["Harmione"]) -> Gryffindor

# for student in students:
#     print(student, students[student], sep=", ") 

# """

# Harmione, Gryffindor
# Harry, Gryffindor
# Ron, Gryffindor
# Dreco, slytherin

# """