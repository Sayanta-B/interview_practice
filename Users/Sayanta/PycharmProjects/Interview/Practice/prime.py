

def isprime(n):
    for i in range(2,n-1):
        if n%2 ==0:
            return False
        else:
            return True

if __name__=="__main__":
    if isprime(8):
        print("the no is prime")
    else:
        print("The no is not prime")