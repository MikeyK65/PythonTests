def myBigSum (n):
    num, nums = 0, []

    while num < n:
        nums.append(num)
        num += 1

    return nums

def myBigSumGenerator (n):
    num = 0

    while num < n:
        yield num
        num += 1


print (sum(myBigSum(10000000)))
print (sum(myBigSumGenerator(10000000)))
