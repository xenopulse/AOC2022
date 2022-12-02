def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        text = []
        for i in input_text:
            text.append(i.rstrip())
        return text

data = get_data("aoc2.txt")

def win_points(opponent, player):
    if (opponent == "A" and player == "Y") or (opponent == "B" and player == "Z") or (opponent == "C" and player == "X"):
        return 6
    elif (opponent == "A" and player == "Z") or (opponent == "B" and player == "X") or (opponent == "C" and player == "Y"):
        return 0
    else:
        return 3

def choice_points(XYZ):
    if XYZ == "X":
        return 1
    elif XYZ == "Y":
        return 2
    else:
        return 3

score = 0

for i in range(0,len(data)):
    score += win_points(data[i][0], data[i][-1])
    score += choice_points(data[i][-1])

print (score)