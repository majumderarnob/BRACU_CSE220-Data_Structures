#........................ Task_1a..................#
def factorial(n):
    if n == 0 | n == 1:
        return 1
    else:
        return n * factorial(n - 1)


x = factorial(6)
print(x)

#..........................Task_1b................#


def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


x = fibonacci(4)
print(x)

#....................Task_1c.....................#


def print_array(list, index):
    if index == len(list):
        return
    else:
        print(list[index])
        print_array(list, index+1)


list = [1, 2, 3, 4, 5, 7]
print_array(list, 0)

# Task_1d


def powerN(base, n):
    if n == 0:
        return 1
    else:
        return base*powerN(base, n-1)


pow = powerN(3, 3)
print(pow)

#........................Task_2a...................#


def binary_converter(n):
    if n == 0:
        return 0
    else:
        return binary_converter(n//2)*10 + (n % 2)


int_val = binary_converter(11)
print(int_val)


#.....................Task_2b.....................#

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class singly_linkedlist:
    def __init__(self, array):
        self.head = None
        tail = None
        for x in array:
            new_node = Node(x)
            if self.head == None:
                self.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

    def addElem(self, head):
        if head is None:
            return 0
        else:
            return head.value + self.addElem(head.next)

    def sum(self):
        return self.addElem(self.head)


array = [1, 2, 3, 4, 5, 6, 7]
listlinked = singly_linkedlist(array)
print(listlinked.sum())


#...............Task_2c.....................#

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linklist:
    def __init__(self, array):
        self.head = None
        tail = None
        for x in array:
            new_node = Node(x)
            if self.head == None:
                self.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

    def reverse(self, head):
        if head.next is None:
            print(head.value)
        else:
            self.reverse(head.next)
            print(head.value)

    def reverse_print(self):
        return self.reverse(self.head)


array = [10, 20, 30, 40, 50]
listlinked = linklist(array)
listlinked.reverse_print()


#.......................task_3....................#

def hocBuilder(height):
    if(height == 0):
        return str(0) + "\n not build a house at all."
    elif height == 1:
        return 8
    else:
        return 5 + hocBuilder(height - 1)


height = int(input("Enter height: "))
print(hocBuilder(height))


# task_4a
def pattern(n):
    if(n == 0):
        return 0
    else:
        pattern(n-1)
        print(n, end="")


def print_pattern(n):
    if(n == 0):
        return 0
    else:
        print_pattern(n - 1)
    pattern(n)
    print()


n = int(input("Enter n: "))
print_pattern(n)

#..............................task_4b........................#


def pattern(n):
    if n == 0:
        return 0
    else:
        pattern(n-1)
        print(n, end="")


def print_pattern(n, i):
    if n == 0:
        return 0
    else:
        space(n-1)
        pattern((i)-n+1)
        print()
        print_pattern(n-1, i)


def space(n):
    if n == 0:
        return 0
    else:
        space(n - 1)
        print("", end=" ")


print_pattern(6, 6)


#...............task_5...................#
class FinalQ:
    def print(self, array, idx):
        if(idx < len(array)):
            profit = self.calcProfit(array[idx])
            print(
                f"{str(idx + 1)}. Investment: {array[idx]}; Profit: {profit} ")
            self.print(array, idx+1)

    def calcProfit(self, investment):
        if investment <= 25000:
            return 0.0
        elif investment > 25000 and investment <= 100000:
            return 45 + self.calcProfit(investment-1000)
        elif investment > 100000:
            return 80 + self.calcProfit(investment-1000)
        else:
            return 0


array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)
