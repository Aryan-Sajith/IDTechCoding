public class Villain {
    public static void main(String[] args) {
        //Var Declarations + Initializations
        String name = "Dr Rhinocerous";
        String weapon = "Brutal Axe";
        int str = 6;
        int agi = 3;
        double health = 35;
        double luck = 69;

        //Print Vals.
        System.out.println("Name: " + name);
        System.out.println("Weapon: " + weapon);
        System.out.println("Strength: " + str);
        System.out.println("Agility: " + agi);
        System.out.println("Health: " + health);
        System.out.println("Luck: " + luck);

        // Took damage.
        health += 30;
        System.out.println("You knocked Aryan out and acquired his amulet of small health");
        System.out.println("Health: " + health);

    }
}
