#quick sort implementation
array = []
def quick_sort(array):
    less = []
    equal = []
    greater = []
    if (len(array) > 1):
        pivot = array[0]
        for element in array:
            if pivot < element:
                greater.append(element)
            if pivot > element:
                less.append(element)
            if pivot == element:
                equal.append(element)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return array
def main():
    array = [8, 8, 11, 3, 2, 0] #put here your list to sort
    quick_sort(array)
    print quick_sort(array)
    

if __name__ == '__main__':
    main()