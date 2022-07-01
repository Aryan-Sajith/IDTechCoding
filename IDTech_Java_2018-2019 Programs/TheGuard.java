import java.util.Scanner;

//variables are true by default
public class TheGuard {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        int playerClass;
        int playerChoice;

        //Get the player's class choice
        System.out.println("Choose a class:\n1 - Warrior\n2 - Thief\n3 - Mage");
        playerClass = userInput.nextInt();

        //Player chooses an action
        System.out.println("There is a guard here, what do you do?");
        System.out.println("1 - Fight him");
        System.out.println("2 - Steal his wallet");
        System.out.println("3 - Throw a fireball");
        System.out.println("4 - Talk the guard into leaving");
        System.out.println("5 - Intimidate the guard");
        System.out.println("6 - Bond with the guard over your shared disdain for magic");

        playerChoice = userInput.nextInt();

        if (playerClass == 1 && playerChoice == 1) {
            System.out.println("You overpower him easily... This is your bread and butter after all!");
        }
        else if (playerClass == 2 && playerChoice == 2) {
            System.out.println("You wisp throw the shadows and pick his pocket without notice... it holds a health amulet... You knock him over easily.");
        }
        else if (playerClass == 3 && playerChoice == 3) {
            System.out.println("You toss a fireball which temporarily stuns the warrior... You take the window of opportunity to summon acid rain and finish him off. ");
        }
        else if ((playerClass == 2 || playerClass == 3) && playerChoice == 4) {
            System.out.println("You try walking past the guard unnoticed when you accidentally trigger a magic bomb " +
                    "which sets off a huge explosion. After a long pause you notice a bruised guard to be protecting you with his shield..." +
                    "It seems we barely made it out of this one alive! After a hearty long chat, you convince the warrior" +
                    "to take some time off duty. ");
        }
        else if ((playerClass == 1 || playerClass == 3) && playerChoice == 5) {
            System.out.println("You walk up to the guard, a fierce look in your eyes. He sees you clenching your" +
                    "artillery of choice and chooses the day not to be the wisest to go looking for a fight." +
                    " He unsheathes his blade and walks off.");
        }
         else if (!(playerClass == 3) && playerChoice == 6){
             System.out.println("You try to gain the guard's attention but he seems busy staring off into oblivion." +
                     "You notice a wanted poster lying on the nearest wall stating a bounty of 10 million zenkils" +
                     "for the hunt of legendary earth mage Garren. You sigh and ask if the guard has heard about him" +
                     "at all... He returns the sigh with a tasteful look and appreciates the gesture." +
                     "You spend the next few hours conversing over the superiority complex of medieval mages.");

         }
         else{
             System.out.println("The guard scoffs at your pathetic attempt to get rid of him. He takes a brief look over" +
                     "his shoulder and immediately goes back to what he is doing.... Hey, #non-main characters matter");
        }
        }
    }
