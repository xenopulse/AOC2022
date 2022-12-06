def get_data(filename):
    with open(filename, "r") as file:
        return file.read()

data = get_data("aoc6.txt")

def find_unique(data):
    sequence = data[0:4]
    print(sequence)
    for index, letter in enumerate(data):
        if index < 4:
            pass
        else:
            sequence = sequence[1:] + data[index]
            if len(set(sequence)) == 4:
                return (index +1)

position = find_unique(data)
print (position)