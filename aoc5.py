stacks = []
entries = []

def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        for line in input_text:
            if line[0] == "[":
                add_to_stacks(line)
            elif line[0] == "m":
                add_to_entries(line)

def add_to_stacks(line):
    pass

def add_to_entries(line):
    parts = line.split(" ")
    entries.append(split[0], etc)
    pass

get_data("aoc5.txt")

def move_crate(entry):
    pass

final = ""

for entry in entries:
    move_crate(entry)

# print first of each row