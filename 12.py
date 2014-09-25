import math

def isprime(x):
    limit = int(math.sqrt(x))
    for i in range(2, limit):
        if x % i == 0:
            return False
    return True

def factors(x):
    factors = []
    while True:
        if isprime(x):
            return factors
        for i in range(2, x/2):
            if x % i == 0:
                x = x / i
                factors.append(i)

inputnum = int(raw_input("Enter a number to factorise: "))
if isprime(inputnum):
    print("the number is prime")
else:
    print("The factors of {} are: {}".format(inputnum, factors(inputnum)))
