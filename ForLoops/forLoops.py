number = "9,223,372,036,854,775,807"
cleanerNumber = ''

for char in number:
    if char in '0123456789':
        cleanerNumber = cleanerNumber + char

newNumber = int(cleanerNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j), end="\t")
    # print("==============")
    print('')