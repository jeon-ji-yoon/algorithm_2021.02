import sys
sys.stdin = open("input.txt", "r")

def DFS(s): #s는 sum, 즉 동전의 액수의 합계를 나타내는 매개변수이다
    if(s == T):
        #여기서 set 자료구조를 사용하면 될 것 같다
        res.add(tuple(ch))

    if(T < s):
        return

    else:
        for i in range(k):
            if(ch[i] < cn[i]):
                ch[i] +=1
                DFS(s + cv[i])
                ch[i] -=1



if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list() #cv == coin value
    cn = list() #cn == coin number(동전의 갯수)
    ch = [0]*k

    res = set()
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)

    DFS(0)
    
    print(len(res))
