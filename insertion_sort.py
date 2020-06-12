def insertion_sort(lst):

    for i in range(1, len(lst)):

        value = lst[i]

        while i > 0 and lst[i-1] > value:
            lst[i] = lst[i-1]
            i = i - 1

        lst[i] = value
    return lst

def main():

    l = [4,6,2,3,1]
    k = [4,3,5,6,1]
    print(insertion_sort(l))

main()  