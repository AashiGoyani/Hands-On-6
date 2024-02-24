import random

def random_pivot_place(mylist, low, high):
    pivot_index = random.randint(low, high)
    mylist[pivot_index], mylist[low] = mylist[low], mylist[pivot_index]
    
    pivot = mylist[low]
    left = low + 1
    right = high

    while True:
        while left <= right and mylist[left] <= pivot:
            left += 1
        
        while left <= right and mylist[right] >= pivot:
            right -= 1
        
        if right < left:
            break
        else: 
            mylist[left], mylist[right] = mylist[right], mylist[left]
    
    mylist[low], mylist[right] = mylist[right], mylist[low]
    return right

def random_quick_sort(mylist, low, high):
    if low < high:
        p = random_pivot_place(mylist, low, high)
        random_quick_sort(mylist, low, p - 1)
        random_quick_sort(mylist, p + 1, high)

mylist = [9, 56, 34, 12, 17, 44]
n = len(mylist)
random_quick_sort(mylist, 0, n - 1)
print("Final Sorted List: ", mylist)
