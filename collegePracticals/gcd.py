# TASK : is to write program to find the gcd of 2 no


def gcd(n1, n2):
    if(n1 == 0) :
        return n2 
    else : return gcd(n2 % n1, n1)

print(gcd(7 , 49))