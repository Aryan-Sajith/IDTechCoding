//Scanner allows pausing the program and waiting for the user to type something so result can be saved.
// \/
// Scanner is a class/datatype and contains the ability to read user input rather than a single value.
import java.util.Scanner;

public class HeroCreator {
    public static void main(String[] args) {
        // Create scanner variable.
        Scanner playerInput;
        // Create a Scanner method and assign to playerinput variable to read input from console.
        playerInput = new Scanner(System.in);

        Scanner numberInput = new Scanner(System.in);
        Scanner textInput = new Scanner(System.in);

        String heroName;
        double heroHealth;
        int heroStr;
        int heroAgi;
        int heroDef;
        String heroSkills;

        System.out.println("What is your Hero's name?");
        // One method that relies on prior use of Scanner method.
        heroName = playerInput.nextLine();
        System.out.println("Welcome, " + heroName );
        System.out.println("Stats check time!\nStrength?");
        heroStr = numberInput.nextInt();
        System.out.println("Health?");
        heroHealth = numberInput.nextDouble();
        System.out.println("Agility?");
        heroAgi = numberInput.nextInt();
        System.out.println("Defense?");
        heroDef = numberInput.nextInt();
        System.out.println("What are his primary skills?");
        heroSkills = textInput.nextLine();
        System.out.println("Hello " + heroName + "\nSTATS=\nStr:" + heroStr + "\nAgi:" + heroAgi +"\nhealth:" + heroHealth + "\nDef:" + heroDef + "\nSKILLS= \n" + heroSkills);



 }
}
