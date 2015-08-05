# my very first Python program!

li = [9,3,4,2,0,4,1,12,14,9,20,5,4,1,5,9,17,25,61,72,31,99,91,13,66]

def merge(x,y):
    if len(x) == 0:
        return y
    elif len(y) == 0:
        return x
    else: 
        if x[0] < y[0]: 
            return [x[0]] + merge(x[1:],y)
        else: 
            return [y[0]] + merge(x,y[1:])

def sort(l):
    if len(l) == 1:
        return l
    else:
        return merge(sort(l[:len(l)/2]), sort(l[(len(l)/2):]))

print sort(li)
