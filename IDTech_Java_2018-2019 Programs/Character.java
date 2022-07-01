public class Character {

    public static String[] nameList = {"Aryan","John", "Smith"};

    public Character(){
        this.name = nameList[Arena.generator.nextInt(nameList.length)];
    }

    public Character(int str, int def, int health){
        this();
        // super();
        this.strength = str;
        this.defense = def;
        this.health = health;
    }

    public String name;
    public int strength;
    public int health;
    public int defense;

    public int takeDamage(int damage){
        int damageTaken = damage-this.defense;
        this.health -= damageTaken;
        return damageTaken;
    }

    public int attack(Character target){
        int damage = this.strength*2;
        int damageDealt = target.takeDamage(damage);
        return damageDealt;
    }
    public boolean isAlive(){
         return this.health > 0;
    }

    public static void main(String[] args) {

    }
}
