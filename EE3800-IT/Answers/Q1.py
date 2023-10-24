import numpy as np

def digits(num):
    lst=list()
    for i in range(4):
        lst.append(int(num%10))
        num=num//10
    return lst

def mutual_information(pmf,i,j):
    xy=[[0 for col in range(10)]for row in range(10)]
    x=[0 for colx in range(10)]
    y=[0 for coly in range(10)]
    for l in range(len(pmf)):
        xy[digits(l)[i]][digits(l)[j]]+=pmf[l]
    for n in range(10):
        for l in range(10000):
            if(digits(l)[i]==n):
                x[n]+=pmf[l]
            if (digits(l)[j]==n):
                y[n]+=pmf[l]           
    mi=0
    for m in range(10):
        for n in range(10):
            if xy[m][n]!=0:
                mi+=xy[m][n]*np.log2(xy[m][n]/(x[m]*y[n]))
    return mi

