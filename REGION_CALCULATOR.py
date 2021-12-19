## This program I wrote for a final project. It takes in a massive csv file for 4 centuries, each year and creates a query for an inputYear


import csv
def get_unique_cities_count(filename):
    sets = []
    lister = []
    count = 0
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0]!= "year":
                sets.append(row[1])

    for i in sets:
        y = sets.count(i)
        if y > 1:
            count += 0
        if y == 1:
            count += 1
    return count


def get_year_count(filename):
    sets = []
    cities = dict()
    count = 0
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:

            if row[0]!= "year":
                sets.append(row[1])

    for i in sets:
        y = sets.count(i)
        cities[i] = y

    return cities

import csv

def get_regions(filename):
    sets = []
    regions = dict()
    count = 0
    regions['East Asia'] = 0
    regions['North America'] = 0
    regions['Middle East'] = 0
    regions['South Asia'] = 0
    regions['East Asia'] = 0
    regions['Europe'] = 0
    regions['Latin America'] = 0
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            if row[0]!= "year" and row[1] !="city" and row[2]!= "country" and row[3]!="population" and row[4] != "region":
               regions[row[4]] = regions[row[4]] + int(row[3])

    return regions

def most_cities(filename, inputYear):
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
                if row[0] == inputYear:
                    print(row[1], " ", end='')

def total_pop(filename,inputYear):
    total = 0
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
                if row[0] == inputYear:
                    total = total + int(row[3])
        return total

def region_count(filename,inputYear):
    sets = []
    regions = dict()
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
                if row[0] == inputYear:
                    sets.append(row[4])

    for i in sets:
        y = sets.count(i)
        regions[i] = y

    for j in regions.keys():
        print(j,regions[j])
    
                    

file = input("Enter file name: ")
year_OI = input("Enter the year of interest ")
while year_OI != "quit":
    print()
    print("Most populous cities in year " + str(year_OI) + ":")
    most_cities(file, int(year_OI))
    print()
    print("Total population: in large cities, in thousands:", total_pop(file, year_OI))
    print()
    print("Big city distribution by region:")
    region_count(file,year_OI)
    year_OI = str(input("Enter the year of interest "))

