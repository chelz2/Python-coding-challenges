# Finding Missing element in an array 
"""
problem - consider an array of non negative integer, second array is created by shuffling the first array & then removing 
a random element from it. i.e We have to find the missing number in second array. 

eg- finder([1,2,3,4], [2,4,1]) --> output : 3 is missing
"""

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return num1[-1]


finder([1,2,4,3], [4,2,3])
