#lambda expressions in functions
def f(n): return lambda x: x ** n

f1 = f(2)
f2 = f(6)
print (f1(2), f2(2))

lam = lambda x: x*x
for n in (1,2,3,4,5,6,7,8,9):
    print (lam(n), end = ", ")

