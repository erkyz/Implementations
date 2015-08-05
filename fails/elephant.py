import sys, math

"""
The distance between cities A and B is 1000 km. We have 3000 bananas in city A, and an elephant that can carry at most 1000 bananas at once. The elephant must eat a banana every 1km; it cannot go furhter if it runs out of the banana supply. What is the maximum number of bananas that can be transferred to the city B?
"""
# There should be a mathematical way of approaching this.
# We want to transport as much as possible each time
# Use continutations to support better control flow? or some sort of data structure?
# Dynamic programming: recursively solve a smaller problem
# The distance to cost ratio is the same, so by hand the best I have is 534, but no programmatic solution. There's probably a good way of proving optimality here. 

def max3(l1,l2):
    if l1[0] > l2[0]:
        return l1
    else:
        return l2

def max_bananas(bananas, dist_remain):
    if dist_remain < 0:
        return -1
    elif dist_remain == 0:
        return bananas
    else:
        alts = []
        for dist in range(1,dist_remain):
            cost = dist*(2*math.ceil(bananas/1000) - 1)
            alts.append([dist/cost,cost,dist])
        else:
            memo = reduce(max3, alts)
            print memo
            print 'max_bananas(' + str(bananas-memo[1]) + ',' + str(dist_remain-memo[2]) + ')'
            return max_bananas(bananas-memo[1],dist_remain-memo[2])

print max_bananas(3000,1000)
