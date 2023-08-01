package models;

public class AbstractClass {
    int id;
    String name;

    int count;

    int frequency;

    public AbstractClass(int id, String name, int count, int frequency) {
        this.id = id;
        this.name = name;
        this.count = count;
        this.frequency = frequency;
    }

    public AbstractClass() {
    }

    public int getId() {
        return id;
    }

    public int setId(int id) {

        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {

    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public int getFrequency() {
        return frequency;
    }

    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }
}

