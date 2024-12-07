N = int(input("Enter the number of prime numbers to find: "))

primes = []  
num = 2     

while len(primes) < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:  
            is_prime = False
            break
    if is_prime:
        primes.append(num) 
    num += 1  

print("Prime numbers:", *primes)