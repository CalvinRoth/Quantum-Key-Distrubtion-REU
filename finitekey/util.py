from math import sqrt,log


def log2(x): return log(x, 2)
def ln(x): return log(x)

def argmin(x): return x.index(min(x))


##Get the shannon entropy of a single varaible
def h(x):
    if((x >= 0.99999) or (x <= 0.000001)):
        ##print("Oh no. We would have had a domain log2 from: ", x, "Returning a big number from now")
        return  0
    y = (1-x)*log2(1-x)
    z = x*log2(x)
    tot = -1*(y+z)
    return tot

##Calculate the full shannon entropy of an array of values
def H(arr):
    if(arr): return -arr[0]*log2(arr[0]) + H(arr[1::])
    return 0

def S(lamb):
     return  1 - h(lamb)
