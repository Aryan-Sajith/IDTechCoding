import java.util.Scanner;

public class MadLibs {
    public static void main(String[] args) {
        intro();
        Scanner userInput = new Scanner(System.in);

        getUserInput("Enter an adjective: ");
        String adjective = userInput.nextLine();

        getUserInput("Enter an noun: ");
        String noun = userInput.nextLine();

        printMadLib(adjective,noun);
    }
    public static void intro() {
        System.out.println("Welcome to MadLibs!");
    }
    public static void printMadLib(String adjective, String noun){
        System.out.println(adjective +" MacDonald had a " + noun);
    }
    public static String getUserInput(String message){
        System.out.println(message);
        return "This is a string";
    }
}
