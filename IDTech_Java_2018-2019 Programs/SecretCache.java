import java.util.Random;

public class SecretCache {
    public static void main(String[] args) {
        // Create random variable just like scanner variable \/
        Random generator = new Random();
        int dollars;
        // Random next int, next double, next boolean -
        // [0 , x-1] for int,
        // [0,1] for double,
        // T/F for boolean.
        // ... can be modified with arithmetic operators 2/3 \/
        dollars = generator.nextInt(500000);
        System.out.println("You stumble upon the thieves' cache and find " + dollars + " dollars!");
    }
}
