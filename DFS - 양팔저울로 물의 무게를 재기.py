'''
import sys
sys.stdin = open("input.txt", "r")
'''
def DFS(L, sum):
    if L == K:
        if(0<sum <= s):
            res.add(sum)
        

    else:
        DFS(L+1, sum-a[L])  
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

''' 양팔 저울 중 왼쪽으로 넣을 경우, 양팔 저울중 오른쪽으로 넣을 경우, 양팔 저울에 넣지 않는
경우, 이 세가지로 분류해서 DFS함수를 설계한다'''

if __name__ == "__main__":
    K = 3
    a = [1,5,7]

    s = sum(a)
    res = set() #중복되는 결과값들(잴 수 있는 무게)을 포함하지 안으려고 set 자료구조를 사용한다
  
    DFS(0, 0)
    print(s-len(res))
