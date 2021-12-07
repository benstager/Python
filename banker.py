## copyright Ben Stager 2021
## Based on a LeetCode problem I completed earlier
## This algorithm takes an array with subarrays as elements
## It takes in an m x n matrix, where m is accts[i] or the ith account,
## and n is either the savings or checking account of that ith person
## The algorithm determins the wealthiest account holder


import math

def banker(accts):
    wealth = [len(accts)]
    money = 0
    acct = 'NULL'
    for i in range(len(accts)):
        if sum(accts[i]) > money:
            money = sum(accts[i])
            acct = i

    print("Account #" + str(acct), "with $" + str(money))
        
accounts = [[1000,500], [122142,412],[242422,216],[125,126]]

banker(accounts)
