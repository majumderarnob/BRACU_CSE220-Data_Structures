
class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


class MyList:
    def __init__(self, a):
        self.head = None
        tail = None
        for i in a:
            newNode = Node(i, None)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode

########################################################################

    def showlist(self):
        n = self.head
        while(n is not None):
            print(n.element, end=" ")
            n = n.next
        print()

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def clear(self):
        self.head = None

    def countnode(self):
        c = 0
        n = self.head
        while(n is not None):
            c += 1
            n = n.next
        return c

    def nodeAt(self, index):
        size = self.countnode()
        if (index < 0 or index >= size):
            return None
        n = self.head
        i = 0
        while(i < index):
            n = n.next
            i += 1
        return n

    def insert(self, newElement, index=0):
        if index == 0:
            n = self.head
            pred = self.head
            ok = 1
            while n is not None:
                if n.element == newElement.element:
                    print("key already exists and doesnot insert the key")
                    ok = 0
                    break
                pred = n
                n = n.next
            if ok:
                tail = pred
                tail.next = newElement
                newElement.next = None
                tail = newElement
        else:
            size = self.countnode()
            if(index < 0 or index >= size):
                print("invalid index")
                return
            n = self.head
            while(n is not None):
                if(n.element == newElement):
                    print("key already exists and doesnot insert the key")
                    return
                n = n.next
            newnode = Node(newElement, None)
            pred = self.nodeAt(index-1)
            newnode.next = pred.next
            pred.next = newnode

    def remove(self, deletekey):
        n = self.head
        index = 0
        removeNode = None
        while(n is not None):
            if(n.element == deletekey):
                if(index == 0):
                    removeNode = self.head
                    head = head.next
                else:
                    pred = self.nodeAt(index-1)
                    removeNode = pred.next
                    pred.next = removeNode.next
            n = n.next
            index += 1
        return removeNode
##############################################################

    def EvenChecker(self):
        n = self.head
        while n is not None:
            if n.element % 2 == 0:
                print(n.element, end=" ")
            n = n.next

    def search_ele(self, number):
        n = self.head
        while n is not None:
            if n.element == number:
                break
            n = n.next
        if n is None:
            print("False")
        else:
            print("True")

    def reverse(self):
        prev = None
        n = self.head
        while n is not None:
            tem = n.next
            n.next = prev
            prev = n
            n = tem
        self.head = prev

    def find_elem(self, number):
        n = self.head
        while n is not None:
            if n.element == number:
                break
            n = n.next
        if n is None:
            print("False")
        else:
            print("True")

    def reverse(self):
        prev = None
        n = self.head
        while n is not None:
            tem = n.next
            n.next = prev
            prev = n
            n = tem
        self.head = prev

    def sorting(self):
        end = None
        while end != self.head.next:
            n = self.head
            while n.next is not end:
                m = n.next
                if n.element > m.element:
                    n.element, m.element = m.element, n.element
                n = n.next
            end = n

    def sumOfelements(self):
        n = self.head
        overall = 0
        while n is not None:
            overall += n.element
            n = n.next
        return (overall)

    def rotate_byplace(self, side, k):
        if side == "Right":
            if k == None:
                return
            prev = None
            prev2 = None
            p = self.head
            q = self.head
            length = 0
            c1 = 0
            while q is not None:
                prev = q
                q = q.next
                length += 1
            q = prev
            c = length-k
            while p is not None and c1 < c:
                prev2 = p
                p = p.next
                c1 += 1
            p = prev2
            q.next = self.head
            self.head = p.next
            p.next = None
        elif side == "Left":
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p is not None and count < k:
                prev = p
                p = p.next
                count += 1
            p = prev
            while q is not None:
                prev = q
                q = q.next
            q = prev
            q.next = self.head
            self.head = p.next
            p.next = None


#####################################################################
x = [1, 2, 3, 4, 5]
c = MyList(x)
c.showlist()
x = Node(20, None)
c.insert(x)
c.showlist()
c.insert(10, 2)
c.showlist()
x = Node(4, 10)
c.insert(x)
c.showlist()
c.remove(2)
c.showlist()
c.find_elem(7)
c.showlist()
c.sorting()
c.showlist()
c.reverse()
c.showlist()
c.EvenChecker()
c.showlist()
c.rotate_byplace("Left", 2)
c.showlist()
print(c.sumOfelements())
c.clear()
print(c.isEmpty())
