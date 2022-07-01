public class SelectionSort {
    public static void main(String[] args) {
        int[] values = {3,1,9,5,6,2};
        selectionSort(values);
    }
    public static void selectionSort(int[] values){
    int arrLen = values.length;

    for(int i= 0; i < arrLen-1;i++){
        int smallest = i;
        for(int j = i+1; j< arrLen; j++){
            if (values[j]<values[smallest]){
                smallest = j;
            }
        }
        int temp = values[smallest];
        values[smallest] = values[i];
        values[i] = temp;
    }
    for(int i = 0;i < values.length; i++){
            System.out.println(" " + values[i]);
        }
    }
}
