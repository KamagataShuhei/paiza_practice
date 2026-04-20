N,M=map(int,input().split())

#減点方式なので初期値を100で作成
points=[100]*N

#正解の音程のリストを作成
ans=[]
for _ in range(M):
    ans.append(int(input()))

#一人一人の点数を確定させていく
for i in range(N):

    player=[]
    
    for _ in range(M):
        player.append(int(input()))
    
    for j in range(M):
        
        if abs(ans[j]-player[j])<=5:
            points[i]+=0
        
        elif abs(ans[j]-player[j])<=10:
            points[i]-=1
            
        elif abs(ans[j]-player[j])<=20:
            points[i]-=2
        
        elif abs(ans[j]-player[j])<=30:
            points[i]-=3 
        
        else:
            points[i]-=5
    
    points[i]=max(points[i],0)
    #print(points)デバック用

print(max(points))
