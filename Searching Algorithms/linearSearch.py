def linearSearch(lst, x):

    for i in range(len(lst)):

        if lst[i] == x:
            return True
            
    return False


if __name__ == '__main__':

    lst = [2,4,6,7,1,3]

    print(linearSearch(lst, 10))

    
