
def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        text = []
        for i in input_text:
            text.append(i.rstrip())
        return text

data = get_data("aoc8.txt")
#data = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]

# data is one arracolumn for each row
# column is position in row
# row size is length of an arracolumn
row_size = len(data[0])
# column size is number of arracolumns
column_size = len(data)

def check_visibility(row, column, height):
    # left check 
    left_visible = 0
    for i in reversed(range(0, column)):
        if int(data[row][i]) < height:
            left_visible += 1
        else:
            break
    # right check 
    right_visible = 0
    for i in range(column+1, row_size):
        right_visible += 1
        if not int(data[row][i]) < height:
            break
     # up check 
    top_visible = 0
    for i in reversed(range(0, row)):
        top_visible += 1
        if not int(data[i][column]) < height:
            break
     # up check 
    bottom_visible = 0
    for i in range(row+1, column_size):
        bottom_visible += 1
        if not int(data[i][column]) < height:
            break
    print (str(left_visible) + str(right_visible) + str(top_visible) + str(bottom_visible))
    return left_visible * right_visible * top_visible * bottom_visible

best_view = 0

for row, trees in enumerate(data):
    for column, tree_height in enumerate(trees):
        view = check_visibility(row, column, int(tree_height))
        print ("Tree at " + str(row) + "/" + str(column) + " with height of " + str(tree_height) + " has a view of " + str(view))
        if view > best_view:
            best_view = view

print(best_view)