def funct(x):
    word=x.lower().split()
    print(word)
    if(word[0][0]==word[1][0]):
        print('TRUE')
    else:
        print('FALSE')
    
a=input('ENTER A STRING : ')
print(a)
funct(a)
