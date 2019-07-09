def f(x):
    return x**3 + 7*x**2 - 36

def derivative(x):
    return 3*x**2 + 14 * x

def bisection(f,a, b, e0):
    if (f(a) * f(b) >= 0):
        print("You have not assumed right a and b\n")

    while ((b - a) >= e0):
        c = (a + b) / 2
        if (f(c) == 0):
            break
        if (f(c) * f(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ", c)

bisection(f,-4, -2, 0.05)

def newton(x, e0):
    h = f(x) / derivative(x)

    while abs(h) >= e0:
        h = f(x) / derivative(x)
        x = x - h

    return x

print("The value of the roots is",newton(-4,0.05))





