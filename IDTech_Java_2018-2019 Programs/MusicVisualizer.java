import processing.core.PApplet;
import ddf.minim.*;
import ddf.minim.analysis.FFT;

public class MusicVisualizer extends PApplet {
    private Minim minim;
    private AudioPlayer audio;
    private int yCenter;
    private int xCenter;
    private final int blue = color(20, 50, 200);
    private final int green = color(20, 200, 50);
    private FFT fft;

    public static void main(String[] args) {
        PApplet.main("MusicVisualizer");
    }

    public void settings() {
        size(1000, 500);
    }

    public void setup() {
        background(0);
        yCenter = height/2;
        xCenter = width / 2;
        minim = new Minim(this);
        audio = minim.loadFile("resources/piano.mp3");
        fft = new FFT(audio.bufferSize(), audio.sampleRate());
        audio.loop();
    }

    public void draw() {
        background(0);

        float[] leftChannel = audio.left.toArray();
        float[] rightChannel = audio.right.toArray();
        fft.forward(audio.mix);

        for (int i = 0; i < leftChannel.length - 1; i++) {
            drawChannel(leftChannel, i, -1, blue);
            drawChannel(rightChannel, i, 1, green);
        }
        for (int i = 0; i < fft.specSize(); i++) {
            drawFrequency(i);
        }
    }
    private void drawFrequency(int index){
        stroke(255,0);
        for (int i = 1; i <= 12; i++) {
            fill(255,(float) 100/sq(i));
            circle(xCenter,yCenter,fft.getBand((int) (index * 1 * i)));
        }

    }

    private void drawChannel(float[] channel, int index, int direction, int color){
        strokeWeight(2);

        for (int i = 1; i <= 3; i++) {
            stroke(color, (float) 100 / sq(i));
            line(index,
                    yCenter + (direction * abs(channel[index] *  (150 * sq(i)))),
                    index + 1,
                    yCenter + (direction * abs(channel[index + 1] *  (150 * sq(i)))));
        }

    }
}