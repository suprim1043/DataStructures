array = [1,2,3,4,5,6,7,8]



#Binary Search

def binarySearch(array,target):
    l,r = 0, len(array)-1 #left and right pointer 
    
    while l <= r:
        mid = (l+r)//2 #middle value
        if target > array[mid]: #eliminates all values left to mid
            l = mid + 1
        elif target < array[mid]: #eliminates all values right to mid
            r = mid - 1
        else:
            return mid #returns the value if target is found
    return -1 
#it divides array everytime loop is run. Time complexity of O(log n)

