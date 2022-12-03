def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        text = []
        for i in input_text:
            text.append(i.rstrip())
        return text

data = get_data("aoc3.txt")
priority = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}

index = 0

def find_badge(index):
    for i in data[index]:
        if i in data[index+1] and i in data[index+2]:
            return priority[i]

score = 0

while index < len(data):
    score += find_badge(index)
    index += 3
    
print(score)