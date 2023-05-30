# acwing 830. 单调栈

N = 10010
n = int(input())
a = list(map(int, input().split()))
stk, tt = [0] * N, 0

for i in range(n):
    while tt and stk[tt] >= a[i]:
        tt -= 1
    if tt:
        print(stk[tt], end=" ")
    else:
        print("-1", end=" ")
    tt += 1
    stk[tt] = a[i]
