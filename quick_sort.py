#quick sort implementation
def quick_sort(list = []):
    less = equal = greater = []
    if (len(list) > 1):
        pivot = list[0]
        for element in list:
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
    print quick_sort([8, 8, 11, 3, 2, 0])
if __name__ == '__main__':
    main()
