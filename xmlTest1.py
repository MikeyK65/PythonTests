

import xml.etree.ElementTree as et

tree = et.parse("C:\\Users\\mikey\\OneDrive\\src\\Python\\tests\\statements\\xmlTest1.xml")
root = tree.getroot()

print (root.attrib)
