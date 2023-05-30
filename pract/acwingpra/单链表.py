# acwing826 单链表 （用数组模拟单链表）
m = int(input())
N = 100010
# head表示头结点下标， e[i]表示结点i的值（e存储值）
# ne[i]表示结点i的next指针（ne存储指针），idx表示当前已用到了数组的哪个点
e, ne, idx, head = [0] * N, [0] * N, 0, -1


def insert_to_head(x):
    global idx, head
    e[idx], ne[idx], head, idx = x, head, idx, idx + 1


def remove_node(k):
    global idx
    ne[k] = ne[ne[k]]


def insert_node(k, x):
    global idx
    e[idx], ne[idx], ne[k], idx = x, ne[k], idx, idx + 1


for _ in range(m):
    op, *p = input().split()
    if op == 'H':
        x = int(p[0])
        insert_to_head(x)
    elif op == 'I':
        k, x = map(int, p)
        insert_node(k - 1, x)
    else:
        k = int(p[0])
        if not k:
            head = ne[head]
        else:
            remove_node(k - 1)
while head != -1:
    print(e[head], end=' ')
    head = ne[head]
