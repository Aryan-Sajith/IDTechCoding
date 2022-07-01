public class Arrays {
    public static void main(String[] args) {
        String[] monsters = {"ghost","zombie","vampire"};
        System.out.println(monsters[0]);
        monsters[2] = "Frankenstein";
        System.out.println(monsters[2]);
        System.out.println(monsters.length);
        System.out.println(monsters[monsters.length-1]);
    }
}
