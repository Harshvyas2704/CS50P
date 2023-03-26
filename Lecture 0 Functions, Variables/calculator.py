x = float(input("What's X? ")) # output of input function will become input of int function
y = float(input("What's Y? ")) 

z = round(x / y, 3)
print(z)
# print(round(x + y))



# round(number[, ndigist]) -> first is number, in docs if there are [] then it means it's optional,
# here ndigits means how many digits we want to round
# print(f"{z:.2f}") -> this will get 2 digits round