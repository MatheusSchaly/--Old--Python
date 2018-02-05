age = int(input("How old are you? "))
if not age < 18:
    print("You are old enough to vote")
    print("Please put and X in the box")
else:
    print("Please come back in {0} years".format(18 - age))