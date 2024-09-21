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

