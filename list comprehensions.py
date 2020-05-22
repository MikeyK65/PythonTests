x = 2
y = 2
z = 2
n = 6


listy = [ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range (z + 1) if ( ( i + j + k) != n )]

print (listy)