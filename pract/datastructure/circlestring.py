class LNode:
    def __init__(self, n):
        self.data = n
        self.next = None

    def getdata(self):
        return self.data


class CircularLink:
    def __init__(self, hd=None):
        self.head = hd
        self.q = None

    def addNode(self, a):
        newNode = LNode(a)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            return
        p = self.head
        self.q = self.head
        while p.next != self.head:
            p = p.next
        p.next = newNode
        p.next.next = self.head

    def delNode(self, b):
        for _ in range(b - 2):
            self.q = self.q.next
        if self.q.next == self.head:
            print(self.head.data, end=' ')
            self.head = self.head.next
            self.q = self.head
        else:

            print(self.q.next.data, end=' ')
            self.q.next = self.q.next.next
            self.q = self.q.next


t = CircularLink()
n = 6
m = 5
for i in range(1, n + 1):
    t.addNode(i)
for i in range(1, n + 1):
    if m == 1:
        print(i)
    else:
        t.delNode(m)
