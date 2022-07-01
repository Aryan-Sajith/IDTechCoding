public class LinearSearch {
    public static void main(String[] args) {
        int[] entries = {32,14,85,62,10};
        System.out.println(linearSearch(entries,62));
    }
    public static int linearSearch(int[] values, int key){
        for(int i = 0; i < values.length; i++ ){
            if (values[i] == key) {
                return values[i];
            }
        }
        return -1;
    }
}
