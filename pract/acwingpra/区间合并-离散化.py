# acwing 802 区间和
n, m = map(int, input().split())
a, s = [0] * 300010, [0] * 300010
alls, add, query = [], [], []
for _ in range(n):
    x, c = map(int, input().split())
    add.append((x, c))
    all.append(x)
for _ in range(m):
    l, r = map(int, input().split())
    alls.append(l)  # 这里将l，r加入alls里面是最后要求区间和的，要让他们在alls里面并保持相对顺序来搞出a的下标，让哪些没加c的都为0
    alls.append(r)

# 实现源代码中的去重排序
alls = list(set(alls))
alls.sort()


# 找到离散化后的x的坐标
def find(x):
    l, r = 0, len(alls) - 1
    while l < r:
        mid = (l + r) // 2
        if alls[mid] <= x:
            r = mid
        else:
            l = mid + 1
    return r+1


# 将所有数插入，没加c的都为0
for x, c in add:
    index = find(x)
    a[index] += c

# 处理前缀和
for i in range(1, 300010):
    s[i] += s[i-1] + a[i]
for l, r in query:
    print(s[find(r)]-s[find(l)-1])

