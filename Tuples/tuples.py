# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# details = imelda[0:3]
# tracks = imelda[3]
#
# print(details)
#
# for track in tracks:
#     print("\t", track)
#

myTuple = "A", "B", "C", ("D", "E", ["F", "G"])
print(myTuple)
myTuple[3][2].append("H")
print(myTuple)