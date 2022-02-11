
class Node:
    def __init__(self, val, prev=None, next=None):
        self.value = val
        self.prev = prev
        self.next = next


class DoublyList:
    def __init__(self, a):
        self.head = Node(None, None, None)
        tail = Node(a[0], None, None)
        self.head.next = tail
        tail.next = self.head
        self.head.prev = tail
        tail.prev = self.head
        for i in range(1, len(a)):
            n = Node(a[i])
            tail.next = n
            n.prev = tail
            tail = tail.next
        tail.next = self.head
        self.head.prev = tail


    def showList(self):
        n = self.head.next
        if self.head.next == None:
            print("Empty List")
        else:
            while (n != self.head):
                print(n.value, end=' ')
                n = n.next
            print()

    def insert(self, newElement):
        n = Node(newElement)
        tail = self.head.prev
        tail.next = n
        self.head.prev = n
        n.prev = tail
        n.next = self.head

    def insertWithIndex(self, newElement, index):
        node = Node(newElement)
        temp = self.head.next
        for i in range(0, index-1):
            if temp != self.head.next:
                temp = temp.next
        if (temp.next != self.head.next):
            node.next = temp.next
            node.prev = temp
            temp.next = node
            if (node.next != None):
                node.next.prev = node

    def remove(self, index):
        temp = self.head.next
        if (index == 0):
            self.head.next = temp.next
            temp = None
            return
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break
        if (temp is None):
            return
        if (temp.next == None):
            return
        n = temp.next.next
        temp.next = None
        temp.next = n

    def removeKey(self, deleteKey):
        temp = self.head.next
        if (temp != None):
            if (temp.value == deleteKey):
                self.head = temp.next
                temp = None
                return
        while (temp == self.head.next):
            if temp.value == deleteKey:
                break
            prev = temp
            temp = temp.next
        if (temp == self.head.next):
            return
        prev.next = temp.next
        temp = None


#####################################################################
x = DoublyList([10, 30, 40, 50])
x.showList()
x.insert(60)
x.showList()
x.insertWithIndex(20, 2)
x.showList()
x.remove(3)
x.showList()
x.removeKey('20')
x.showList()
