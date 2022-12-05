stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
entries = []

def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        for line in input_text:
            if line[0] == "[":
                add_to_stacks(line)
            elif line[0] == "m":
                add_to_entries(line)
    for stack in stacks:
        stacks[stack].reverse()

def add_to_stacks(line):
    stacks[1].append(line[1])
    if len(line) >= 6 and line[5] is not " ":
        stacks[2].append(line[5])
    if len(line) >= 10 and line[9] is not " ":
        stacks[3].append(line[9])
    if len(line) >= 14 and line[13] is not " ":
        stacks[4].append(line[13])
    if len(line) >= 18 and line[17] is not " ":
        stacks[5].append(line[17])
    if len(line) >= 22 and line[21] is not " ":
        stacks[6].append(line[21])
    if len(line) >= 26 and line[25] is not " ":
        stacks[7].append(line[25])
    if len(line) >= 30 and line[29] is not " ":
        stacks[8].append(line[29])
    if len(line) >= 34 and line[33] is not " ":
        stacks[9].append(line[33])


def add_to_entries(line):
    parts = line.split(" ")
    entries.append([int(parts[1]), int(parts[3]), int(parts[5][0])])

get_data("aoc5.txt")

def move_crate(entry):
    moving = []
    for i in range(0,entry[0]):
        moving.append(stacks[entry[1]].pop())
    moving.reverse()
    for i in moving:
        stacks[entry[2]].append(i)

for entry in entries:
    move_crate(entry)

for i in range(1,10):
    print(stacks[i][-1])