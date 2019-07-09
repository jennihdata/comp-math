from sympy import Symbol, Derivative

def f(x):
    return x**4 - 3*x**3 + 6*x**2 - 10*x - 9

def derivative1(f, x, h):
    return (f(x+h) - f(x-h))/ (2*h)

def derivative2(f, x, h):
    return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)

def forward(f,x,h):
    return (f(x+h) - f(x))/ h

def backward(f,x,h):
    return (f(x) - f(x-h))/ h

def center(f,x,h):
    return (f(x+h) - f(x-h))/ (2*h)

x= Symbol('x')

function = x**4 - 3*x**3 + 6*x**2 - 10*x - 9

deriv1 = Derivative(function, x)
deriv1_result = deriv1.doit().subs({x:0})

deriv2 = Derivative(deriv1, x)
deriv2_result = deriv2.doit().subs({x:0})

print("exact: ",deriv1_result, deriv2_result)

fir05 = derivative1(f, 0, 0.5)
sec05 = derivative2(f, 0, 0.5)
fir025 = derivative1(f, 0, 0.25)
sec025 = derivative2(f, 0, 0.25)
fir0125 = derivative1(f, 0, 0.125)
sec0125 = derivative2(f, 0, 0.125)

print("first derivtive:", fir05,"second derivative:", sec05)
print("first derivtive:", fir025,"second derivative:", sec025)
print("first derivtive:", fir0125,"second derivative:", sec0125)

print("h =0.5")
print(forward(f,0,0.5))
print(backward(f,0,0.5))
print(center(f,0,0.5))

print("h =0.25")
print(forward(f,0,0.25))
print(backward(f,0,0.25))
print(center(f,0,0.25))

print("h =0.125")
print(forward(f,0,0.125))
print(backward(f,0,0.125))
print(center(f,0,0.125))

