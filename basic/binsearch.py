import mergesort

li = mergesort.sort(mergesort.li)

def binsearch(l,i):
    n = len(l)
    if n == 1:
        return i == l[0]
    elif i < l[n/2]:
        return binsearch(l[:n/2],i)
    else:
        return binsearch(l[n/2:],i)

print binsearch(li,91)
print binsearch(li,82)
