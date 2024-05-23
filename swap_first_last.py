def swap_first_last(lst):
    if len(lst) < 2:
        return lst # if the list has less than 2 elements, no swapping needed
    lst[0],lst[-1] = lst[-1], lst[0]
    return lst

def swap_two_with_temp(lst):
    size = len(lst)
    
    temp = lst[0]
    lst[0] = lst[size-1]
    lst[size-1] = temp
    return lst

if __name__ == "__main__":
    input = [12, 35, 9, 56, 24]
    print("Original input: ", input)
    swapElements = swap_first_last(input)
    print("List after swapping the first and last element: ", swapElements)
     
    swapwithtemp = swap_two_with_temp(input)
    print("List after swapping the first and last element using Temp: ", swapwithtemp)
     