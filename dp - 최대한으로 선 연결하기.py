import sys
sys.stdin = open("input.txt", "r")

if __name__ == "__main__":
    n = int(input())
    v = list(map(int, input().split() ))

    v.insert(0,0)
    dy = [0]*(n+1)
    dy[1] = 1

    for i in range(2, n+1):
        temp = list()
        for j in range(1,i):
            if v[j] < v[i]:
                temp.append(dy[j])
        if(len(temp)!=0):
            dy[i] = max(temp)+1
        else:
            dy[i] +=1

    print(max(dy))
