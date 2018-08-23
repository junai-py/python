def count_prime(x):
    prime=[]
    count=0
    for i in range(2,x+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime.append(i)
            count += 1
    print(prime)
    print(f'NO OF PRIME {count}')
num=int(input('ENTER A NUM : '))
count_prime(num)