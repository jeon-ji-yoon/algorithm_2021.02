import sys
sys.stdin = open("input.txt", "r")


def DFS(L):
    global res
    if( L == N ):
        dif = max(pa) - min(pa)
        if res > dif:
            temp = set()
            for x in pa:
                temp.add(x)
            if len(temp) == 3:
                res = dif

    else:
        for i in range(3):
            pa[i] += cv[L]
            DFS(L+1)
            pa[i] -= cv[L]

'''
함수명 : DFS
함수의 기능 : 세개의 가지(세 사람에게 동전을 분배) 를 뻗는
인자 : L : 동전의 갯수를 나타내는 인자임
반환값 : 없음
작성날짜 : 2020/02/04
작성자 : 전지윤
'''

if __name__ == "__main__":
    N = int(input())
    cv = list()
    pa = [0]*(3) #person amount
    res = 2147000000
    for i in range(N):
        cv.append(int(input()))
    
    DFS(0)
    print(res)

'''
함수명 : main
함수의 기능 : N으로 동전의 갯수를 받는다/ N개 동전의 액수를 입력받는다
인자 : 없음
반환값 : 없음
작성날짜 : 2020/02/04
작성자 : 전지윤
'''
