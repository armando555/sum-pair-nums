def pairSum(arr, target):
    if not arr:
        return  

    first_element = arr[0]
    remaining_array = arr[1:]

    checkPair(first_element, remaining_array, target)

    pairSum(remaining_array, target)
   
def checkPair(item,arr,target):
    
    if len(arr) <= 1:
        if len(arr) == 1 and item + arr[0] == target:
            print(f"{item}, {arr[0]}")
        return True
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    checkPair(item,left_half, target)
    checkPair(item,right_half, target)


pairSum([1,9,5,0,20,-4,12,16,7,15,3],12)