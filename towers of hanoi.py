def hanoi (n, start_pole, end_pole, inter_pole):
    global numMoves
    
    if n >= 1:
        numMoves += 1
        hanoi (n-1, start_pole, inter_pole, end_pole)
        print ("Disc moved from ",start_pole, "to",end_pole)
        hanoi (n-1, inter_pole, end_pole,start_pole)

numMoves = 0
hanoi(3, "a", "b", "c")
print ("Number of moves = ", numMoves)