H,W=map(int,input().split())

N=int(input())

A=[["."]*W for _ in range(H)]

for i in range(N):
    
    x,y,d,w=input().split()
    #print(x,y,d)
    x,y,d=int(x)-1,int(y)-1,int(d)
    #print(w)
    #print(x,y,d)
    
    if d == 0:
        #print("d0")
        for j in range(x,x+len(w)):
            A[j][y]=w[j-x]
            #print(A,w[j-x])
    
    if d == 1:
        #print("d1")
        for j in range(y,y+len(w)):
            A[x][j]=w[j-y]
        #print(A,w)

#print(A)

for i in range(H):
    ans=""
    for j in range(W):
        ans+=A[i][j]
    print(ans)


