import lxml.etree

tree = lxml.etree.parse("rebels.xml")
x = tree.findall("rebel")
print ("findall rebel = ")
print (x)

x = tree.findall("//{rebel}*[@lastname]")
print("Findall rebels with last name = ")
print (x)

x = tree.findall("//{rebels}*[@lastname='Skywalker']")
print("Find skywalker = ")
print (x)


