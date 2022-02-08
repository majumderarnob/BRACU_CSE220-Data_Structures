# task_1

class Key_index:
    k = []

    def __init__(self, a=list):
        x = self.negIndex(a)
        for i in range(len(a)):
            a[i] = a[i] + x
        m = max(a) + 1
        for i in range(m):
            self.k.append(0)
        for i in range(len(a)):
            self.k[a[i]] += 1

    def negIndex(self, a):
        x = 0
        if(min(a) < 0):
            x = min(a)*-1
        return x

    def KeyIndex_search(self, val):
        if(s.k[val] >= 1):
            return True
        elif(s.k[val] == 0):
            return False
        pass

    def KeyIndex_sort(self):
        temp_val = []
        i = 0
        while i < len(self.k):
            j = 1
            while j <= self.k[i]:
                temp_val.append(i)
                j += 1
            i += 1
        return temp_val
        pass


arr = [8, -5, 3, -8, 7, 4]
initial = 0
if(min(arr) < 0):
    initial = min(arr)*-1
s = Key_index(arr)
value = int(input("Please enter the value: ")) + initial
print(s.KeyIndex_search(value))
temp = s.KeyIndex_sort()
for i in range(len(temp)):
    print(temp[i] - initial)


# Task_2

class Hashing:
    def __init__(self):
        self.size = 9
        self.aux = [0] * self.size

    def __str__(self):
        return str(self.aux)

    def hash(self, key):
        x = 0
        consonant = "BCDFGHJKLMNPQRSTVWXYZ"
        digit = "0123456789"
        for i in key:
            if i not in digit and i in consonant:
                x += 1
        totalDigit = 0
        for j in key:
            if j in digit:
                totalDigit += int(j)
        return ((x * 24) + totalDigit) % 9

    def connect(self, val):
        HashIndex = self.hash(val)
        if (self.aux[HashIndex] == 0):
            self.aux[HashIndex] = val
        else:
            print("Collision Occured")
            k = 0
            L = False
            while not L:
                index = (HashIndex + k) % 9
                if (self.aux[index] == 0):
                    self.aux[index] = val
                    L = True
                else:
                    k += 1


check = Hashing()
check.connect("ST1E89B8A32")
print(check)
