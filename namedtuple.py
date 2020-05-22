from collections import namedtuple

#input

#ID         MARKS      NAME       CLASS     
#1          97         Raymond    7         
#2          50         Steven     4         
#3          91         Adrian     9         
#4          72         Stewart    5         
#5          80         Peter      6   

N = 5
header = "ID MARKS NAME CLASS"

marks = namedtuple('Marks', header)
l = list()
#for x in range(N):
#    l.append(marks._make(input().split()))
l = [Marks(ID='1', MARKS='97', NAME='Raymond', CLASS='7'), Marks(ID='2', MARKS='50', NAME='Steven', CLASS='4'), Marks(ID='3', MARKS='91', NAME='Adrian', CLASS='9'), Marks(ID='4', MARKS='72', NAME='Stewart', CLASS='5'), Marks(ID='5', MARKS='80', NAME='Peter', CLASS='6')]

total = 0
for m in l:
    total += int(m.MARKS)
    
print (total / N)