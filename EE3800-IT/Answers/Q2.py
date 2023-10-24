def lrt(T):
    p=[[0.5,0.35,0.15],[0.2,0.3,0.5]]
    h=list()
    for i in [0,1]:
        h.append([[[x1*x2*x3 for x1 in p[i]] for x2 in p[i]] for x3 in p[i]])
    l=[[[h[0][x1][x2][x3]/h[1][x1][x2][x3] for x1 in range(3)] for x2 in range(3)] for x3 in range(3)]
    a=0
    b=0
    for m in range(3):
        for n in range(3):
            for o in range(3):
                if l[m][n][o]<T:
                    a+=h[0][m][n][o]
                else:
                    b+=h[1][m][n][o]
    return a,b