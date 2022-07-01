import java.util.Scanner;

public class SavingTheDay {
    public static void main(String[] args) {
        int heroMagic = 39;
        int numLights;
        boolean heroHasGauntlet = true;
        Scanner numLightsInput = new Scanner(System.in);

        System.out.println("How many lights to be saved?");
        numLights = numLightsInput.nextInt();

        if(heroMagic > numLights){
            System.out.println("You saved the day!");
        }
        else{
            System.out.println("Hero has fainted due to lack of strength!");
        }
    }
}
