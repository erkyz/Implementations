from math import sqrt
import random
import timeit

# TODO use open addressing

def isprime(x):
    for i in range(2, int(sqrt(x))+1):
        if x%i == 0:
            return False
    return True

class CollisionError(Exception):
    pass

class PerfectHash: # All keys must be static and known beforehand
    def __init__(self, keys):
        self.m = len(keys)

        while True:
            try:
                # [m, a, b, []*m] where h(x) = ((ax+b) mod p) mod m
                # using a universal hashing scheme
                self.table = [None]*self.m
                for i in range(self.m):
                    self.table[i] = [0,0,0,[]]

                # Generate a random prime - because there's ~1/N primes you'll get one soon enough
                self.p = 10
                while not isprime(self.p):
                    self.p = random.randrange(self.m,10*self.m)

                # pick from universal family of hash functions where
                # h_{a,b}(k) = ((ak+b) mod p) mod m - i.e. linear transformation to Z_m
                self.a = random.randrange(1,self.p) # a \in Z*_p
                self.b = random.randrange(0,self.p) # b \in Z_p

                # figure out how many keys hash to each slot
                for key in keys:
                    self.table[((self.a*key + self.b)%self.p)%self.m][0] += 1
                    self.table[((self.a*key + self.b)%self.p)%self.m][3].append(key)

                for slot in self.table:
                    # It's more likely than not that there will be no collisions.
                    # So keep trying until you find a good hash function. 
                    # May want to try open addressing...
                    __done = False
                    __ks = slot[3]
                    slot[1] = random.randrange(1,self.p) # a \in Z*_p
                    slot[2] = random.randrange(0,self.p) # b \in Z_p
                    slot[3] = [None]*(slot[0]**2)
                    for k in __ks:
                        if slot[3][((slot[1]*k+slot[2])%self.p)%slot[0]] is not None:
                            raise CollisionError()
                        else:
                            slot[3][((slot[1]*k+slot[2])%self.p)%slot[0]] = k

            except CollisionError as e:
                continue
            else:
                break

        print self.table

    # Guaranteed worst-case O(1)
    def find(self, x):
        slot = ((x*self.a+self.b)%self.p)%self.m
        m = self.table[slot][0]
        if m == 0:
            return False
        a = self.table[slot][1]
        b = self.table[slot][2]
        if self.table[slot][3][((a*x + b)%self.p)%m] == x:
            return True
        else:
            return False

# Tests
test = [1,12,13,4,6,7,312,1512,1245,121,42,1350,134,52]
a = PerfectHash(test)

print 'True:', a.find(12)
print 'True:', a.find(13)
print 'False:', a.find(14)
print 'True:', a.find(312)
print 'False:', a.find(313)
print 'False:', a.find(0)
print 'False:', a.find(20000)

for n in range(1,5):
    test2 = []
    x = 2**40
    for i in range(n*10):
        test2.append(random.randrange(0,x))

    print timeit.timeit(lambda: PerfectHash(test2), number=1)
    # NO GOOD! TAKES EXPONENTIALLY LONGER AS N INCREASES... WHY??

    '''
    for i in test2:
        if b.find(i) == False:
            print "Failed"
    '''
