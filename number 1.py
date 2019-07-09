# import math
# import numpy
#
#
# def f1(x):
#     ans = math.tan(x)
#     return ans
#
#
# def newton(x0, x1, x):
#     b0 = f1(x0)
#     b1 = (f1(x1) - f1(x0))/(x1-x0)
#
#
#     order2 = b0 + b1 * (x - x0)
#
#     return order2
#
# estimate = newton(44 * math.pi/180 , 46 * math.pi/180,45 * math.pi/180)
# print(estimate)
#
# def lagrange(x0, x1, x):
#     l0 = (x - x1)/(x0 -x1)
#     l1 = (x - x0)/(x1 - x0)
#
#     order2 = (l0*f1(x0)) + l1*f1(x1)
#
#     return order2
#
# estimate2 = lagrange(44 * math.pi/180 , 46 * math.pi/180,45 * math.pi/180)
# print(estimate2)


import math


def f(x):
    ans = math.tan(x)
    return ans

def newton(x0, x1, x,f):
    b0 = f(x0)
    b1 = (f(x1)-f(x0))/(x1-x0)

    order2 = b0 + b1*(x-x0)

    return order2


def lagrange(x0,x1, x,f):
    l0 = (x - x1)/(x0-x1)
    l1 = (x -x0)/(x1-x0)

    order2 = (l0*f(x0)) + (l1*f(x1))
    return order2;

print("Newton: ", newton(44 * math.pi/180,46 * math.pi/180,45 * math.pi/180,f))
print("Lagrange: ", lagrange(44 * math.pi/180,46 * math.pi/180,45 * math.pi/180,f))
