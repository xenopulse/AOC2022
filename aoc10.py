def get_data(filename):
    with open(filename, "r") as file:
        input_text = file.readlines()
        text = []
        for i in input_text:
            if "noop" in i:
                text.append(0)
            else:
                entry = i.split(" ")
                text.append(int(entry[1]))
        text.append(0)
        text.append(0)
        return text

data = get_data("aoc10.txt")
# data = get_data("aoc10test.txt")

print (data)
print(len(data))

cycle = 1
register = 1
results = []
data_counter = 0

def check_register():
    if cycle in [20, 60, 100, 140, 180, 220]:
        print("Cycle at ", cycle, "  is ", register)
        results.append(register * cycle)

for entry in data:
    if entry == 0:
        cycle += 1
        check_register()
    else:
        cycle += 1
        check_register()
        cycle += 1
        register += entry
        check_register()

print (results)
print ("Total is ", sum(results))
