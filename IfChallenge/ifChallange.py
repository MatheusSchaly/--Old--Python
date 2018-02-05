name = input("Please enter your name: ")
age = int(input("Please enter you age: "))
if 18 <= age <= 30:
    print("{}, welcome to the holiday!!".format(name))
else:
    print("Sorry, you are {0} years old, we only accept "
          "ages between 17 and 31".format(age))