import math

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True

n = int(input("Enter the number:"))
count = 0
num = 2
while count < n:
     if isPrime(num):
        print(num)
        count += 1
     num += 1