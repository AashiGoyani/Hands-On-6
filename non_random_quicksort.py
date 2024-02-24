def pivot_place(mylist,low,high):
    pivot = mylist[low]
    left = low + 1
    right = high
     
    while True:
        while left <= right and mylist[left] <= pivot:
            left += 1
        
        while left <= right and mylist[right] >= pivot:
            right -= 1
        
        if right < left :
            break
        
        else: 
            mylist[left] , mylist[right] = mylist[right] , mylist[left]
    
    mylist[low] , mylist[right] = mylist[right] , mylist[low]
    return right

def quick_sort(mylist,low,high):
    if low < high:
        p = pivot_place(mylist,low,high)
        quick_sort(mylist,low,p-1)
        quick_sort(mylist,p+1,high)

mylist = [9,56,34,12,17,44]
n = len(mylist)
quick_sort(mylist,0,n-1)
print("Final Sorted List: ",mylist)


