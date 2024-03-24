import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = {2,7,1,0,5,3,9};

        int[] result = insertionSort(arr);
        System.out.println(Arrays.toString(result));
    }

    public static int[] insertionSort(int[] arr){

        for(int i=1; i<arr.length; i++){
            int temp = arr[i];

            int j = i-1;
            while (j>=0 && arr[j]>temp) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
        return arr;
    }
}
