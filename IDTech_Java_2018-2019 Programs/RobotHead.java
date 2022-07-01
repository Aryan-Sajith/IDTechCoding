package robothead;

import processing.core.PApplet;

public class RobotHead extends PApplet {

    public static void main(String[] args) {
        PApplet.main("robothead.RobotHead");
    }

    public void settings() {
        size (700, 800);
    }

    public void setup() {
        background(255,255,255);
    }

    public void draw() {
        face(100,200);
    }

    public void face(float xPos, float yPos){
        fill(0,255,0);
        rect(xPos,yPos,400,200);
        eyes(xPos+40,yPos+40);
        mouth(xPos+125,yPos+150);
        earLeft(xPos-25,yPos+50);
        earRight(xPos+400,yPos+50);
    }

    public void eyes(float eyeX, float eyeY){
        fill(0,0,0);
        ellipse(eyeX,eyeY,75,75);
        ellipse(eyeX+300,eyeY,75,75);
    }

    public void mouth(float mouthX, float mouthY){
        fill(255,0,0);
        triangle(mouthX,mouthY,mouthX+150,mouthY,mouthX+75,mouthY+50);
    }

    public void earLeft(float earXL,float earYL){
        fill(128,0,128);
        rect(earXL,earYL,25,100);
        fill(0,0,0);
        line(earXL,earYL+100,earXL-50,earYL);
        line(earXL-50,earYL,earXL,earYL);

    }

    public void earRight(float earXR, float earYR){
        fill(128,0,128);
        rect(earXR,earYR,25,100);
        fill(0,0,0);
        line(earXR+25,earYR+100,earXR+75,earYR);
        line(earXR+75,earYR,earXR,earYR);
    }

}