import random as r
def rotate_larger_element_to_right(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            temp = x[i]
            x[i] = x[i+1]
            x[i+1] = temp
    return x
def bubble_sort(x):
    for i in range(len(x)):
        rotate_larger_element_to_right(x)
    return x


def init_list_random(x):
    for i in range(20):
        x.append(r.randint(10, 99))


def main():
    x = []
    init_list_random(x)
    print(x)
    bubble = bubble_sort(x)
    print(bubble)
main()
print()
def list_sorting(list1,list2):
    for i in range(len(list1)):
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
                list2[i],list2[i+1] = list2[i+1],list2[i]
    l1 = list1,list2
    return l1
def list_sort(list1, list2):
    for i in range(len(list1)):
        for i in range(len(list1)-1):
            if list2[i] > list2[i+1]:
                list2[i], list2[i+1] = list2[i+1], list2[i]
                list1[i], list1[i+1] = list1[i+1], list1[i]
                
    l1 = list2, list1
    return l1
def main():
    list1 = []
    init_list_random(list1)
    print(list1)
    list2 = []
    init_list_random(list2)
    print(list2)
    x = list_sorting(list1, list2)
    print(x)
    y = list_sort(list1, list2)
    print(y)
main()
print()
def shuffle_elements(arr,n):
    for i in range(n):
        i = r.randint(0,len(arr)-1)
        j = r.randint(0,len(arr)-1)
        if i != j:
            arr[i],arr[j] = arr[j],arr[i]
    return arr
def main():
    arr = []
    init_list_random(arr)
    print(arr)
    x = shuffle_elements(arr, 20)
    print(x)
main()
print()
def main():
    x = []
    for i in range(2,99):
        x.append(i)
    print(x)
main()