myList = [['Prashant', 32.0], ['Pallavi', 36.0], ['Dheeraj', 39.0], ['Shivam', 40.0]]

min = myList[0][1]

for x in range (1, len(myList)):
    if myList[x][1] < min:
        min = myList[x][1]


for x in range (0, len(myList)):
    if (myList[x][1]) == min:
        myList.pop(x)
        break

# Get new min
min = myList[0][1]
for x in range (1, len(myList)):
    if myList[x][1] < min:
        min = myList[x][1]

#print(myList, " ", min)

for x in range (0, len(myList)):
    if (myList[x][1]) == min:
        print(myList[x][0])


