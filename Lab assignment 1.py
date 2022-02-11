# Linear Array (1-8)

# Answer No. 1 (Shift Left K cells)
def shiftLeft(source, k):
    x = 0
    while x < k:
        source[i] = source[x+k]
        x = x + 1
    x = k
    while x <= len(source)-1:
        source[x] = 0
        x = x + 1
    print(source)


source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)


# Answer No. 2 (rotate left k cells)
def rotateLeft(source, k):
    x = [0] * k
    i = 0
    while i < k:
        x[i] = source[i]
        i = i + 1

    y = [0] * k
    i = 0
    while i < k:
        y[i] = source[i+k]
        i = i + 1

    new_source = y + x
    print(new_source)


source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 3)


# Answer No. 3 (Remove an element from an array)
def remove(source, size, idx):
    x = idx
    while x < len(source) - idx:
        source[x] = source[x+1]
        x = x + 1
    source[idx + idx] = 0

    print(source)


source = [10, 20, 30, 40, 50, 0, 0]
remove(source, 5, 2)


# Answer No. 4 (Remove all occurrences of a particular element from an array)
def removeAll(source, size, element):
    i = 0
    while i < len(source) - 1:
        if source[i] == element:
            for x in range(i, len(source)-1):
                source[x] = source[x+1]
                source[len(source)-1] = 0
            i -= 1
        i += 1
    return source


source = [10, 2, 30, 2, 50, 2, 2, 60, 0, 0]
print(removeAll(source, 8, 2))


# Ans No. 5(Splitting an Array)


# Ans No. 6 (Array series)
def arrayOfSeries(n):

    x = [0]*(n*n)
    i = 1
    while i <= n:
        j = 1
        k = (n*i)-1
        while j <= i:
            x[k] = j
            j = j + 1
            k = k - 1
        i = i + 1
    print(x)


arrayOfSeries(int(input()))


# Ans No. 7(Max Bunch Count)
def bunch(source):

    i = 0
    j = 0
    l_bun = 0

    while i < len(source) - 1:
        if source[i] == source[i+1]:
            j += 1
            l_bun = j
        else:
            j = 1
        if j > l_bun:
            l_bun = j
            j = 1

        i += 1
    print(l_bun)


bunch([1, 2, 2, 3, 4, 4, 4])


# Ans  no. 8 (Repetition)
def repetition(source):

    a = [0]*len(source)
    b = 1
    i = 0
    j = i+1
    while i < len(source)-1:
        while j < len(source):
            if source[i] > source[j]:
                c = source[i]
                source[i] = source[j]
                source[j] = c
            j += 1
        i += 1

    i = 0
    j = i + 1
    k = 0
    while i < len(source)-1:
        b = 1
        while j < len(source):
            if source[i] == source[j]:
                b += 1
            else:
                break
            j += 1
        i += 1
        if b > 1:
            a[k] = b
            i = i+b-1
            k += 1

    i = 0
    while i < len(a)-1:
        if a[i] != 0:
            j = i+1
            while j < len(a):
                if a[j] != 0:
                    if a[i] == a[j]:
                        return False
                    else:
                        return True
                j += 1
        i += 1


print(repetition([3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6]))
print(repetition([4, 5, 6, 6, 4, 3, 6, 4]))


# Circular Array
# Ans. No 1(palindrome)

def palindrome(source, size, start):
    x = [0]*len(source)
    y = [0]*len(source)
    i = 0
    j = start
    while i < size:
        x[i] = source[j]
        i += 1
        j = (j+1) % len(source)
    i = 0
    j = size-1
    while j >= 0:
        y[i] = x[j]
        i += 1
        j -= 1
    if x == y:
        return True
    else:
        return False


print(palindrome([20, 10, 0, 0, 0, 10, 20, 30], 5, 5))
print(palindrome([10, 20, 0, 0, 0, 10, 20, 30], 5, 5))


# Ans. No. 2(Intersection)

def intersection(array_1, start_1, size_1, array_2, start_2, size_2):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    array1_len = len(array_1)
    array2_len = len(array_2)
    
    for i in range(1, array1_len):
        if(array_1[i] == 0 and array_1[i - 1] != 0):
            for x in range(i):
                list1.append(array_1[x])

    for i in range(1, array1_len):
        if(array_1[i] != 0 and array_1[i - 1] == 0):
            for x in range(i, array1_len):
                list2.append(array_1[x])

    for i in range(1, array2_len):
        if(array_2[i] == 0 and array_2[i - 1] != 0):
            for y in range(i):
                list3.append(array_2[y])

    for i in range(1, array2_len):
        if(array_2[i] != 0 and array_2[i - 1] == 0):
            for y in range(i, array2_len):
                list4.append(array_2[y])

    combined_list1 = list2 + list1
    combined_list2 = list4 + list3

    for i in range(len(combined_list1)):
        new = combined_list1[i]
        for i in range(len(combined_list2)):
            if(new == combined_list2[i]):
                if(new not in list5):
                    list5.append(new)
                else:
                    continue
            else:
                continue
    print(list5)

intersection([40, 50, 0, 0, 0, 10, 20, 30], 5, 6, [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25], 8, 7)

# Ans No. 3 (Musical Chair Game)
