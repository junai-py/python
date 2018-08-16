num=int(input('ENTER A NUMBER:'))
fact=1
if num==0:
    print('THE FACTORIAL OF 0 IS 1')
elif num<1:
    print('ENTER A POSITIVE NUMBER')
else:
    for i in range(1,num+1):
        fact=fact * i
    print('THE FACTORIAL OF',num,'is',fact)
