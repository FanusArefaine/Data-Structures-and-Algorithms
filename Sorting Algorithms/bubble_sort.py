def bubble_sort(lst):

    for i in range(len(lst)-1):

        for j in range(len(lst)-i-1):

            if lst[j] > lst[j+1]:

                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


    

def main():

    l = [4,3,6,9,8,1,0]
    print(bubble_sort(l))

main()
            
            