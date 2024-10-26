from collections import defaultdict
#BLIND 75

#Two Sum
nums = [3,4,5,6]
target = 7


def twoSum(nums, target):
       for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i!=j and nums[i]+nums[j] == target:
                    return [i,j]


#Can be solved efficiently using hashmap as well.
def twoSumHash(numus, target):
    map = {}

    for i,n in enumerate(nums):
        difference = target - n
        if difference in map:
            return [map[difference], i]
        map[n] = i

#Group Anagrams
'''
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''

strs = ["act","pots","tops","cat","stop","hat"]

def anagrams(strs):
    newDict = defaultdict(list) #This will create a new key when there is no key in dictionary and will assign an empty list as its value

    for string in strs:
        sorting = sorted(string)
        sorting = ''.join(sorting)
        newDict[sorting].append(string)
    return (newDict.values())



###################
#3 sum 



nums = [-1,0,1,2,-1,-4]
def threeSum(nums):
    result = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 :
                    temp = [nums[i],nums[j],nums[k]]
                    result.add(tuple(temp))
            
                        
    return [list(i) for i in result]

print(threeSum(nums))