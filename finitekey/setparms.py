from math import sqrt 
##selector should be an array of tuples, first element is selected component, second is scale factor
def setparms(Q,case, selector = []):

    params = {    0 : 0.5,
        1 : 0.5,
        2 : 1-Q,
        3:  Q,
        4 : Q,
        5 : 1-Q,
        6 : 0.5,
        7 : 0.5,
        8 : 0.5,
        9 : 0.5,
        10 : 0.5,
        11 : 0.5,
        12 : (Q**2) + ((1-Q)**2),
        13 : 2*Q*(1-Q),
        14 : 2*Q*(1-Q),
        15 : (Q**2) + ((1-Q)**2) }

    pairs = {2:3, 3:2, 4:5, 5:4, 12:13, 13:12, 14:15, 15:14}
    for i,s in selector:
        ##TODO if <=0 = 0 if >= 1 = 1
        if(params[i] +s <= 0):
            params[i] = 0
        elif(params[i] + s >= 1):
            params[i] = 1
        else:
            params[i] += s
        if(i in pairs):
            params[pairs[i]] = 1 - params[i]
        # if(params[i] <= 0):
        #     params[i] = 0


    pa0 = params[0]
    pa1 = params[1]
    p00 = params[2]
    p01 = params[3]
    p10 = params[4]
    p11 = params[5]
    p00a = params[6]
    p01a = params[7]
    p10a = params[8]
    pa0a = params[9]
    pa1a = params[10]
    p11a = params[11]
    P0R0 = params[12]
    P0R1 = params[13]
    P1R0 = params[14]
    P1R1 = params[15]
    ##Case: 0 All statistics
    ##Case: 1 No P_ZRX
    ##Case: 2 No P_?ZX
    ##Case: 3 No P_?ZX No P_ZRX
    if(case == 0):
        e00e02 = 2*(pa0*pa0a) - (0.5*(p00 + p10)) - (p00*(p00a - 0.5)) - \
            (p10*(p10a - 0.5)) - (pa0) + (0.5*(p00 + p10))
        e11e13 = 2*(pa1*pa1a) - (0.5*(p01 + p11)) - (p01*(p01a - 0.5)) - \
            (p11*(p11a - 0.5)) + (pa0) - (0.5*(p00 + p10))
        g0g1 = 0
        extra = 0
    elif(case == 1):
        e00e02 = 2*(pa0*pa0a) - (0.5*(p00 + p10)) - (p00*(p00a - 0.5)) - \
            (p10*(p10a - 0.5)) - (pa0) + (0.5*(p00 + p10))
        e11e13 = 2*(pa1*pa1a) - (0.5*(p01 + p11)) - (p01*(p01a - 0.5)) - \
            (p11*(p11a - 0.5)) + (pa0) - (0.5*(p00 + p10))
        g0g1 = sqrt(P0R0 * P0R1) + sqrt(P1R0 * P1R1)
        extra = 0
    elif(case == 2):
        e00e02 = 2*(1-Q)*Q
        e11e13 = 2*(1-Q)*Q
        g0g1 = 0
        extra = 0
    else:
        e00e02 = 2*(1-Q)*Q
        e11e13 = 2*(1-Q)*Q
        g0g1 = sqrt(P0R0*P0R1) + sqrt(P1R0 * P1R1)
        extra = 0

    ##If we know that the channel is symmetric then g0g1 + g2g3 = 0 for free
    ## Otherwise we bound it with cauchy schwartz. If the channel happens to be
    ## symmetric but we didn't know that extra = 0 and g0g1 is not bounded to 0
    combinedTerm = g0g1 + extra
    return e00e02 + e11e13 + combinedTerm
