package models;

public class Models extends AbstractClass{
    public Models(int id, String name, int count, int frequency) {
        setId(id);
        setName(name);
        setCount(count);
        setFrequency(frequency);
    }
/*
    public Models() {
        this.id = 0;
        this.name = " ";
        this.count = 0;
        this.frequency = 0;
    }
*/
    @Override
    public int getId() {
        return super.getId();
    }

    @Override
    public void setId(int id) {
        super.setId(id);
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
                ". Количество игрушек: " + getCount() + "\n";
    }

}
