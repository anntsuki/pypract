class Deque:
    def __init__(self, lists):
        self.lists = lists

    def append(self, a):
        self.lists.append(a)

    def popleft(self):
        return self.lists.pop(0)

    def len(self):
        return len(self.lists)

def yuesefu(n, m):
    t = Deque([n for n in range(1, n+1)])
    for _ in range(n):
        for i in range(m-1):
            t.append(t.popleft())
        print(t.popleft())

yuesefu(6, 5)