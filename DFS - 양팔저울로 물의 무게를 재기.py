import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    if L == K:
        if(sum > 0):
            res[sum] = 1
        

    else:
        DFS(L+1, sum-a[L])  
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

''' 양팔 저울 중 왼쪽으로 넣을 경우, 양팔 저울중 오른쪽으로 넣을 경우, 양팔 저울에 넣지 않는
경우, 이 세가지로 분류해서 DFS함수를 설계한다'''

if __name__ == "__main__":
    K = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    res = [0]*(s+5)
    cnt = 0
    
    DFS(0, 0)
    
    for i in range(1, s+1): #1부터 s까지 각각의 무게를 잴 수 있는지 체크한다
        if res[i] == 0:
            cnt += 1
    print(cnt)
