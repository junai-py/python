def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print('Thank you, your number squared is: ',n**2)
            break
            
   
        
ask()     
    
   