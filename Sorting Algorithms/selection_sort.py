def selection_sort(lst):

    for i in range(len(lst)-1):

        for j in range(i, len(lst)):
            if lst[j] <= lst[i]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst

def main():
    l = [4,3,6,0,5,7,8]
    print(selection_sort(l))

main()
    