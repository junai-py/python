def funct(x,y):
    if(x%2==0) and (y%2==0):
        print(f'{x} and {y} are both even')
        if min(x,y):
            print(f'{x} is less than of {y}')
        else:
            print(f'{y} is less than of {x}')
    elif max(x,y):
        print(f'{x} is the greatest num')
    else:
        print(f'{y} is the greatest num')
            
a=int(input('ENTER THE FIRST NUM :'))
b=int(input('ENTER THE SECOND NUM :'))
funct(a,b)