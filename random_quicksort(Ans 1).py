import random

def random_pivot_place(list1, low, high):
    pivot_index = random.randint(low, high)
    temp = list1[pivot_index]
    list1[pivot_index] = list1[low]
    list1[low] = temp    
    pivot = list1[low]
    left_element = low + 1
    right_element = high

    while True:
        while left_element <= right_element and list1[left_element] <= pivot:
            left_element += 1
        
        while left_element <= right_element and list1[right_element] >= pivot:
            right_element -= 1
        
        if right_element < left_element:
            break
        else: 
            temp = list1[left_element]
            list1[left_element] = list1[right_element]
            list1[right_element] = temp
    
    # Swap low and right_element 
    temp = list1[low]
    list1[low] = list1[right_element]
    list1[right_element] = temp
    return right_element

def random_quick_sort(list1, low, high):
    if low < high:
        p = random_pivot_place(list1, low, high)
        random_quick_sort(list1, low, p - 1)
        random_quick_sort(list1, p + 1, high)

list1 = [9, 56, 34, 12, 17, 44]
n = len(list1)
random_quick_sort(list1, 0, n - 1)
print("Final Sorted List: ", list1)
