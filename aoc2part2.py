def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        text = []
        for i in input_text:
            text.append(i.rstrip())
        return text

data = get_data("aoc2.txt")

def win_points(player):
    if player == "Z":
        return 6
    elif player == "Y":
        return 3
    else:
        return 0

def choice_points(opponent, player):
    if (opponent == "A" and player == "Y") or (opponent == "B" and player == "X") or (opponent == "C" and player == "Z"):
        return 1
    elif (opponent == "A" and player == "Z") or (opponent == "B" and player == "Y") or (opponent == "C" and player == "X"):
        return 2
    else:
        return 3

score = 0

for i in range(0,len(data)):
    score += win_points(data[i][-1])
    score += choice_points(data[i][0], data[i][-1])

print (score)