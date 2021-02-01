import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum1, sum2):
    global res
    if(L == N):
        if( sum2 > M):
            return
        if(sum1 > res):
            res = sum1

    else:
        #DFS의 가지가 두개(점수를 포함하는지 아닌지)로만 뻗으므로 for문을 쓸 필요 없음
        DFS(L+1, sum1 + s[L], sum2 + t[L])
        DFS(L+1, sum1, sum2)
        


if __name__ == "__main__":
    N, M=map(int, input().split())
    s=[] #리스트에 N개의 자료가 들어있다
    t=[]
    res = -2147000000

    for i in range(N):
        a, b = map(int, input().split())
        s.append(a)
        t.append(b)

    DFS(0,0,0)
    print(res)
