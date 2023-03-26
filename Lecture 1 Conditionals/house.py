def main():
    name = input("What's your name? ")
    
    match name:
        case "Harry" | "Hermiony" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

main()

# match is similer to switch case methods in Java