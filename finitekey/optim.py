from setparms import *
from util import *

def optim(flag, case, selector=[], xi = 0):
    minarg = 0
    minval = 100
    Q=0.01
    ##Q = 0.11
    result = []
    arr = []
    while(Q <= 0.12):
    ##while(Q == 0.04):
        minarg = 0
        minval = 100
        foo = lambda x : round(x,3)
        es = [0,0,0,0]
        while(es[3] <= Q**2):
            es[1] = 0
            while(es[1] <= Q*(1-Q)):
                es[2] = 0
                while(es[2] <= Q*(1-Q)):
                    if(flag):
                        Qa = 2*Q*(1-Q) + xi
                    else:
                        Qa = Q + xi
                    es[0] = -2*(Qa-0.5) - (es[3] + es[1] + es[2] + setparms(Q,case, selector))
                    ls = [0,0,0,0]
                    ls[0] = 0.5 + abs(es[0]/(2*(1-Q)*(1-Q)))
                    ls[1] = 0.5 + abs(es[1]/(2*Q*(1-Q)))
                    ls[2] = 0.5 + abs(es[2]/(2*Q*(1-Q)))
                    ls[3] = 0.5 + abs(es[3]/(2*Q*Q))
                    ss = [0,0,0,0]
                    for i in range(4): ss[i] = S(ls[i])
                    k_rate = ((1-Q)**2)*ss[0]
                    k_rate += Q*(1-Q)*(ss[1] + ss[2])
                    k_rate += (Q**2)*ss[3]
                    k_rate -= h(Q)
                    # if(k_rate > 0): print(k_rate)
                    if(k_rate <= minval):
                        minval = k_rate
                        minarg = Q
                        arr.append((minval, minarg))
                    es[2] += 0.01
                es[1] += 0.01
            es[3] += 0.01
            ##Take a look at different step size later
        arr2 = [(i,j) for (i,j) in arr if i>=0]
        if(len(arr) == len(arr2)):
            result.append(min(arr2))
        Q += 0.001
    if(len(result) == 0):
        return [0,0]

    ##We want the largest feasible noise. The largest is the final one
    res = [round(result[-1][1], 3),result[-1][0]]
    return res

