# insertion sort
# Logic: Its assumes first element to minimum and compare with every element in pass(round)

# Best case: O(n) { if the input is in asscending order}
# Worst case: O(n^2) { if the input is in descending order}

def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i-1

        while(arr[j]>current and j>=0):
            arr[j+1]=arr[j]
            j -= 1

        arr[j+1]=current
    return arr


def main():
    arr = [4,2,1,9,6,5]
    print("Entered arr: ", arr)

    result = insertion_sort(arr)
    print("Sorted arr: ", result)
    pass

if __name__ == "__main__":
    main()