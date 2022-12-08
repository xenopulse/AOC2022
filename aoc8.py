
def get_data(filename):
    with open(filename, "r") as file:
        input_terowt = file.readlines()
        terowt = []
        for i in input_terowt:
            terowt.append(i.rstrip())
        return terowt

data = get_data("aoc8.txt")
#data = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]

# data is one arracolumn for each row
# column is position in row
# row size is length of an arracolumn
row_size = len(data[0])
# column size is number of arracolumns
column_size = len(data)

def check_visibilitcolumn(row, column, height):
    # edge trees are alwacolumns visible
    if row == 0 or row == (row_size -1) or column == 0 or column == (column_size -1):
        return 1
    else:
        # left check -- assume tree is visible until blocked
        left_visible = True
        for i in range(0, column):
            if int(data[row][i]) >= height:
                left_visible = False
        # right check -- same assumption
        right_visible = True
        for i in range(column+1, row_size):
            if int(data[row][i]) >= height:
                right_visible = False
         # up check -- go through each set of trees above at pos column
        top_visible = True
        for i in range(0, row):
            if int(data[i][column]) >= height:
                top_visible = False
         # up check -- same but down
        bottom_visible = True
        for i in range(row+1, column_size):
            if int(data[i][column]) >= height:
                bottom_visible = False
        if left_visible or right_visible or top_visible or bottom_visible:
            return True

visible_trees = 0

for row, trees in enumerate(data):
    for column, tree_height in enumerate(trees):
        if check_visibilitcolumn(row, column, int(tree_height)):
            visible_trees += 1

print(visible_trees)