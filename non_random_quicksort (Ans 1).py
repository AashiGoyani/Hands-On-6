def pivot_place(list1,low,high):
    pivot = list1[low]
    left_element = low + 1
    right_element = high
     
    while True:
        while left_element <= right_element and list1[left_element] <= pivot:
            left_element += 1
        
        while left_element <= right_element and list1[right_element] >= pivot:
            right_element -= 1
        
        if right_element < left_element :
            break
        
        else: 
            # Swap left_element and right_element 
            temp = list1[left_element]
            list1[left_element] = list1[right_element]
            list1[right_element] = temp
    
    # Swap low and right_element 
    temp = list1[low]
    list1[low] = list1[right_element]
    list1[right_element] = temp
    return right_element

def quick_sort(list1,low,high):
    if low < high:
        p = pivot_place(list1,low,high)
        quick_sort(list1,low,p-1)
        quick_sort(list1,p+1,high)

list1 = [9,56,34,12,17,44]
n = len(list1)
quick_sort(list1,0,n-1)
print("Final Sorted List: ",list1)


