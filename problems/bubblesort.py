def bubblesort(list):
    n = len(list)
    for i in range(n):
        sorted = True
        for j in range(n -i - 1):
            if list[j] > list[j + 1]:
                list[j] , list[j + 1] = list[j + 1], list[j]
                sorted = False
        if sorted:
            break
        
    return list


list = [89,1,65,5,5,34,10,244,15,250,251,256,512,1024,1032]
x = 512
result = bubblesort(list)
print(result)

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
result2 = binarysearch(list, x)
if result2 != -1:
    print("element is present in list",str(result2))
else:
    print("element is not present in list")