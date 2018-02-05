locations = {0: "Sitting",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}
         }

wordsPlayerMayUse = {"NORTH": "N",
                     "SOUTH": "S",
                     "EAST": "E",
                     "WEST": "W",
                     "QUIT": "Q"
                     }

# print(locations[0].split())
# print(locations[3].split(","))
# print(" ".join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    if direction in wordsPlayerMayUse:
        direction = wordsPlayerMayUse.get(direction)
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("This direction does not exist")
