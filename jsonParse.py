import json
from io import StringIO

io = StringIO('["streaming API"]')

testJSON = json.dumps (["rebels",
                        {"firstname":"Luke", "lastName":"Skywalker"},
                        {"firstname":"Han", "lastName":"Solo"},
                        {"firstname":"Wedge", "lastName":"Antilles"}],
                       separators=(",",":"))

print ("original JSON = ", testJSON)

testDecoder = json.loads(testJSON)
print ("Decoded JSON = ", testDecoder)

for el in testDecoder:
    print (el)
