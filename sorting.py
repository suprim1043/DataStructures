def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [8,7,3,4,56,2]
from collections import Counter

def insertionSort(array):

    n = len(array)
    for i in range(n):
        j = i - 1
        while j >= 0 and array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
    return array









words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]
ans = []

def wordSubsets(words1, words2):
        max_freq = Counter()
        
        for word in words2:
            word_freq = Counter(word)
            for char, count in word_freq.items():
                max_freq[char] = max(max_freq[char], count)
        ans = []
        for word in words1:
            word_freq = Counter(word)
            
            if all(word_freq[char] >= max_freq[char] for char in max_freq):
                ans.append(word)
        
        return ans
    

print(wordSubsets(words1,words2))