print (dir())
import time
print (dir())  # Will now show as above plus 'time'
import re
print (dir())  # Will now show as above plus 're'


s = "Hey I'm a string!"
n = 123
a = [1,2,3,4,5,6,7]
d = {'Mike':'10', "Dave":'20'}

print (type(s))
print (type(n))
print (type(a))
print (type(d))

if type(s) == str:
    print("Success - s is a string!")

if type(d) == dict:
    print("Success - d is a dictionary!")
    for key,value in d.items():
        print (key + ":" + value)

        
