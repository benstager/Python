import math

def distanceCalculator(target, home):
    shortest_distance = float(10000)
    target_city = "NULL"
    for i in target.keys():
        house_distance = float(math.sqrt((home[1] - target[i][1])**2 +
                                               (home[0] - target[i][0])**2))
        if house_distance < shortest_distance:
                        shortest_distance = house_distance
                        target_city = i
    return target_city, shortest_distance
    



burroughs = {"Bronx": [45, 90], "New York City": [20, 10], "Staten Island": [-10, 100],
             "Brookln" :[40, 80], "Queens": [20, 45], "Manhattan": [34, 44],
             "Westchester":[10,-1]}

lat = int(input())
long = int(input())
your_house = [lat,long]


print("You are closest to", distanceCalculator(burroughs,your_house), "km")
