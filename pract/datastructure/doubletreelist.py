class SStack:  # 栈
    def __init__(self, list):
        self.lists = list

    def push(self, a):
        self.lists.append(a)

    def pop(self):
        if self.lists:
            return self.lists.pop()

    def len(self):
        return len(self.lists)

    def pei(self):
        print(self.lists)


class Deque:  # 队列
    def __init__(self, lists):
        self.lists = lists

    def append(self, a):
        self.lists.append(a)

    def popleft(self):
        return self.lists.pop(0)

    def len(self):
        return len(self.lists)


class BiTNode:  # 二叉树
    def __init__(self, dat, lft=None, rht=None):
        self.data = dat  # 节点的数据
        self.left = lft  # 该节点的左子节点
        self.right = rht

    def preorder(self):  # 先序遍历
        print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):  # 中序遍历
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()

    def preorderNonrec(self):  # 先序遍历的非递归形式
        stack = SStack([])  # 栈的类名为SStack
        p = self
        while p or stack:
            while p:
                print(p.data, end=' ')
                stack.push(p)
                p = p.left
            p = stack.pop()
            if p:
                p = p.right


nd1 = BiTNode('G')
nd2 = BiTNode('E', None, nd1)
nd1 = BiTNode('F')
nd3 = BiTNode('D', nd2, nd1)  # 'D'生成后，nd1与nd2可以重用
nd1 = BiTNode('C')
nd2 = BiTNode('B', nd1, nd3)  # 'B'生成后，nd1与nd3可以重用
root = BiTNode('A', nd2)  # 生成根节点，二叉树构造完毕
root.preorder()
print()
root.inorder()
print()
root.preorderNonrec()
