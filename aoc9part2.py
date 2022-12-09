
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
# data = [["U",10], ["R",10], ["L", 2], ["D", 12]]

class Head():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tail():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def follow(self, parent_x, parent_y):
        vector = [parent_x - self.x, parent_y - self.y]
        # if they overlap or are adjacent, do not move the tail
        if abs(vector[0]) <= 1 and abs(vector[1]) <= 1:
            pass
        # else if head straight to the right (etc)
        elif vector == [2,0]:
            self.x += 1
        elif vector == [-2,0]:
            self.x -= 1
        elif vector == [0,2]:
            self.y += 1
        elif vector == [0,-2]:
            self.y -= 1
        # diagonal positioning will either be top left, top tight, bottom right, bottom left; each with THREE permutations but similar move
        # top left
        elif vector == [-1,2] or vector == [-2,1] or vector == [-2,2]:
            self.x -= 1
            self.y += 1
        # top right
        elif vector == [1,2] or vector == [2,1] or vector == [2,2]:
            self.x += 1
            self.y += 1
        # bottom right
        elif vector == [2,-1] or vector == [1,-2] or vector == [2,-2]:
            self.x += 1
            self.y -= 1
        # bottom left
        elif vector == [-2,-1] or vector == [-1,-2] or vector == [-2,-2]:
            self.x -= 1
            self.y -= 1
        print(self.name + " at position", self.x, self.y)

head = Head(0,0)
tail1 = Tail(0,0, "tail1")
tail2 = Tail(0,0, "tail2")
tail3 = Tail(0,0, "tail3")
tail4 = Tail(0,0, "tail4")
tail5 = Tail(0,0, "tail5")
tail6 = Tail(0,0, "tail6")
tail7 = Tail(0,0, "tail7")
tail8 = Tail(0,0, "tail8")
tail9 = Tail(0,0, "tail9")

grid = [[tail9.x, tail9.y]]

def execute_move(command):
    # set new position relative to old position
    for steps in range(0,command[1]):
        if command[0] == "U":
            head.y += 1
            print("Head moving up to", head.x, head.y)
        elif command[0] == "D":
            head.y -= 1
            print("Head moving down to", head.x, head.y)
        elif command[0] == "L":
            head.x -= 1
            print("Head moving left to", head.x, head.y)
        elif command[0] == "R":
            head.x += 1
            print("Head moving right to", head.x, head.y)
        tail1.follow(head.x, head.y)
        tail2.follow(tail1.x, tail1.y)
        tail3.follow(tail2.x, tail2.y)
        tail4.follow(tail3.x, tail3.y)
        tail5.follow(tail4.x, tail4.y)
        tail6.follow(tail5.x, tail5.y)
        tail7.follow(tail6.x, tail6.y)
        tail8.follow(tail7.x, tail7.y)
        tail9.follow(tail8.x, tail8.y)
        update_grid()

def update_grid():
    tail_pos = [tail9.x, tail9.y]
    if tail_pos not in grid:
        grid.append(tail_pos)

for command in data:
    execute_move(command)
print(grid)
print(len(grid))