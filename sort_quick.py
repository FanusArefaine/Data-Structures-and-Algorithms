def partition(lst, start, end):
    pivot = lst[end]
    pIndex = start
   
    for i in range(start, end):

        if lst[i] < pivot:
            lst[i], lst[pIndex] = lst[pIndex], lst[i]
            pIndex += 1
    lst[pIndex], lst[end] = lst[end], lst[pIndex]
    return pIndex



def quick_sort(lst, start, end):

    if start < end:
        pIndex = partition(lst, start, end)
        quick_sort(lst, start, pIndex-1)
        quick_sort(lst, pIndex+1, end)
    return lst


def main():

    l = [4,6,2,3,4,5,0,1,8,9]
    
    print(quick_sort(l, 0, 9))

main()

    
