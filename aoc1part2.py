file = open("aoc1_input.txt", "r")
high1 = 0
high2 = 0
high3 = 0
current = 0
while True:   
    line = file.readline()
    if not line:
        print(high1 + high2 + high3)
        break
    if line is not "\n" and line is not "":
        current += int(line)
    else:
        current = 0
    if current > high1:
        high3 = high2
        high2 = high1
        high1 = current
    elif current > high2:
        high3 = high2
        high2 = current
    elif current > high3:
        high3 = current
file.close()