#行、列の入力
n,m=map(int,input().split())

#マップの入力
maze=[list(input()) for i in range(n)]

#マップの距離情報をdistに :-1は壁
dist=[[-1]*m for i in range(n)]

now=[0,0]
queue=[]
cnt=1

for i in range(n):
    for j in range(m):
        if maze[i][j]=='S':
            now[0]=i
            now[1]=j
            queue.append([i,j])
        elif maze[i][j]=='.':
            dist[i][j]=0

#幅優先探索と距離の記録
while len(queue):
    for i in range(len(queue)):
        qx,qy=queue.pop(0)
        if dist[qx-1][qy]==0:
            queue.append([qx-1,qy])
            dist[qx-1][qy]=cnt
        if dist[qx+1][qy]==0:
            queue.append([qx+1,qy])
            dist[qx+1][qy]=cnt
        if dist[qx][qy-1]==0:
            queue.append([qx,qy-1])
            dist[qx][qy-1]=cnt
        if dist[qx][qy+1]==0:
            queue.append([qx,qy+1])
            dist[qx][qy+1]=cnt
    cnt+=1

#マップの出力
#for i in dist:
#    for j in i:
#        print(j,end='')
#    print()