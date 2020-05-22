import xml.parsers.expat

def start_element(name, atts):
    print ("Start Elem = ", name, atts)

def end_element (name):
    print ("End Elem = ", name)

def char_data (data):
    print ("Char data = ", repr(data))

p = xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

xmlData = """<?xml version = "1.0"?><army id = "Rebel Alliance"><echoThree name = "Luke Skywalker">Jedi in training</echoThree><echoSeven name = "Han Solo">Smuggler</echoSeven></army>"""

p.Parse(xmlData, 1)
