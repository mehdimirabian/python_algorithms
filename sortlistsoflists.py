""""
Best way to merge list of list of sorted numbers ?

eg : [10 20, 30 40], [5, 15, 65, 75], [35, 65, 95, 100]
"""

"""
total no of elemnts = nm
n = no of arrays ; here its 3
m = no of elements in an array. here m = 4
"""

"""
iterate through all numbers one single time 
keep track of each index per array in a separate variable
per iteration compare values and append the minimum of all values to the result array
append the left over at the end of loop
"""


 
def merge(array1, array2):
    i = 0
    j = 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    if i > len(array1):
        result.extend(array1[i:])
    else:
        result.extend(array2[j:])
    return result
    
    
def mergeElements(array):
    if len(array) == 1:
        return array
    # if len(array) == 2:
    #     sorted = merge(array)
    #     return sorted
    newArray = []
    
    for i in range(len(array)):
        if i%2 == 0:
            if i == len(array) - 1:
                newArray.append(sorted)
            continue
        sorted = merge(array[i-1], array[i])
        newArray.append(sorted)
        
    return mergeElements(newArray)
        
 
test1 = [[10, 20, 30, 40], [5, 15, 65, 75], [35, 65, 95, 100]]
results = mergeElements(test1)
print(results[0])

test2 = [[10, 20, 30, 40], [5, 15, 65, 75], [35, 65, 95, 100], [12, 56, 78, 120]]
results2 = mergeElements(test2)
print(results2[0])
      
