print("Welcome to Cup of Joe!")
print("We have espresso, americano, and latte. What would you like to drink?")
coffType = str(input())

while coffType != "espresso" and coffType != 'americano' and coffType != 'latte':
    print("Sorry, I didn't get that. Could you please try again?")
    coffType = str(input())
    
print("How many oz would you like?", end='')
ozNum = int(input())
totalPrice = float(ozNum*.30)
centsNum = int(100*(totalPrice - int(totalPrice))) + 1
print("Here's your", ozNum, "oz cup of", coffType)

if centsNum != 1:
    print("Your total is", int(totalPrice), "dollars and", centsNum, "cents")

elif centsNum == 1:
    print("Your total is", int(totalPrice), "dollars even")
