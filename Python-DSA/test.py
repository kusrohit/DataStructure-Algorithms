# for i in range(4,-1,-1):
#     print(i)


def insertion(arr):
    # first element holds

    for i in range(1, len(arr)):
        temp = arr[i]

        j = i-1
        while(j>=0 and arr[j]>temp):
            # shift the value
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

def main():
    arr = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
    result = insertion(arr)
    print(result)

if __name__ == "__main__":
    main()