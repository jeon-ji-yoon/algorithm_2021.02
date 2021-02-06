import sys
sys.stdin = open("input.txt", "r")


N = int(input())
dy = [0]*(N+1)

dy[1] = 2
dy[2] = 3

for i in range(3, N+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[N])
