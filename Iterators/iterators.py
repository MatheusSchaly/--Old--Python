# string = "1234567890"
#
#
# #
# # my_iterator = iter(string)
# # print(my_iterator)
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# #
# # print(next(my_iterator))
#
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

myList = [1, 2, 3, 4, 5]
myIterator = iter(myList)

for number in range(0, len(myList)):
    print(next(myIterator))