IP = input("Inform the IP: ")

if IP[-1] != ".":
    IP += "."
segments = 1
howLong = 0

for number in IP:
    if number == '.':
        print("The segment {} is {} long".format(segments, howLong))
        segments += 1
        howLong = 0
    else:
        howLong += 1
