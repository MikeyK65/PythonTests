#sets

words = set("This is a list of words".split())

names = set(["Mike","John","Nick"])

goodnames = set(["Chris","Vicky"])

print(names | goodnames)
print (names.union(goodnames))
print (names - goodnames)

print (names ^ goodnames)
print (names.symmetric_difference(goodnames))
print (names < goodnames)
print (names > goodnames)

set2 = {1}
print (set2)
set2.add(2)
print (set2)
set2.update ({2,3,4,5})
print (set2)
set2.discard(3)
print (set2)

            
