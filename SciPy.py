import numpy
from scipy.optimize import minimize
from scipy.integrate import quad
def fun(x):
    return (2*(x[0]-x[1]-3)**2 + 4*(x[0]+2*x[1]+1)**4)
constraint=[{'type':'ineq','fun':lambda x:x[0]-x[1]+3},
            {'type':'ineq','fun':lambda x:5-((x[0]+2)**2+(x[1]+1)**2)}]
x0=[0,0]
result=minimize(fun,x0,constraints=constraint)
print("PART-A")
print("Optimal value: ",result.fun)
print("Optimal point: ",result.x)

def integrand(t):
    x=numpy.sqrt(3)*numpy.cos(t)
    y=numpy.sqrt(3)*numpy.sin(t)
    return x**2+y**4
integral,e=quad(integrand,0,2*numpy.pi)
print("PART-B")
print("Integral value: ",integral)