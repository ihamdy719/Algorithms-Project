def merge_and_sort_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    return merged_array

def find_kth_element(arr1, arr2, k):
    merged_array = merge_and_sort_arrays(arr1, arr2)
    kth_element = merged_array[k-1]
    return merged_array, kth_element

# Add the arrays and the value of k here
arr1 = [int(x) for x in input("Enter numbers for the first array separated by spaces: ").split()]
arr2 = [int(x) for x in input("Enter numbers for the second array separated by spaces: ").split()]
k = int(input("Enter the value of k: "))

sorted_array, kth_element = find_kth_element(arr1, arr2, k)
print(f'Sorted Array: {sorted_array}')
print(f'{k}th Element: {kth_element}')



'''

Algorithm FindKthElement(arr1, arr2, k)
{
    merged_array := MergeArrays(arr1, arr2);
    return merged_array[k-1];
}

Algorithm MergeArrays(arr1, arr2)
{
    merged_array := [];
    i := 0;
    j := 0;
    
    while i < length(arr1) AND j < length(arr2) do
    {
        if arr1[i] < arr2[j] then
        {
            merged_array.append(arr1[i]);
            i := i + 1;
        }
        else
        {
            merged_array.append(arr2[j]);
            j := j + 1;
        }
    }
    
    while i < length(arr1) do
    {
        merged_array.append(arr1[i]);
        i := i + 1;
    }
    
    while j < length(arr2) do
    {
        merged_array.append(arr2[j]);
        j := j + 1;
    }
    
    return merged_array;
}

// Example usage
arr1 := read("Enter the elements of the first array separated by spaces: ");
arr2 := read("Enter the elements of the second array separated by spaces: ");
k := read("Enter the value of k: ");
write("The ", k, "-th element is: ", FindKthElement(arr1, arr2, k));




'''   