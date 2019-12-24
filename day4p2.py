potential = 0
for p in range(152085, 670283):
    string = str(p)
    if len(string) == 6:
        pair = False
        increasing = True
        numeral = -1
        group_size = 0
        for i in range(len(string)):
            integer = int(string[i])
            if integer < numeral:
                increasing = False
                break
            elif integer == numeral:
                group_size += 1
            else:
                numeral = integer
                if group_size == 2:
                    pair = True
                group_size = 1
        if group_size == 2:
            pair = True
        if pair and increasing:
            potential += 1
print("Potential Pairs: " + str(potential))
