lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
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
    