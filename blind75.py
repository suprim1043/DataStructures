#BLIND 75

#Two Sum
nums = [3,4,5,6]
target = 7


def twoSum(nums, target):
       for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i!=j and nums[i]+nums[j] == target:
                    return [i,j]

print(twoSum(nums,target))

#Can be solved efficiently using hashmap as well.
def twoSumHash(numus, target):
    map = {}

    for i,n in enumerate(nums):
        difference = target - n
        if difference in map:
            return [map[difference], i]
        map[n] = i


print(twoSumHash(nums, target), "hash")

