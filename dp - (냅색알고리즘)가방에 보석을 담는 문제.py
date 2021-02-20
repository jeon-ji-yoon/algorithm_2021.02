import sys
sys.stdin =open("input.txt", "r")
'''
프로그램의 기능 : 가방에 담을 수 있는 무게의 최대치가 주어졌을 때 가방에 얼마만큼의 가치를 가진
보석을 담을 수 있는지 구하는 프로그램

변수  n :보석의 종류

      weight:가방이 담을 수 있는 최대무게

      li:보석 각각의 무게와 가치를 tuple자료형으로 담는 list

      dy:예를 들어 dy[n]에는 n만큼의 무게를 담을 수 있는 가방이 주어졌을 때
      채울 수 있는 보석의 최대 가치가 들어간다

      tempW : 임시로 보석의 무게를 담는 변수

문제 해결 방안 : 동적 프로그래밍을 이용한다. 이때 dy라는 리스트에 무슨 값을 담는지
가 이 문제를 푸는 핵심이다
'''

n, weight = map(int, input().split())
global li
li= []
for i in range(n):
    a,b =map(int, input().split())
    li.append((a,b))

dy = [0] * (weight +1)

for j in li:
    tempW = j[0]
    for k in range(tempW, weight+1):
       
        if(dy[k] < dy[k - tempW] + j[1]):
            dy[k] = dy[k - tempW] + j[1]


print(max(dy))
