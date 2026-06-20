def binarysearch(list,x):
    low = 0
    mid = 0
    high = len(list)
    while low <= high:
        mid = (low + high)// 2
        
        if list[mid] < x:
            low = mid + 1
        elif list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

list = [1,5,10,15,250,251,256,512,1024,1032]
x = 1

result = binarysearch(list, x)
if result != -1:
    print("element is present in list",str(result))
else:
    print("element is not present in list")
        
        