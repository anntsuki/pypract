# acwing827.双链表
N = 100010


def insert(k, x):
    global idx
    e[idx], r[idx], l[idx], l[r[k]], r[k], idx = x, r[k], idx, idx, idx + 1


def delete(k):
    r[l[k]], l[r[k]] = r[k], l[k]


if __name__ == '__main__':
    m = int(input())
    e, l, r, idx = [0] * N, [0] * N, [0] * N, 2
    r[0], l[1] = 1, 0

    for _ in range(m):
        op, *p = input().split()
        p = [int(x) for x in p]
        if op == 'L':
            insert(0, p[0])
        elif op == 'R':
            insert(l[1], p[0])
        elif op == 'D':
            delete(p[0] + 1)
        else:
            insert(p[0] + 1, p[1])
    while r[0] != 1:
        print(e[r[0]], end=' ')
        r[0] = r[r[0]]
