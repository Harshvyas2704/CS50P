import re

email = input("What's your email? ").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")


"""
. any character except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repititions
{m} m repititions
{m, n} m - n repititions

"""
