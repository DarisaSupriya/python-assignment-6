def computeHCF(x,y):
    while(y):
        x,y=y,x%y
    return x
