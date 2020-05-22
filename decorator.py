class theDecorator (object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print ("Entering : ", self.f.__name__, " Decoration\n")
        self.f()
        print ("Exiting : ", self.f.__name__, " Decoration\n")


@theDecorator
def f1():
    print ("Inside f1")

@theDecorator
def f2():
    print ("Inside f2")

def f3():
    print ("Inside f3")
    
print ("1: ")
f1()
print ("2: ")
f2()
print ("3: ")
f3()
