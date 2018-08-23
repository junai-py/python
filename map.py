def sqr(num):
    return num ** 2
mynum=[1,2,3,4,5]
for item in map(sqr,mynum):
    print(item)
numlist=list(map(sqr,mynum))
print(numlist)