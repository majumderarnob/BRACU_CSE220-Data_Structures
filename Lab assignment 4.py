# Task_1: using an array based stack
##################################################################################
class Stack:
    def __init__(self):
        self.lst1 = []
        self.lst2 = []
        self.hst = -1
        self.chr = 0

    def push(self, temp):
        self.lst1 += [temp]
        self.lst2 += [self.chr]
        self.hst = self.hst + 1

    def peek(self):
        return self.lst1[self.hst]

    def pop(self):
        val = self.lst1[self.hst]
        self.hst = self.hst - 1
        self.lst1 = self.lst1[:-1]
        return val

    def expChecker(self, arith_exp):
        for i in arith_exp:
            self.chr = self.chr + 1
            if self.hst == -1 and i in ")}]":
                print("This expression is NOT correct.")
                print("Error at character #", self.chr, ".",
                      "'", i, "'", " not opened.", end="")
                return
            elif i in "({[":
                self.push(i)
            elif i in ")}]":
                x = self.peek()
                if i == ")" and x == "(":
                    self.pop()
                elif i == "}" and x == "{":
                    self.pop()
                elif i == "]" and x == "[":
                    self.pop()
                else:
                    print("This expression is NOT correct.")
                    print("Error at character #",
                          self.lst2[self.hst], ".", "'", x, "'", " not closed.", end="")
                    return
        if self.hst == -1:
            print("This expression is correct.")
        else:
            print("This expression is NOT correct.")
            print("Error at character #",
                  self.lst2[self.hst], ".", "'", x, "'", " not opened.", end="")


arith_exp = input("Enter The expression: ")
operation = Stack()
operation.expChecker(arith_exp)

# 1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14
# 1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14
# 1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14
# 1+2*(3/4)


##########################################################################################
# Task_2: using a linked list based stack.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, element):
        if self.head == None:
            self.head = Node(element)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(element)

    def pop(self):
        global list_status
        global available
        if self.head == None:
            list_status = "Empty"
            available = None
        else:
            if self.head.next == None:
                available = self.head.data
                self.head = None
            else:
                n = self.head
                while n.next.next is not None:
                    n = n.next
                available = n.next.data
                n.next = None


opening_brackets = ["[", '{', "("]
closing_brackets = ["]", "}", ")"]


def bracketChecker(a, b):
    if a == "(" and b == ")":
        return True
    elif a == "{" and b == "}":
        return True
    elif a == "[" and b == "]":
        return True
    else:
        return False


check = linkedlist()
string = input()
expression = False
index = []
t = 1
x = 0
y = ""

for v in string:
    if v in opening_brackets:
        check.push(v)
        index.append(t)
    if v in closing_brackets:
        check.pop()
        if available == None:
            expression = False
            x = t
            y = v
            break
        else:
            expression = bracketChecker(available, v)
            if expression == True:
                index.pop()
            else:
                x = index
                y = available
    t = t+1

if expression is True:
    print('This expression is correct.')
else:
    if isinstance(x, list):
        print('This expression is NOT correct.')
        print("Error at character # {0}. '{1}'- not closed.".format(x[-1], y))
    else:
        print('This expression is NOT correct.')
        print("Error at character # {0}. '{1}'- not opened.".format(x, y))
