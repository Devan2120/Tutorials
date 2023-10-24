import numpy as np
def HammingDecoder(x):
    H=np.array([
        [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
        [0,0,0,1,1,1,1,0,0,0,0,1,1,1,1],
        [0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]])
    s=np.matmul(H,x) % 2
    j=0
    for i in range(4):
        j+=s[i]*(2**(3-i))
    if j!=0 :
        x[j-1]=0 if x[j-1]==1 else 1
    return(x)