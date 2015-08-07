from avl import AVL
from avl_dict import AVL_dict

# Tests: AVL
test = AVL([10,4,20,14,15,16])
print(list(test))
print("14 in test:", 14 in test)
del test[14]
print(list(test))
print("14 in test:", 14 in test)
del test[10]
print(list(test))

print ("---")

# Tests: AVL_dict
testdict = {'ten':10,'four':4,'twenty':20,'fourteen':14,'fifteen':15,'sixteen':16}
testavl = AVL_dict(testdict)
print(list(testavl))
print(list(testdict))
print("\"fourteen\" in testavl:", "fourteen" in testavl)
print("\"fourteen\" in testdict:", "fourteen" in testdict)
del testavl["fourteen"]
del testdict["fourteen"]
print(list(testavl))
print(list(testdict))
print("\"fourteen\" in testavl:", "fourteen" in testavl)
print("\"fourteen\" in testdict:", "fourteen" in testdict)
del testavl["four"]
del testdict["four"]
print(list(testavl))
print(list(testdict))
print("\"fourteen\" in testavl:", "fourteen" in testavl)
print("\"fourteen\" in testdict:", "fourteen" in testdict)

print ("---")
