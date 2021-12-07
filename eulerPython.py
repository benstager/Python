def f(x,y):
    yprime = x
    return x


xbeg = 0
xend = 1
y0 = 1
h = float(input())

y = y0
x = xbeg
while x <= xend:
    y += f(x,y)*h
    x += h

print(y)
