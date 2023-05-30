N = 1000010
n, k = map(int, input().split())
hh, tt = 0, 1
arr, q = [int(x) for x in input().split()], [0] * N
for i in range(n):
    if i - k + 1 > q[hh]:
        hh += 1
        while hh<=tt and arr[i]



