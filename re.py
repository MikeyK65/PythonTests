__author__ = 'MikeK'

import re

str = "This is some text written by Mike Kennedy - you can find him at mike@test.com or mike@test2.com and definitely not at mike3@wibble not an email."

# Find first email
match = re.search(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]+', str)

print ('Match First...')
if match:
    print (match.group())
    

print ('Match All...')
matches = re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]+', str)
for m in matches:
    print(m)
        
