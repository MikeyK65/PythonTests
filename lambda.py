
#sentence = "This is a test"
#words = sentence.split()
#
#lengths = map(lambda word: len(word), words)
#print (lengths)

# STANDARD FUNCTION
def F (temp):
    return ((float(9)/5) * temp + 32)

celsius = (36.5,37,35,33)
f = map(F, celsius)

for t in f:
    print (t)
    

#LAMDA FUNCTION
celsius = [36.5,37,35,33]
f = map(lambda x:(float(9)/5) * x + 32, celsius)
for t in f:
    print(t)
    
