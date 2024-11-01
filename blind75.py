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


#Anagram

def is_Anagram(s,t):
        '''
        This is simple but has time complexity of O(nlogn)
        if s == t:
            return True
        else:
            return False
        s = sorted(s)
        s = ''.join(s)
        t = ''.join(sorted(t))
        '''


        #use of hashmap, counts how many items there are for each, time complexity of O(n)

        hash1 = {}
        hash2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            
            hash1[s[i]] = 1 + hash1.get(s[i],0)
            hash2[t[i]] = 1 + hash2.get(t[i],0)

        
        return hash1 == hash2
    

    
      
      
        
   
     
            