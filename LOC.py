def countLOC(s):
    count = 0
    for line in s:
        line = line.strip()
        if line != '':
            if line[0] != '#':
                count += 1
            else: 
                count += 0
    return count


f = input()
file = open(f, "r")
print("Number of lines of code:", countLOC(file))
    
