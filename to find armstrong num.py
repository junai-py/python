num = int(input('ENTER A NUMBER:'))

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
tot = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    tot += digit ** order
    temp //= 10

# display the result
if num == tot:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
