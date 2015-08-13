from heap import MinHeap
from random import randint
from time import clock

# TODO use my mergesort for comparison?

fill = []
for i in range(30):
    x = randint(0,10000)
    fill.append((x,x))
test = MinHeap(fill)
print(test.heap)

res = []
for i in range(test.size):
    res.append(test.pop()[1])
print(test.heap)

fill.sort(key=lambda tup : tup[0])
res2 = list(map(lambda x : x[0], fill))
print("Expect:",res2)
print("Get:   ",res)

print("Now for excitement!")
heapElapsed = 0
listElapsed = 0
err = False
for i in range(10000):
    fill = []
    for i in range(100):
        x = randint(0,10000)
        fill.append((x,x))

    startHeap = clock()
    test = MinHeap(fill)
    res = []
    for i in range(test.size):
        res.append(test.pop()[0])
    endHeap = clock()
    heapElapsed += (endHeap-startHeap)

    startList = clock()
    fill2 = []
    for x in fill:
        fill2.append(x)
    fill2.sort(key=lambda tup : tup[0])
    endList = clock()
    listElapsed += (endList-startList)
    fill2 = list(map(lambda x : x[0], fill2))

    if not fill2 == res:
        print(fill2)
        print(res)
        err = True

print("Errors:",err)
print("Heap Elapsed:",heapElapsed)
print("List Elapsed:",listElapsed)
print("Ratio:",heapElapsed/listElapsed)
