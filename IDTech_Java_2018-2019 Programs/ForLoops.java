public class ForLoops {
    public static void main(String[] args) {
        String[] inventory = new String[5];
        inventory[0] = "HP Potion";
        inventory[1] = "Magic Sword";
        inventory[2] = "Wooden Shield";

        for (int i=0; i< inventory.length; i++){
            String item = inventory[i];
            if (item != null){
                System.out.println(inventory[i]);
            }
        }
    }
}


// OOP.
// classes.
// constructors.
// methods - return, parameters.
// void, int, String.
// static = applies to whole class and not instance of class.
// this = way to specify the specific instance of a class.
// arrays and for/while loops.
