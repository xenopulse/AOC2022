file = open("aoc1_input.txt", "r")
high = 0
current = 0
while True:   
    line = file.readline()
    if not line:
        print(high)
        break
    if line is not "\n" and line is not "":
        current += int(line)
    else:
        current = 0
    if current > high:
        high = current
file.close()