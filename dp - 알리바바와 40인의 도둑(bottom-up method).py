import sys
sys.stdin = open("input.txt", "r")
n = int(input())
valley = []
for i in range(n):
    tempList = list(map(int, input().split()))
    valley.append(tempList)

dy = [0] * (2*n)
dy[0]=(valley[0][0])

for i in range(1,n):
    dy[i] = dy[i-1] + min(valley[i-1][i], valley[i][i-1]) +valley[i][i]

print(max(dy))
