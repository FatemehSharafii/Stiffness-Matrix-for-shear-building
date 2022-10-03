import numpy as np

def stiffness(N,K0):
    # N is the number of degrees of freedom
    # K0 is the interstory stiffness of columns
    K=np.zeros([N,N])
    Ks=K0*np.ones([N+1])
    Ks.itemset(N,0);
    for i in range(N):
        for j in range(N):
         if i==j:
             K[i,j]=Ks[i]+Ks[i+1]
         elif i>j and i==j+1:
             K[i,j]=-Ks[i]
         elif j>i and j==i+1:
             K[i,j]=-Ks[j]
         else:
             K[i,j]=0
    print(K)
