public class Rouge extends Character {

    public int dexterity = 20;

    // make a constructor that inherits from Character.java
    public Rouge(){
        super(); // inherits from Character.java

        // manually redefining str, def, health params from Character.java constructor
        this.strength = 8;
        this.defense = 4;
        this.health = 100;
    }

    // override attack() from Character.java
    public int attack(Character target){
        // true if less than dexterity; false if not
        boolean criticalHit = Arena.generator.nextInt(100) < dexterity;
        int damage = this.strength * 2;
        if (criticalHit){// criticalHit == True
            damage *=2; // damage doubled
            System.out.println("*** Critical Hit***");// use DOUblE quotes for string, char uses single quotes 'a', 'b' , etc.
        }
        int damageDealt = target.takeDamage(damage);
        return damageDealt; // return int
    }

}
