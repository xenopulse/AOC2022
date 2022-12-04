def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        text = []
        for i in input_text:
            text.append(i.rstrip())
        return text

data = get_data("aoc4.txt")

def make_pairs():
    pairs = []
    for i in range(0,len(data)):
        newpair = data[i].split(",")
        pairleft = newpair[0].split("-")
        pairright = newpair[1].split("-")
        combined = [[int(pairleft[0]), int(pairleft[1])], [int(pairright[0]), int(pairright[1])]]
        pairs.append(combined)
    return pairs

def find_overlap(pair):
    if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]):
        return 1
    else:
        return 0

score = 0

pairs = make_pairs()

for i in range(0,len(pairs)):
    score += find_overlap(pairs[i])

print(score)