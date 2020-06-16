def insertion_sort(lst):

    for i in range(len(lst)):

        value = lst[i]

        while i > 0 and lst[i-1] > value:
            lst[i] = lst[i-1]
            i -= 1
        lst[i] = value
    return lst


def main():

    l = [4,6,2,3,1]
    print(insertion_sort(l))

main()  