## This is an algorithm I wrote in 2020, but have converted it from C++ to Python
## Consider a 2x2 system of linear differential equations with coeffecients
## a11, a12, b21, b22
## The dynamics of a system at the origin (0,0) can be calculated using a relation between the
## trace and determinant of the system

## Trace = a11 + b22
## Determinant = (a11 * b22) - (b21 * 12)


import math
def dynamics(lin_sys):
    trace = lin_sys[0][0] + lin_sys[1][1]
    det = (lin_sys[0][0] * lin_sys[1][1]) - (lin_sys[0][1] * lin_sys[1][0])

    trace_det = (trace**2) - 4*det

    if trace == 0:
        print("Saddle point")
    if trace > 0:
        if trace_det > 0:
            print("Unstable node")
        if trace_det < 0:
            print("Unstable spiral")
    if trace < 0:
        if trace_det < 0:
            print("Stable spiral")
        if trace_det > 0:
            print("Stable node")
                                        







system = [[3,1],[0,5]]
dynamics(system)
