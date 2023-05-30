class DNode:
    def __init__(self, data, nxt=None, prev=None):
        self.elem = data  # 存放数据
        self.next = nxt  # 下一个（右边）结点对象名
        self.prev = prev  # 上一个（左边）结点对象名


class DLianbiao:
    def __init__(self):
        self.head = None  # 头结点
        self.rear = None  # 尾结点
        # self.len = 0

    def addHead(self, e):  # 新节点(里面的数据是e)，只要原来的头节点
        newNode = DNode(e)
        if self.head is None:  # 原来链表为空
            self.head = newNode
            self.rear = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addRear(self, e):  # 尾节点的右边，增加新节点
        newNode = DNode(e)
        if self.head is None:
            self.head = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode

    def insertNode(self, i, e):  # 在第i个节点位置插入新节点，里面数据是 e
        newNode = DNode(e)
        p = self.head
        for j in range(i - 1):  # p 指向第i 个节点
            p = p.next
        p.prev.next = newNode  # 第i-1个节点，指向新节点
        newNode.prev = p.prev  # 新节点，反指向第i-1 个节点
        newNode.next = p
        p.prev = newNode

    def printLianbiao(self):
        p = self.head
        while p is not None:
            print(p.elem, end=' ')
            p = p.next


list1 = DLianbiao()  # 生成空双链表
for i in range(100):
    list1.addHead(i + 1)
list1.printLianbiao()
list1.insertNode(10, 999)
print('\n ----------------')
list1.printLianbiao()
print('\n ************************')
list2 = DLianbiao()
for i in range(100):
    list2.addRear(i + 1)
list2.printLianbiao()
list2.insertNode(10, 888)
print('\n ----------------')
list2.printLianbiao()
