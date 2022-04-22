def isprime(num):
    test=True
    if num>1:
        for i in range(2,num):
            if num%i==0:
                test=False
    return test
