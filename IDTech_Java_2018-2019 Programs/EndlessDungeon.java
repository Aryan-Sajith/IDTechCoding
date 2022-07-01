import java.util.Random;

public class EndlessDungeon {
    public static void main(String[] args) {
        System.out.println("You are a knight and have found a cave that leads to mystical dungeons. They replenish" +
                "on every visit and are truly the best places to master your craft.");
        Random generator = new Random();
        int playerHealth, enemyHealth;
        int playerDamage, enemyDamage;
        playerHealth = 100;
        enemyHealth = generator.nextInt(10) + 1;


        while (playerHealth > 0) {
            System.out.println("You have " + playerHealth + " health.");

            playerDamage = generator.nextInt(5) + 1;
            enemyDamage = generator.nextInt(3) + 1;

            playerHealth -= enemyDamage;
            enemyHealth -= playerDamage;

            System.out.println("You attack the enemy for " + playerDamage);
            System.out.println("The enemy attacks you for " + enemyDamage);
        }
    }
}
