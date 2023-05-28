# finding factorial using recusion

def fact(n):
    if n == 0 or n==1: # base
        return 1
    else:
        return n * fact(n-1) # recursive
    
print(fact(5))

