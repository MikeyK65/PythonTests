import types

class MyMathClass():
    def add(self, x, y):
        return x+y

    def monkey_path_adder(self):
        oldAdd = self.add

        def morePowerfulAdd (self, x, y):
            return oldAdd(x,y) + 1
    
        self.add = types.MethodType (morePowerfulAdd, self)

myMath = MyMathClass()
print (myMath.add (3,3))

myMath.monkey_path_adder()
print (myMath.add (3,3))
