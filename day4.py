potential = 0
for p in range(152085, 670283):
    string = str(p)
    if len(string) == 6:
        pair = False
        increasing = True
        for i in range(len(str(string))-1):
            if string[i] > string[i+1]:
                increasing = False
                break
            elif string[i] == string[i+1]:
                pair = True
        if pair and increasing:
            potential += 1
print("Potential Pairs: " + str(potential))
