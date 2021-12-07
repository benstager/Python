import random
lst = []
for i in range(100):
    lst.append(random.randint(1,501))

print("Original list:")
for i in range(100):
    print(lst[i])

print()
print()

print("Sorted list:")
lst.sort()
for i in range(100):
    print(lst[i])
    
print()
print()

print("Reversed sorted list:")
lst.reverse()
for i in range(100):
    print(lst[i])
print()
print()

print("Please ask for a number")
num = int(input())

while num not in lst:
    print("Sorry your number isn't here, guess again")
    num = int(input())
count = 0

    
for i in range(100):
    if num == lst[i]:
        count = count + 1

print("The number appeared", count, "time(s)")


m = max(lst)
mi = min(lst)

print("Max:", m)
print("Min:", mi)

