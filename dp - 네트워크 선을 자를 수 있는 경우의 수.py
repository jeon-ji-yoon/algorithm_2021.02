import sys
sys.stdin = open("input.txt")

if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n+1)

    dy[1] = 1
    dy[2] = 2

    for i in range(3,n+1):
        dy[i] = dy[i-1] + dy[i-2]

    print(dy[n])

'''
함수 이름 : main
인자 : 없음
기능 : 1차원 배열을 만든 뒤 for문을 통해 1차원 배열에
요소를 채워 넣는다/ 요소를 넣을때는 점화식의 원리를 적용했다
/ f(n) = f(n-1)+ f(n-2)

작성자 : 전지윤
작성일 : 2021 02 25
'''
