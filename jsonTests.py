import json

print (json.__file__)


straightJSON = json.dumps(["rebels",
                           {"firstName":"Luke", "lastName":"Skywalker"}],
                          separators= (",",":"))

print ("Straight JSON = \n", straightJSON)

prettyJSON = json.dumps(["rebels",
                           {"firstName":"Luke", "lastName":"Skywalker"}],
                        sort_keys = True,
                        indent = 4)

print ("Pretty JSON = \n", prettyJSON)

f = open ("generatedJSON.json", "w")
f.write (prettyJSON)
f.close()

