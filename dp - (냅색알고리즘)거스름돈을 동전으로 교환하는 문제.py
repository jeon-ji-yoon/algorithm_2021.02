import sys
sys.stdin = open("input.txt", "r")

n = int(input())
coinLi = list( map(int, input().split()   )    )
v = int(input())

dy = [2147000000]*(v+1)
dy[0] = 0

for i in coinLi:

    for j in range(i,v+1):
        if(  dy[j] >   dy[j - i] + 1      ):
            

            dy[j] = dy[j - i] + 1

print(dy[v])
    
    
