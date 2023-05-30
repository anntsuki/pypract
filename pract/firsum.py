n = 100010
b = [0] * n  # 设 b[0] = 0 ,免于边界错误和可以求前几项和
a = [0] + [int(x) for x in input().split()]    # 同，a[0]=0，数组第一位为下标1
c, n = map(int, input().split())
for i in range(1, n+1):
    b[i] = b[i-1] + a[i]
print(b[n]-b[c-1])
