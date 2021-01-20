def selection_sort(lst):

    for i in range(len(lst)-2):

        min = i

        for j in range(i+1, len(lst)-1):

            if lst[min] >= lst[j]:
                min = j
        lst[min], lst[i] = lst[i], lst[min]

    return lst


   
def main():
    l = [4,3,6,0,5,7,8]
    print(selection_sort(l))

main()
    