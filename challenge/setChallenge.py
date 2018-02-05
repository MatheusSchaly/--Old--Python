myString = "A set is mutable and unordered"
myList = []
myVowelSet = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

finalSet = set(myString).difference(myVowelSet)
finalList = sorted(finalSet)

print(finalList)