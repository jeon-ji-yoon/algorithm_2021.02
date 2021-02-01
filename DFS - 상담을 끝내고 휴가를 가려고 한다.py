import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum1): 
    if(L > N):
        res.append(sum1)

    else:
        DFS(L + tv[L], sum1+pv[L])
        DFS(L+1, sum1)


'''변수설명
    L : 며칠인지를 나타낸다. L=1이면 1일이라는 소리이다
    sum1 : 가격의 종합을 나타내는 매개변수
'''

if __name__ == "__main__":
    N = int(input())
    tv = [0]*(N+1)#time value, price value
    pv = [0]*(N+1)
    for i in range(1, N+1):
        a, b= map(int, input().split())
        tv[i] = a
        pv[i] = b
    res = list()

    DFS(1, 0)
    print(max(res))
        
