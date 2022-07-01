public class BinarySearch {
    public static void main(String[] args) {
        int[] entries = {1,2,3,4,5,6,7,8,9,10};
        System.out.println(binarySearch(entries,4));
    }

    public static int binarySearch(int[] values,int x ){
        int low = 0;
        int high = values.length-1;
        while(low<high){∂
            int midpoint = (low+high)/2;
            if(values[midpoint] == x){
                return midpoint;
            }
            else if(values[midpoint] > x){
                high = midpoint;
            }
            else if(values[midpoint]< x){
                low = midpoint;
            }
            System.out.println(midpoint);
        }
        return -1;
    }
}