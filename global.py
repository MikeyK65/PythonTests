v = "Test"

def localF():
    v = "Local Test"
    print (v)

def globalF():
    global v
    v = "Global Test"
    print (v)

print (v)
localF()
print ("After local: ", v)
globalF()
print ("After global: ", v)

