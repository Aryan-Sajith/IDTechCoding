package imagetest;

import processing.core.PApplet;
import processing.core.PImage;

public class ImageTest extends PApplet {
    PImage duck;
    PImage backGround;

    public static void main(String[] args) {
        PApplet.main("imagetest.ImageTest");
    }

    public void settings() {
        size(500, 500);
    }

    public void setup() {
        duck = loadImage("Images/Duck.png");
        backGround = loadImage("Images/Sky.png");
    }

    public void draw() {
        background (210,105,30);
        image(duck, 0, 0);
        tint(0, 153, 204, 150);
        duck.resize(500,500);
    }

}