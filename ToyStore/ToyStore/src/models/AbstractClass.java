package models;

public class AbstractClass {
    int id;
    String name;

    int count;

    double frequency;

    public AbstractClass(int id, String name, int count, double frequency) {
        this.id = id;
        this.name = name;
        this.count = count;
        this.frequency = frequency;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public double getFrequency() {
        return frequency;
    }

    public void setFrequency(double frequency) {
        this.frequency = frequency;
    }
}

