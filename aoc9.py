
def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        text = []
        for i in input_text:
            text.append(i.rstrip())
        commands = []
        for i in text:
            entry = i.split(" ")
            entry[1] = int(entry[1])
            commands.append(entry)
        return commands

data = get_data("aoc9.txt")
#data = [["U",2], ["R",1], ["L", 12], ["R", 12]]

class Object():
    def __init__(self, x, y):
        self.x = x
        self.y = y

head = Object(0,0)
tail = Object(0,0)
grid = [[tail.x, tail.y]]

def execute_move(command):
    # set new position relative to old position
    for steps in range(0,command[1]):
        if command[0] == "U":
            head.y += 1
        elif command[0] == "D":
            head.y -= 1
        elif command[0] == "L":
            head.x -= 1
        elif command[0] == "R":
            head.x += 1
        move_tail()

def move_tail():
    vector = [head.x - tail.x, head.y - tail.y]
    # if they overlap or are adjacent, do not move the tail
    if abs(vector[0]) <= 1 and abs(vector[1]) <= 1:
        pass
    # else if head straight to the right (etc)
    elif vector == [2,0]:
        tail.x += 1
    elif vector == [-2,0]:
        tail.x -= 1
    elif vector == [0,2]:
        tail.y += 1
    elif vector == [0,-2]:
        tail.y -= 1
    # diagonal positioning will either be top left, top tight, bottom right, bottom left; each with two permutations but similar move
    # top left
    elif vector == [-1,2] or vector == [-2,1]:
        tail.x -= 1
        tail.y += 1
    # top right
    elif vector == [1,2] or vector == [2,1]:
        tail.x += 1
        tail.y += 1
    # bottom right
    elif vector == [2,-1] or vector == [1,-2]:
        tail.x += 1
        tail.y -= 1
    # bottom left
    elif vector == [-2,-1] or vector == [-1,-2]:
        tail.x -= 1
        tail.y -= 1
    update_grid()

def update_grid():
    tail_pos = [tail.x, tail.y]
    if tail_pos not in grid:
        grid.append(tail_pos)

for command in data:
    execute_move(command)

print(len(grid))