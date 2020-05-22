# default params
def func(x, y=10, z="mystring"):
    return x+y


def myConcat(*args):
    return ", ".join (args)

print (myConcat("earth", "wind", "fire"))

