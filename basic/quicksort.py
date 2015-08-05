from random import randint

li = [9,3,4,2,0,4,1,12,14,9,20,5,4,1,5,9,17,25,61,72,31,99,91,13,66]

def sort(l):
    if len(l) <= 1:
        return l
    else:
        x = randint(0,len(l)-1)
        n = l[x]
        a = []
        b = []
        
        m = []
        m.extend(l)
        del m[x]
        for i in m:
            if i < n:
                a.append(i)
            else:
                b.append(i)
      
        return sort(a) + [n] + sort(b)

print sort(li)
