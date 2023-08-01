package models;
import toyInterface.ToyInterface;

public class Models extends AbstractClass implements ToyInterface, Comparable<Models> {

    public Models(int id, String name, int count, int frequency) {
        this.id = id;
        this.name = name;
        this.count = count;
        this.frequency = frequency;
    }

    public Models(int id, String name, int count) {
        setId(id);
        setName(name);
        setCount(count);
    }

    public Models() {
    }

    @Override
    public int getId() {
        return super.getId();
    }

    @Override
    public int setId(int id) {
        super.setId(id);
        return id;
    }

    @Override
    public String getName() {
        return super.getName();
    }

    @Override
    public void setName(String name) {
        super.setName(name);
    }

    @Override
    public int getCount() {
        return super.getCount();
    }

    @Override
    public void setCount(int count) {
        super.setCount(count);
    }

    @Override
    public int getFrequency() {
        return super.getFrequency();
    }

    @Override
    public void setFrequency(int frequency) {
        super.setFrequency(frequency);
    }

    @Override
    public String toString() {
        return "ID игрушки: " + getId() + ". Название игрушки: " + getName() +
                ". Вероятность выпадения: " + getFrequency() + "\n";
    }

    @Override
    public Models addToys(int id, String name, int count, int frequency) {
        return null;
    }

    @Override
    public int compareTo(Models o) {
        return sorted(getFrequency());
    }

    private int sorted(int frequency) {
        return sorted(frequency);
    }
}
