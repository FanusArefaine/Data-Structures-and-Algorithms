def binarySearch(lst, x):

    start=0
    end=len(lst)-1

    while start <= end:

        mid = start + (end-start)//2
        if lst[mid] == x:
            return True 
        elif lst[mid] > x:
            end = mid-1 
        else:
            start = mid+1

    return False 


def binarySearch_recursive(lst, low, high, x):

    if low > high:
        return False 
    mid = low + (high-low)//2

    if lst[mid] == x:
        return True 
    
    elif lst[mid] > x:
        return binarySearch_recursive(lst, low, mid-1, x)
    
    else:
        return binarySearch_recursive(lst, mid+1, high, x)


if __name__ == '__main__':

    lst = [2,3,5,6,9,10,13,16]

    print(binarySearch(lst, 10))
    print(binarySearch_recursive(lst, 0, 7, 10))
    