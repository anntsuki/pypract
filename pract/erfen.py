# n, q = map(int, input().split())
# a = [int(x) for x in input().split()]
n, q = 8, 2
a = [1, 2, 2, 6, 6, 7, 8, 9]
for i in range(q):
    k = int(input())
    l, r = 0, n - 1
    # 找左边界 如果满足，则在mid的左边部分找[l,mid],r=mid。否则mid右边找[mid+1,r],l=mid+1
    while l < r:
        mid = (l + r) // 2
        if a[mid] >= k:
            r = mid
        else:
            l = mid + 1
    if a[l] != k:
        print('-1 -1')
        continue
    else:
        print(l, end=' ')
    l, r = 0, n - 1
    # 找右边界 如果满足，则在mid的左边部分找[l,mid],r=mid。否则mid右边找[mid+1,r],l=mid+1
    while l < r:
        # 如果不加1，假设l=r-1，如果此时True会无限递归
        mid = (l + r + 1) // 2
        if a[mid] <= k:
            l = mid
        else:
            r = mid - 1
    print(l)
