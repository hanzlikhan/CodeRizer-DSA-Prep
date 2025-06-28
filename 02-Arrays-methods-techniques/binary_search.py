# function to perform binary search on list 
def binary_search(arr, target):

# write code here to perform binary search

    start = 0 
    end = len(arr) - 1

    while start <= end:
        # calculate mid index
        # using integer division to avoid float result
        mid = (start + end) // 2
        # check if the target is at mid index
        # if yes, return mid index
        if arr[mid] == target:
            return mid
        # if target is greater than mid element, search in right half
        # if target is less than mid element, search in left half

        elif arr[mid] < target:
            start = mid + 1
        
        else:
            end = mid - 1



# target which we need to find in a list 
target = 9

# a list in which we need to find the target
arr = [2,7,8,9,10,11,14,20]
# call a function to perform linear search
Result = binary_search(arr, target)


