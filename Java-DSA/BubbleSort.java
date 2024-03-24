import java.util.Arrays;

class BubbleSort {
  public static void main(String[] args) {
    System.out.println("Program for bubble sort\n");

    int[] arr = {22,43,21,3,40,1};
    System.out.println("Entered array : "+ Arrays.toString(arr));

    int[] result = bubbleSort(arr);
    System.out.println("Sorted Array: "+ Arrays.toString(result));
  }


  public static int[] bubbleSort(int[]arr) {

    int size = arr.length;
    for(int i = 0; i < size; i++){

      for(int j = 0; j < size-1; j++){
        int temp = 0;
        if(arr[j] > arr[j+1]){
          temp = arr[j];
          arr[j] = arr[j+1];
          arr[j+1] = temp;

        }
      }
    }
    return arr;
  }
}