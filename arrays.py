#Practicing problems related to arrays

array = [1,21,3,4,5,6,7,8]


#Printing items of array

def printArray(array):
    for i in range(len(array)):
        print(array[i], end = " ")
    print("")

#printing largest element of an array
def largestElmnt(array):
        temp = 0
        for i in range(len(array)):
            if i == len(array):
                 break
            else:
                if temp <= array[i]:
                     temp = array[i]
            i += 1
        print(temp, "is the largest element")


#Check if an array is sorted
def checkSorted(array):
    for i in range(len(array)):
            if i+1 == len(array):
                break
            else:
                if (array[i]>array[i+1]):
                    return False
    return True
   
#Check if its sorted alternate method
def alternate(array):
    i = 1
    while i < len(array):
            if array[i] < array[i-1]:
                 return False
            i = i + 1
    return True

#Hash Map/Sets

hashArray = ["alice", "sedhai", "suprim", "suprim"]


def hashMap(hashArray):
    dict = {}
    for name in hashArray:
        if name not in dict:
             dict[name] = 1
        else:
             dict[name] += 1

    return dict

print((hashMap(hashArray))["suprim"])


from collections import Counter
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]

def ret(words1, words2):
    
    maximum = Counter()
    for word in words2:
        maximum_freq = Counter(word)
        for key,val in maximum_freq.items():
            maximum[key] = max(maximum[key],val)    
    stack = []
    for word in words1:
        matching = Counter(word)
        if all(matching[char] >= maximum[char] for char in maximum):
            stack.append(word)
    return stack

        
print(ret(words1,words2))