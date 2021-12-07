## Iterative method that I wrote for the 'Runge-Kutta' approximation in diff eq
## This is for y' = x, meaning y = x^2/2 + C where y(0) in this case is 1
## So y(x) 1/2(x^2) + 1,
## Testing xend = 1, we get 1.6, where the actual is 1.5 so the approximation is
## somewhat successful



import math
def f(x,y):
    yn = x
    return yn



y0 = 1
xbeg = 0
xend = 1
h = .1

y = y0
x = xbeg

while x <= xend:
    v1 = h*f(x,y)
    v2 = h*f((x + (1/2)*h), (y + (1/2)*v1))
    v3 = h*f((x + h), (y + (2*v2) -1))

    y += (1/6)*(v1+(4*v2)+v3)
    x += h

print("y(x) approximated at x =", xend, "is", y)
