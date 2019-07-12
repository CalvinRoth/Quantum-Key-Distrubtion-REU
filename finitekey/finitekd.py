import pandas as pd
from optim import optim


N = 10**2
e = 0.01


##Main function for optimizing key rate. Output files are currently commented out
def keyrate(filename = None, verb=False):
    out = filename != None
    ##Used for printing results
    if(out):
        outlog = open(filename, "w")
    rhead  = ["pa0","pa1","p00","p01","p10","p11","p00a","p01a","p10a","pa0a","pa1a","p11a","P0R0","P0R1","P1R","P1R1"]
    chead = ["-1","-10^-1","-10^-2","-10^-3", "0","10^-3","10^-2","10^-1","1"]

    for flag in [False, True]: ##Is this correlated or uncorrelated
        if(out):
            print("Are these cases correlated:", flag, file=outlog)
        if(verb):
            print("Are these cases correlated:", flag)
        for case  in range(4):
            if(out):
                print("This is case ", case+1, "\n", file=outlog)
            if(verb):
                print("This is case ", case+1, "\n", file=outlog)
            results = []
            for i in range(16):
                result = []
                noises = [100 for i in range(9)] ##100 is >> than any noise we will find
                k_rates= [0 for i in range(9)] ## 0 <= any key rate we will find
                space = gensels()
                ##For each spacing we want to consider of parameter i
                for j,s in enumerate(space):
                    noise, k_rate =  optim(flag, case, [(i,s)], 0)
                    if(noise < noises[j]):
                        noises[j] = noise
                        k_rates[j] = k_rate
                ##For that parameter what were the best noises and k rates at each spacing
                for j in range(9):
                    result.append((noises[j],k_rates[j]))
                results.append(result)
            table = pd.DataFrame(results,columns=list(chead),index=list(rhead)).to_csv()
            if(out):
                print(table, file=outlog)
            if(verb):
                print(table)
    if(out): outlog.close()

##Generates the set of spacing we consider
def gensels():
    arr = []
    for sign in range(1,3):
        res = []
        for s in range(0,4,1):
            scale = ((-1)**sign)*(10**(-s))
            res.append(scale)
        if(sign == 2):
            res = res[::-1]
            res += [0]
        arr += res
    return arr

##If you want the file output as a file, provide a file name
##If you want the file output to terminal, set verb = True
keyrate()
