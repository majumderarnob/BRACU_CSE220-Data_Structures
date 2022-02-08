class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

    def height(self):
        ans = 1
        if self.left is not None:
            ans = max(ans, 1 + self.left.height())
        if self.right is not None:
            ans = max(ans, 1 + self.right.height())
        return ans

    def get_level(self, value, level=1):
        if self.key is value:
            return level
        if self.left is not None:
            ans = self.left.get_level(value, level+1)
            if ans != -1:
                return ans
        if self.right is not None:
            ans = self.right.get_level(value, level+1)
            if ans != -1:
                return ans
        return -1

    def pre_order(self):
        print(self.key, end=' ')
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()

    def in_order(self):
        if self.left is not None:
            self.left.in_order()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.in_order()

    def post_order(self):
        if self.left is not None:
            self.left.post_order()
        if self.right is not None:
            self.right.post_order()
        print(self.key, end=' ')

    def same(self, other):
        if self.key != other.key:
            return False
        if self.left is not None and other.left is not None:
            if self.left.same(other.left) is False:
                return False
        elif self.left is None and other.left is not None:
            return False
        elif other.left is None and self.left is not None:
            return False
        if self.right is not None and other.right is not None:
            if self.right.same(other.right) is False:
                return False
        elif self.right is None and other.right is not None:
            return False
        elif other.right is None and self.right is not None:
            return False
        return True

    def copy(self, other):
        self.key = other.key
        if other.left is not None:
            self.left = Node(0)
            self.left.copy(other.left)
        if other.right is not None:
            self.right = Node(0)
            self.right.copy(other.right)

    def get_copy(self):
        other = Node(0)
        other.copy(self)
        return other


def main():
    T = Node(0)
    T.left = Node(1)
    T.right = Node(2)
    T.left.left = Node(3)
    T.right.left = Node(4)
    T.right.right = Node(5)
    print("Height of Tree is", T.height())
    print("Level of node 2 is", T.get_level(0))
    print("Pre-Order:")
    T.pre_order()
    print("")
    print("Post-Order:")
    T.post_order()
    print("")
    print("In-Order:")
    T.in_order()
    print("")

    T1 = Node(0)
    T1.left = Node(1)
    T1.right = Node(2)
    T1.left.left = Node(3)
    T1.left.right = Node(4)
    T1.right.left = Node(5)
    print("For the created Tree:")
    print("Both trees are same") if T.same(
        T1) else print("Both trees are not same")
    print("For the copied Tree:")
    T2 = T.get_copy()
    print("Both trees are same") if T.same(
        T2) else print("Both trees are not same")


if __name__ == '__main__':
    main()
