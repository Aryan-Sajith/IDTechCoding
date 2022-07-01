public class HeroPrinter {
    public static void main(String[] args) {
        //Variable Declaration - Creation of variable by stating type and name.
        int strength;
        int mana;
        double health;
        double luck;
        String name;


        //Variable Initializiation- The assignment of values to declared variables while or post declaration.
        strength = 4;
        mana = 50;
        health = 12.5;
        luck = 69.96;
        name = "Aerius";

        //Printing values
        System.out.println("Strength: " + strength);
        System.out.println("Mana: " + mana);
        System.out.println("Health: " + health);
        System.out.println("Luck: " + luck);
        System.out.println("Superhero Name: " + name);

        // Taking Damage!
        health -= 2;
        System.out.println("Dr. Rhinocerous swung his axe and hit you for 2 damage!");
        System.out.println("Health: " + health);

        //Training to get Stronger.
        strength *= 2;
        System.out.println("You trained for a month for a rematch and doubled your strength");
        System.out.println("Strength: " + strength);
    }
}
