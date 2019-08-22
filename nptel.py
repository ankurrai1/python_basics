def intreverse(num):
    result = 0
    while(num > 0):
        temp = num % 10
        result = (result * 10) + temp
        num = int(num / 10)
    return result

def matched(s):
    stack = []
    for item in s:
        if item == ")" and len(stack)<1: 
            return False
        if item == "(":
            stack.append(item)
        if item == ")" and stack[-1] == "(":
            stack.pop()
    if len(stack) > 0: return False
    else: return True

def isPrime(num):
    if num < 2: return False
    div = 2
    while div < num:
        if num%div==0:
            return False
        div += 1
    return True

def sumprimes(l):
    sum = 0
    for item in l:
        if(isPrime(item)):
            sum += item
    return sum



print(sumprimes([-3,1,6]))