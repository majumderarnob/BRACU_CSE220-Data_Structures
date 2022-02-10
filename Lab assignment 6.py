# Task_1
def exChange(i, j):
    array[i], array[j] = array[j], array[i]


def selectionSort(array, i, j, flag):
    size = len(array)
    if (i < size - 1):
        if (j < size):
            if (array[i] > array[j]):
                exChange(i, j)
            selectionSort(array, i, j + 1, 0)
        else:
            selectionSort(array, i + 1, i+2, 1)


array = [64, 22, 55, 37, 56, 700, 10]
selectionSort(array, 0, 1, 1)
print(array)


################################################################################

# Task_2
def insertion(val, array):
    if (len(array) == 0):
        return [val]
    elif (val < array[0]):
        return [val] + array
    else:
        return (array[0:1] + insertion(val, array[1:]))


def sorting(array):
    if (len(array) == 0):
        return array
    if (len(array) == 1):
        return array
    else:
        return (insertion(array[0], sorting(array[1:])))


array = [23, 24, 35, 66, 47, 10]
print(sorting(array))


###############################################################################

# Task_3
class Node:
    def __init__(self, Value=None, next=None):
        self.Value = Value
        self.next = next


class Singly_Linked:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def bubbleSorting(self):
        temp2 = None
        while self.head.next != temp2:
            x = self.head
            while x.next != temp2:
                y = x.next
                if (x.Value > y.Value):
                    y.Value, x.Value = x.Value, y.Value
                x = x.next
            temp2 = x

    def showlist(self):
        temp = self.head
        while temp != None:
            print(temp.Value, end=",")
            temp = temp.next
        print()


test = Singly_Linked()
array = [55, 22, 82, 10]

for i in array:
    test.push(i)
print("UnSorted list: ", end=" ")
test.showlist()
test.bubbleSorting()
print("Sorted list: ", end=" ")
test.showlist()


##########################################################################
# Task_4

class Node:
    def __init__(self, Value=None, next=None):
        self.Value = Value
        self.next = next


class Singly_Linked:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def selection_sort(self):
        temp2 = self.head
        while temp2 != None:
            min_val = temp2
            x = temp2.next
            while x != None:
                if x.Value < min_val.Value:
                    min_val = x
                x = x.next
            temp2.Value, min_val.Value = min_val.Value, temp2.Value
            temp2 = temp2.next

    def showlist(self):
        temp = self.head
        while temp != None:
            print(temp.Value, end=",")
            temp = temp.next
        print()


test = Singly_Linked()
array = [55, 22, 82, 10]
for i in array:
    test.push(i)
test.selection_sort()
print("Sorted List:", end=" ")
test.showlist()


###############################################################################
# task_5

class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class Doublylinkedlist:
    def __init__(self, array):
        self.head = Node(array[0], None, None)
        tail = self.head
        for x in range(1, len(array)):
            new_node = Node(array[x], None, tail)
            tail.next = new_node
            tail = new_node

    def showList(self):
        if self.head.next is None:
            print("Empty list")
        else:
            head = self.head
            while self.head is not None:
                if head.next is None:
                    print(head.value)
                    break
                else:
                    print(head.value, end=" ")
                    head = head.next

    def insertionSort(self):
        head = self.head
        if head == None:
            return
        else:
            while head is not None:
                tail = head.next
                while tail and tail.prev != None and tail.value < tail.prev.value:
                    tail.value, tail.prev.value = tail.prev.value, tail.value
                    tail = tail.prev
                head = head.next


array = [7, 6, 9, 3, 5, 99, 1]
doublylinkedlist = Doublylinkedlist(array)
doublylinkedlist.insertionSort()
doublylinkedlist.showList()


#######################################################################
# task_6

def binarySearch(test, search, head, tail):
    mid_val = (head + tail) // 2
    if(mid_val >= len(test) or mid_val < 0):
        return "Error"
    mid_item = test[mid_val]
    if (head > tail):
        return "Error"
    if (mid_item == search):
        return mid_val
    if (mid_item < search):
        head = mid_val + 1
    else:
        tail = mid_val - 1
    return binarySearch(test, search, head, tail)


test = [10, 347, 453, 954, 475, 7, 5627, 6854]
index = binarySearch(test, 475, 0, len(test))
print(index)

##############################################################################

# task_7
memoization = {}


def nth_fibonacci(nth):
    if nth in memoization:
        return memoization[nth]
    if nth == 0 or nth == 1:
        return nth
    else:
        item = nth_fibonacci(nth-1) + nth_fibonacci(nth-2)
    memoization[nth] = item
    return item


n = int(input())
print(n, "th Fibonacci number is :", nth_fibonacci(n))
