li = [9,3,4,2,0,4,1,12,14,9,20,5,4,1,5,9,17,25,61,72,31,99,91,13,66]

def rev(l):
    if len(l) == 0:
        return l
    else:
        return rev(l[1:]) + [l[0]]

print li
print rev(li)

