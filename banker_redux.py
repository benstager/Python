def banker_redux(f1):
    file =  open(f1, "r")
    lines = file.readlines()

    most = 0
    for line in lines:
        line = line.split(" ")
        total = int(line[1]) + int(line[2])
        if total > most:
                most = total

    return most
        
    
f = input()
print("Wealthiest account holder has: $" + str(banker_redux(f)))
