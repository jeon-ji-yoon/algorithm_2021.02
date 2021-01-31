import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum1, sum2):
    if(L == N):
        if( sum2 <=M):
            res.append(sum1)

    else:
        #for j in range(N): 0 1 2 3 4 
        DFS(L+1, sum1 + s[L], sum2 + t[L])
        DFS(L+1, sum1, sum2)
        


if __name__ == "__main__":
    N, M=map(int, input().split())
    s=[] #리스트에 N개의 자료가 들어있다
    t=[]
    res = []

    for i in range(N):
        a, b = map(int, input().split())
        s.append(a)
        t.append(b)

    DFS(0,0,0)
    print(max(res))
