def print_formatted(number):
    
    binNum = "{0:b}".format(number)
    
    lenBigBen = str(len(binNum))
    formatString = ""
    
    for i in range (1, number+1):
        formatString = "{0:" + str(lenBigBen) + "d} {0:" + str(lenBigBen) + "o} {0:" + str(lenBigBen) + "x} {0:" + str(lenBigBen) + "b}"
        
        print(formatString.format(i))
    
    return

num = 20
print_formatted(num)
