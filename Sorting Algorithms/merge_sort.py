def merge_sort(lst):

    if len(lst) < 2:
        return
    
    n = len(lst)//2

    left = lst[:n]
    right = lst[n:]

    merge_sort(left) #sorting the left half
    merge_sort(right) #sorting the right half
    

    i = j = l = 0

    while (i<len(left) and j<len(right)):
        if left[i] < right[j]:
            lst[l] = left[i]
            i+=1
        else:
            lst[l] = right[j]
            j+=1
        l+=1
    # Checking for elements left
    while(i<len(left)):
        lst[l] = left[i]
        l+=1
        i+=1
    while(j<len(right)):
        lst[l] = right[j]
        l+=1
        j+=1
    
    return lst


def main():

    l = [4,2,9,8,3,5]
    print(merge_sort(l))

main()


