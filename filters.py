def check(num):
    return num %2==0
mynum=[1,2,3,4,5,6,7,8,9]
mylist=list(filter(check,mynum))
print(mylist)