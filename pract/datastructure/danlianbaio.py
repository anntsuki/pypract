class LNode:
    def __init__(self, data, nxt=None):
        self.elem = data
        self.next = nxt  # 下一个节点对象名

    def getData(self):
        return self.elem


class Danlianbiao:
    def __init__(self, hd=None):
        self.head = hd
        self.num = 0  # 链表中节点的个数

    def addHead(self, elem):  # 在头结点前增加节点
        newNod = LNode(elem)
        if self.head is None:
            self.head = newNod
        else:
            newNod.next = self.head  # newNode指向了原来的头结点
            self.head = newNod
        self.num += 1

    def addRear(self, elem):  # 在尾节点后面增加一个节点
        newNode = LNode(elem)
        if self.head == None:
            self.head = newNode
            self.num += 1
            return
        # p定位到尾节点
        p = self.head
        while p.next != None:
            p = p.next
        p.next = newNode
        self.num += 1

    def popHead(self):
        if self.head == None:
            print('没有头结点，不能删')
            return
        self.head = self.head.next
        self.num -= 1

    def printLianbiaoDatas(self):
        if self.head == None:
            print('单链表空，没有元素可打印')
            return
        p = self.head
        while p is not None:
            print(p.elem, end=' ')
            p = p.next


if __name__ == '__main__':
    list1 = Danlianbiao()  # 空单链表
    for i in range(100):
        list1.addHead(i)
    list1.printLianbiaoDatas()
    print('-----------------------')
    for i in range(100):
        list1.addRear(100 + i)
    list1.printLianbiaoDatas()
