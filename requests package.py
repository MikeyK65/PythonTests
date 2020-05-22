import requests

r = requests.get ("http://bbc.co.uk")

print (r)
print (r.text)

