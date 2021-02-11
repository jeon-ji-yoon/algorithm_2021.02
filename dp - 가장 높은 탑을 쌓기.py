import sys
sys.stdin = open("input.txt" ,"r")

n = int(input())
bricks = []
for i in range(n):
    a,b,c = map(int, input().split())
    bricks.append((a,b,c))
bricks.sort(reverse = True)

'''벽돌의 밑면의 넓이가 오름차순으로 주어졌으므로, 벽돌의 무게만 고려하면 된다.
벽돌의 무게를 이용해서 최대길이의 증가수열의 길이를 구하기'''

dy= [0]*(n) #증가수열의 길이를 담는 리스트 dy
dy[0] = bricks[0][1]
for i in range(1, n):
    temp = list()
    for j in range(0,i):
        if bricks[j][2] > bricks[i][2]:
            temp.append(dy[j])
    if(len(temp)!=0):
        dy[i] = max(temp)+bricks[i][2]
    else:
        dy[i] +=bricks[i][2]


print(max(dy))



